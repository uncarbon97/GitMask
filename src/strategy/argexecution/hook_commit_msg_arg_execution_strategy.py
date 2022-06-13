import os

from src.constant import msg_constant, file_constant, template_constant
from src.exception.business_exception import BusinessException
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy
from src.util import file_util


class HookCommitMsgArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    hook commit-msg 策略
    """
    def execute_strategy(self):
        cwd = file_util.get_cwd()
        hook_dir = os.path.join(cwd, '.git', 'hooks')
        if not file_util.exists_dir(hook_dir):
            raise BusinessException(msg_constant.FATAL_NOT_FOUND_GIT_HOOKS, cwd)

        # 拿到命令行参数中的[需求配置文件名]
        commandline_args = self.get_commandline_args()
        required_file_name = commandline_args.commit_required_file_name

        commit_msg_full_path = os.path.join(hook_dir, file_constant.COMMIT_MSG)
        if file_util.exists_file(commit_msg_full_path):
            file_util.rename_file(commit_msg_full_path, commit_msg_full_path + '.bak')

        with open(commit_msg_full_path, 'w+') as f:
            if f.write(template_constant.TEMPLATE_COMMIT_MSG.format(
                required_file_name,
                required_file_name,
            )):
                print(msg_constant.SUCCESS_INSTALL_COMMIT_MSG_HOOK)
                return

        raise BusinessException(msg_constant.FATAL_INSTALL_COMMIT_MSG_HOOK)
