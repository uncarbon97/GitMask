import argparse

from src.constant import file_constant
from src.exception.business_exception import BusinessException
from src.strategy.argexecution.assign_arg_execution_strategy import AssignArgExecutionStrategy
from src.strategy.argexecution.hook_commit_msg_arg_execution_strategy import HookCommitMsgArgExecutionStrategy
from src.strategy.argexecution.register_arg_execution_strategy import RegisterArgExecutionStrategy
from src.strategy.argexecution.version_arg_execution_strategy import VersionArgExecutionStrategy
from src.strategy.argexecution.ls_arg_execution_strategy import LsArgExecutionStrategy
from src.strategy.argexecution.equals_arg_execution_strategy import EqualsArgExecutionStrategy

ARG_PARSER = argparse.ArgumentParser(description='GitMask')
ARG_EXECUTION_STRATEGY_MAP = {
    'register': RegisterArgExecutionStrategy,
    'version': VersionArgExecutionStrategy,
    'ls': LsArgExecutionStrategy,
    'equals_file_name': EqualsArgExecutionStrategy,
    'assign_file_name': AssignArgExecutionStrategy,
    'commit_required_file_name': HookCommitMsgArgExecutionStrategy,
}


def config_arg_parse():
    """
    配置命令行参数解析
    :return: void
    """
    # action='store_true' 用来免参数(不能 nargs=0)
    # nargs 表示后面跟的参数数量
    # type 表示后面跟的参数类型
    # dest 表示占位符名称
    ARG_PARSER.add_argument('--register', help='register into system PATH', action='store_true')
    ARG_PARSER.add_argument('--version', help='show GitMask version', action='store_true')
    ARG_PARSER.add_argument('--ls', help='list *.gitconfig', action='store_true')
    ARG_PARSER.add_argument('--equals',
                            help='check if system\'s {} equals {}{}'.format(
                                file_constant.DOT_GITCONFIG,
                                '[EQUALS_FILE_NAME]',
                                file_constant.DOT_GITCONFIG,
                                file_constant.DOT_GITCONFIG
                            ),
                            type=str,
                            dest='equals_file_name',
                            )
    ARG_PARSER.add_argument('--assign',
                            help='assign {}{} into system'.format(
                                '[ASSIGN_FILE_NAME]',
                                file_constant.DOT_GITCONFIG
                            ),
                            type=str,
                            dest='assign_file_name'
                            )
    ARG_PARSER.add_argument('--icm',
                            help="Install Commit-Msg hook into .git/hooks . so that ensure 'git commit' with {}{}"
                            .format(
                                '[COMMIT_REQUIRED_FILE_NAME]',
                                file_constant.DOT_GITCONFIG
                            ),
                            type=str,
                            dest='commit_required_file_name'
                            )


def get_commandline_args() -> argparse.Namespace:
    return ARG_PARSER.parse_args()


if __name__ == '__main__':
    config_arg_parse()
    args = get_commandline_args()

    for function, function_enabled in args.__dict__.items():
        if function_enabled and ARG_EXECUTION_STRATEGY_MAP.get(function):
            # 启用功能，且存在可用策略类
            strategy_class = ARG_EXECUTION_STRATEGY_MAP[function]
            if strategy_class:
                # 创建策略对象，并执行预置的策略
                strategy = strategy_class()
                strategy.set_commandline_args(commandline_args=args)

                # try 执行，方便打印异常消息
                try:
                    strategy.execute_strategy()

                except BusinessException as be:
                    print(str(be))

                # 跳出循环
                break
