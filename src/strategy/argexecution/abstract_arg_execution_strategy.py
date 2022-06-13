import argparse

from src.constant import file_constant
from src.util import file_util


class AbstractArgExecutionStrategy:
    """
    抽象命令行参数执行器策略
    """
    __commandline_args: argparse.Namespace = None

    def get_commandline_args(self) -> argparse.Namespace:
        """
        commandline_args GETTER
        :return: commandline_args: 命令行参数
        """
        return self.__commandline_args

    def set_commandline_args(self, commandline_args: argparse.Namespace):
        """
        commandline_args SETTER
        :param commandline_args: 命令行参数
        :return: void
        """
        self.__commandline_args = commandline_args

    def execute_strategy(self):
        """
        执行策略
        :return: void
        """
        pass


    def get_system_gitconfig_full_path(self) -> str:
        """
        取系统 .gitconfig 文件全路径
        :return:
        """
        return '{}{}{}'.format(
            file_util.get_user_home_path(),
            file_constant.FILE_SEPARATOR,
            file_constant.DOT_GITCONFIG
        )
