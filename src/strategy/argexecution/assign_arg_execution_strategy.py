from src.constant import file_constant, msg_constant
from src.exception.business_exception import BusinessException
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy
from src.strategy.argexecution.equals_arg_execution_strategy import EqualsArgExecutionStrategy
from src.util import file_util


class AssignArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    指定 .gitconfig 覆盖系统 .gitconfig 策略
    """

    # equals 策略类实例
    __equals_strategy: EqualsArgExecutionStrategy = EqualsArgExecutionStrategy()

    def execute_strategy(self):
        # 拿到命令行参数中的[待覆盖文件名]
        commandline_args = self.get_commandline_args()
        assign_file_name = commandline_args.assign_file_name

        # 如果执行无误，就能拿到本地 gitconfig 全路径
        self.__equals_strategy.equals_gitconfig(file_name=assign_file_name)

        if not self.__equals_strategy.get_latest_equals_result():
            # 不相符则替换文件
            gitconfig_full_path = self.__equals_strategy.get_latest_gitconfig_full_path()
            system_gitconfig_full_path = self.__equals_strategy.get_system_gitconfig_full_path()

            file_util.copy_file(gitconfig_full_path, system_gitconfig_full_path)
            print(msg_constant.SUCCESS_ASSIGN_INTO.format(gitconfig_full_path, system_gitconfig_full_path))
            return

        raise BusinessException(msg_constant.FATAL_ASSIGN_FAIL, gitconfig_full_path, system_gitconfig_full_path)
