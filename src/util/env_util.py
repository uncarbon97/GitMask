import os
import platform

from src.constant import msg_constant
from src.exception.business_exception import BusinessException


def get_env_value(key: str) -> str:
    """
    取系统环境变量值
    :param key: 键名
    :return:
    """
    return os.environ[key]


def set_env_value_permanently(key: str, value: str):
    """
    置系统环境变量值，！永久性！
    :param key: 键名
    :param value: 键值
    :return:
    """
    if platform.system().lower() == 'windows':
        os.environ[key] = value
        os.system('SETX {} "{}" > nul'.format(key, value))
    else:
        raise BusinessException(msg_constant.FATAL_UNSUPPORTABLE_OS, platform.system())
