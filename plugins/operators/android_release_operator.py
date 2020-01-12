from airflow.utils.decorators import apply_defaults

from operators.release_ci_operator import ReleaseCIOperator

class AndroidReleaseOperator(ReleaseCIOperator):
    @apply_defaults
    def __init__(self, repo_name, tag_id, tag_sha, runner_conf, *args, **kwargs):
        super(AndroidReleaseOperator, self).__init__(
            repo_name=repo_name,
            tag_id=tag_id,
            tag_sha=tag_sha,
            queue='android',
            runner_conf=runner_conf,
            release_xcom_key='android_release',
            *args,
            **kwargs
        )

    def verify_release(self, release_files):
        if release_files is None or len(release_files) < 2:
            return False

        expected_type='application/vnd.android.package-archive'
        expected_names=['app-debug.apk', 'app-debug-androidTest.apk']

        for file in release_files:
            if file.type == expected_type and file.name in expected_names:
                expected_names.remove(file.name)

        return len(expected_names) == 0