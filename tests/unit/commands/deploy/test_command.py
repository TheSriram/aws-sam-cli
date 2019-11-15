from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from samcli.commands.deploy.command import do_cli


class TestDeployliCommand(TestCase):
    def setUp(self):

        self.template_file = "input-template-file"
        self.stack_name = "stack-name"
        self.s3_bucket = "s3-bucket"
        self.s3_prefix = "s3-prefix"
        self.kms_key_id = "kms-key-id"
        self.no_execute_changeset = False
        self.notification_arns = []
        self.parameter_overrides = {"a": "b"}
        self.capabilities = "CAPABILITY_IAM"
        self.tags = {"c": "d"}
        self.fail_on_empty_changset = True
        self.role_arn = "role_arn"
        self.force_upload = False
        self.metadata = {"abc": "def"}
        self.region = None
        self.profile = None
        self.use_json = True
        self.metadata = {}

    @patch("samcli.commands.package.command.click")
    @patch("samcli.commands.package.package_context.PackageContext")
    @patch("samcli.commands.deploy.command.click")
    @patch("samcli.commands.deploy.deploy_context.DeployContext")
    def test_all_args(self, mock_deploy_context, mock_deploy_click, mock_package_context, mock_package_click):

        context_mock = Mock()
        mock_deploy_context.return_value.__enter__.return_value = context_mock

        do_cli(
            template_file=self.template_file,
            stack_name=self.stack_name,
            s3_bucket=self.s3_bucket,
            force_upload=self.force_upload,
            s3_prefix=self.s3_prefix,
            kms_key_id=self.kms_key_id,
            parameter_overrides=self.parameter_overrides,
            capabilities=self.capabilities,
            no_execute_changeset=self.no_execute_changeset,
            role_arn=self.role_arn,
            notification_arns=self.notification_arns,
            fail_on_empty_changeset=self.fail_on_empty_changset,
            tags=self.tags,
            region=self.region,
            profile=self.profile,
            use_json=self.use_json,
            metadata=self.metadata,
        )

        mock_deploy_context.assert_called_with(
            template_file=ANY,
            stack_name=self.stack_name,
            s3_bucket=self.s3_bucket,
            force_upload=self.force_upload,
            s3_prefix=self.s3_prefix,
            kms_key_id=self.kms_key_id,
            parameter_overrides=self.parameter_overrides,
            capabilities=self.capabilities,
            no_execute_changeset=self.no_execute_changeset,
            role_arn=self.role_arn,
            notification_arns=self.notification_arns,
            fail_on_empty_changeset=self.fail_on_empty_changset,
            tags=self.tags,
            region=self.region,
            profile=self.profile,
        )

        context_mock.run.assert_called_with()
        self.assertEqual(context_mock.run.call_count, 1)
