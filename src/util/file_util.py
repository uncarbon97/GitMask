"""
文件工具类
不知道 Python 有没有类似 hutool 之类的通用工具类?
"""
import os
import sys
from src.constant import file_constant, msg_constant, env_constant
from src.exception.business_exception import BusinessException


def get_cwd(format_dir_flag: bool = True) -> str:
    """
    取当前目录
    :return: str
    """
    tmp = os.getcwd()
    return format_dir(tmp) if format_dir_flag else tmp


def get_working_dir(format_dir_flag: bool = True) -> str:
    """
    取运行目录，即可执行文件所在目录
    :return: str
    """
    tmp = os.path.dirname(sys.executable)
    return format_dir(tmp) if format_dir_flag else tmp


def format_dir(source: str) -> str:
    """
    格式化文件路径：
    1. \\ 替换为 /
    :param source: 原路径
    :return: 新路径
    """
    ret = source.replace('\\', file_constant.FILE_SEPARATOR)
    return ret


def enum_files(start_path: str, ret: list = None, extend_name: str = None, deep_flag=False) -> list:
    """
    递归遍历
    :param start_path: 必填参数，起始目录
    :param ret: 免填参数，目标保存 list，同时也是返回值
    :param extend_name: 可选参数，扩展名
    :param deep_flag: 可选参数，是否继续向深层目录遍历
    :return:
    """
    if ret is None:
        ret = []

    files = os.listdir(start_path)
    for file in files:
        sub_path = start_path + file_constant.FILE_SEPARATOR + file
        if os.path.isfile(sub_path):
            if extend_name and not sub_path.endswith(extend_name):
                # 不以指定扩展名结尾
                continue

            # 加入 list
            ret.append(sub_path)
        elif os.path.isdir(sub_path):
            if file[0] == '.':
                pass
            elif deep_flag:
                enum_files(start_path=sub_path, ret=ret)

    return ret


def enum_files_walk(start_path: str, extend_name: str = None, with_dir: bool = False) -> list:
    """
    通过 os.walk 简单遍历文件
    :param start_path: 必填参数，起始目录
    :param extend_name: 可选参数，扩展名
    :param with_dir: 可选参数，前面是否补充目录全路径
    :return: 
    """
    ret = list()

    for dir_path, folder, files in os.walk(start_path):
        for file in files:
            if extend_name and not file.endswith(extend_name):
                # 不以指定扩展名结尾
                continue

            if with_dir:
                full_path = '{}{}{}'.format(format_dir(dir_path),
                                            file_constant.FILE_SEPARATOR,
                                            file)
            else:
                full_path = file

            # 加入 list
            ret.append(full_path)

    return ret


def get_user_home_path() -> str:
    """
    取系统用户 HOME 目录
    :return: str
    """
    return format_dir(os.path.expanduser(env_constant.HOME_STUB_CHAR))


def exists_file(full_path: str) -> bool:
    """
    判断文件是否存在
    :param full_path: 文件全路径
    :return: bool
    """
    return os.path.isfile(full_path)


def exists_dir(full_path: str) -> bool:
    """
    判断目录是否存在
    :param full_path: 目录全路径
    :return: bool
    """
    return os.path.isdir(full_path)


def read_bytes(full_path: str) -> bytes:
    """
    以二进制形式读取指定文件
    :param full_path: 文件全路径
    :return: bytes
    """
    if exists_dir(full_path):
        raise BusinessException(msg_constant.FATAL_PATH_IS_DICTIONARY_NOT_A_FILE, full_path)

    if not exists_file(full_path):
        return bytes()

    with open(full_path, 'rb') as f:
        return f.read()


def copy_file(src_path: str, dest_path: str) -> bool:
    """
    复制文件(仅单文件)
    :param src_path: 原始路径
    :param dest_path: 目标路径
    :return: bool
    """
    if not exists_file(src_path) or not exists_file(dest_path):
        return False

    with open(src_path, 'rb') as stream_r:
        container = stream_r.read()
        with open(dest_path, 'wb') as stream_w:
            stream_w.write(container)
            return True
    return False


def rename_file(src_path: str, dest_path: str) -> bool:
    """
    重命名文件(仅单文件)
    :param src_path: 原始路径
    :param dest_path: 目标路径
    :return: bool
    """
    if not exists_file(src_path) or exists_file(dest_path):
        return False

    os.rename(src_path, dest_path)
    return True
