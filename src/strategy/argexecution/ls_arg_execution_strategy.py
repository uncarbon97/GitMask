import os
import sys

from typing import List

from src.constant import file_constant, msg_constant
from src.exception.business_exception import BusinessException
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy
from src.util import file_util


class LsArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    枚举 .gitconfig 策略
    """

    # 预置枚举目录顺序
    __ENUM_DIRS = (
        # 1. 运行目录
        file_util.get_working_dir(),
        # 2. 当前目录
        file_util.get_cwd(),
    )

    # 枚举到的所有 gitconfig 文件全路径
    __gitconfigs: List[str] = list()

    def execute_strategy(self):
        self.enum_gitconfigs()

        self.assert_gitconfigs_not_empty()

        for each in self.get_gitconfigs():
            print(each)

    def enum_gitconfigs(self):
        """
        枚举 gitconfig 文件
        如果每次都重新枚举影响效率，可以考虑枚举完后记录到某个文件作为缓存；枚举前判断缓存是否超时
        :return: void
        """
        self.__gitconfigs = []
        for dir_ in self.__ENUM_DIRS:
            files = file_util.enum_files(start_path=dir_,
                                         extend_name=file_constant.DOT_GITCONFIG,
                                         )
            self.__gitconfigs.extend(files)

    def get_gitconfigs(self):
        # 如果每次都重新枚举影响效率，可以考虑枚举完后记录到某个文件作为缓存，这个方法直接从缓存读
        return self.__gitconfigs

    def assert_gitconfigs_not_empty(self):
        """
        断言 __gitconfigs 不为空，否则抛异常
        :return:
        """
        if len(self.__gitconfigs) <= 0:
            # 一个可用文件都没有
            raise BusinessException(msg_constant.FATAL_GITCONFIGS_NOT_FOUND, self.__ENUM_DIRS)
