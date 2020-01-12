from airflow.exceptions import AirflowException
from airflow.utils.decorators import apply_defaults

from operators.stock_operator import StockOperator
from hooks.github_hook import GithubHook

class ReleaseFile(object):
    def __init__(self, git_release_asset=None):
        if not git_release_asset:
            return
        self.name = git_release_asset.name
        self.type = git_release_asset.content_type
        self.url = git_release_asset.browser_download_url

    def __str__(self):
        return 'ReleaseFile(name=%s, type=%s, url=%s)' % (self.name, self.type, self.url)

    def __repr__(self):
        return self.__str__()

class ReleaseCIOperator(StockOperator):
    @apply_defaults
    def __init__(self, repo_name, tag_id, tag_sha, release_xcom_key, queue, runner_conf, *args, **kwargs):
        super(ReleaseCIOperator, self).__init__(queue=queue, runner_conf=runner_conf, *args, **kwargs)
        self.repo_name = repo_name
        self.tag_id = tag_id
        self.tag_sha = tag_sha
        self.release_xcom_key = release_xcom_key

    def verify_release(self, release_files):
        """
        :param release_files
        :type release_files: list(ReleaseFile)
        """
        raise NotImplementedError()

    def execute(self, context):
        github_client = GithubHook(conn_id=self.repo_name)
        repo = github_client.get_repo(self.repo_name)
        if repo is None:
            raise AirflowException('repo %s not found' % self.repo_name)

        if not github_client.check_release_sha(repo, self.tag_id, self.tag_sha):
            raise AirflowException('tag %s sha %s not match' % (self.tag_id, self.tag_sha))

        release_assets = github_client.get_release_assets(repo, self.tag_id)
        release_files = [ReleaseFile(item) for item in release_assets]

        if not self.verify_release(release_files):
            raise AirflowException('release files not verify: %s' % release_files)

        self.xcom_push(context, key=self.release_xcom_key, value=release_files)
