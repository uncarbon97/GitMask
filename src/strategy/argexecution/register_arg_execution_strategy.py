from src.constant import env_constant, msg_constant
from src.strategy.argexecution.abstract_arg_execution_strategy import AbstractArgExecutionStrategy
import os
import datetime

from src.util import file_util, env_util


class RegisterArgExecutionStrategy(AbstractArgExecutionStrategy):
    """
    全局注册到系统策略
    """
    def execute_strategy(self):
        old_path = env_util.get_env_value(env_constant.PATH)

        # 备份原 PATH
        path_backup_key = '{}_BACKUP_{}'.format(
            env_constant.PATH,
            datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        )
        print(msg_constant.SET_PATH_BACKUP.format(path_backup_key))
        env_util.set_env_value_permanently(path_backup_key, old_path)

        # 更新 GITMASK_HOME; Win 写入到环境变量里的，不能用 "/" 号
        env_util.set_env_value_permanently(env_constant.GITMASK_HOME, file_util.get_working_dir(format_dir_flag=False))

        # 写入新 PATH; 对 PATH 中原本可能存在的错误进行修正
        old_path = old_path.replace(';;', ';')
        env_util.set_env_value_permanently(env_constant.PATH, '{}{}%{}%'.format(
            old_path,
            # 如果 PATH 最后以 ; 结尾，则不另行添加
            '' if old_path.endswith(';') else ';',
            env_constant.GITMASK_HOME,
        ))

        print(msg_constant.SUCCESS_REGISTER)
