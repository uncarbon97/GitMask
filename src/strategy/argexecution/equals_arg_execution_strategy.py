from src.constant import file_constant, msg_constant
from src.exception.business_exception import BusinessException
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy
from src.strategy.argexecution.ls_arg_execution_strategy import LsArgExecutionStrategy
from src.util import file_util


class EqualsArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    比较指定 .gitconfig 与系统 .gitconfig 异同策略
    """

    # ls 策略类实例
    __ls_strategy: LsArgExecutionStrategy = LsArgExecutionStrategy()

    # 最后一次匹配成功的本地 gitconfig 文件全路径
    __latest_gitconfig_full_path: str = None

    # 最后一次匹配结果
    __latest_equals_result: bool = False

    def execute_strategy(self):
        # 拿到命令行参数中的[待比较文件名]
        commandline_args = self.get_commandline_args()
        equals_file_name = commandline_args.equals_file_name
        self.equals_gitconfig(file_name=equals_file_name, print_equals_result=True)

    def equals_gitconfig(self, file_name: str, print_equals_result: bool = False):
        """
        :param file_name: 不带扩展名的文件名
        :param print_equals_result: 是否打印比较结果
        :return:
        """
        # 重置变量
        self.__latest_equals_result = False

        # 看看是否真的有待比较文件
        self.__ls_strategy.enum_gitconfigs()
        existing_gitconfigs = self.__ls_strategy.get_gitconfigs()

        # 没有可用文件则抛异常
        self.__ls_strategy.assert_gitconfigs_not_empty()

        # 拼出本地完整文件名
        full_file_name = '{}{}'.format(
            file_name,
            file_constant.DOT_GITCONFIG
        )
        gitconfig_full_path = None

        for existing_gitconfig in existing_gitconfigs:
            # 直接尾判断，相符则匹配
            if existing_gitconfig.endswith(full_file_name):
                gitconfig_full_path = existing_gitconfig
                break

        if gitconfig_full_path is None:
            # 没有找到待比较文件
            raise BusinessException(msg_constant.FATAL_GITCONFIG_NOT_FOUND, full_file_name)

        self.__latest_gitconfig_full_path = gitconfig_full_path
        if file_util.read_bytes(self.get_system_gitconfig_full_path()) == file_util.read_bytes(gitconfig_full_path):
            self.__latest_equals_result = True

        if print_equals_result:
            print(self.__latest_equals_result)

    def get_latest_gitconfig_full_path(self) -> str:
        """
        Getter of __latest_gitconfig_full_path
        :return: str
        """
        return self.__latest_gitconfig_full_path

    def get_latest_equals_result(self) -> bool:
        """
        Getter of __latest_equals_result
        :return: bool
        """
        return self.__latest_equals_result
