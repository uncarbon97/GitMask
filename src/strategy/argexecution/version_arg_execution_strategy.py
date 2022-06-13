from src.constant import gitmask_constant
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy


class VersionArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    打印版本号策略
    """
    def execute_strategy(self):
        print('GitMask {}'.format(gitmask_constant.GITMASK_VERSION))
