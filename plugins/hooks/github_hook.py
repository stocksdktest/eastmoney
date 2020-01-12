

from github import Github

from airflow.exceptions import AirflowException
from airflow.hooks.base_hook import BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin


class GithubHook(BaseHook, LoggingMixin):
    def __init__(self, conn_id='github_default', *args, **kwargs):

        self.github_conn_id = conn_id
        self.connection = self.get_connection(conn_id)
        self.extras = self.connection.extra_dejson.copy()
        self.__token = self.extras['access_token']
        self.client = None

    def get_conn(self):
        if self.client is not None:
            return self.client
        self.client = Github(login_or_token=self.__token).get_user()
        return self.client

    def get_repo(self, repo_name):
        """
        :param repo_name:
        :type repo_name: str
        :return: Repository
        """
        conn = self.get_conn()

        for repo in conn.get_repos():
            if repo.full_name == repo_name:
                return repo
        return None

    def check_release_sha(self, repo, release_id, release_sha):
        """
        :param repo:
        :type repo: Repository
        :param release_id:
        :type release_id: str
        :param release_sha:
        :type release_sha: str
        :return: bool
        """
        for tag in repo.get_tags():
            if tag.name == release_id and tag.commit is not None and tag.commit.sha == release_sha:
                return True
        return False

    def get_release_assets(self, repo, release_id):
        release = repo.get_release(release_id)
        if release is None:
            return None

        return release.get_assets()
