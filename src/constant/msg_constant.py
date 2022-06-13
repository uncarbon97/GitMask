"""
消息常量
"""

# 路径为目录，而非文件
FATAL_PATH_IS_DICTIONARY_NOT_A_FILE = '''
Fatal: {} is a dictionary, not a file!
'''

# 文件不存在（一个都没有）
FATAL_GITCONFIGS_NOT_FOUND = '''
Fatal: Cannot found any *.gitconfig in {}
'''

# 特定文件不存在
FATAL_GITCONFIG_NOT_FOUND = '''
Fatal: Cannot found {}, please run 'gitmask --ls' to check.
'''

# 成功覆盖到系统
SUCCESS_ASSIGN_INTO = '''
Success: assigned {} into {} 
'''

# 覆盖到系统失败
FATAL_ASSIGN_FAIL = '''
Fatal: Cannot assign {} into {}, please check your system and permissions.
'''

# 未找到 .git/hooks 目录
FATAL_NOT_FOUND_GIT_HOOKS = '''
Fatal: Cannot found .git/hooks in {}, are you sure already executing 'git init' ?
'''

# 成功写入 commit-msg hook
SUCCESS_INSTALL_COMMIT_MSG_HOOK = '''
Success: installed commit-msg hook into .git/hooks , please try it!
'''

# 写入 commit-msg hook 失败
FATAL_INSTALL_COMMIT_MSG_HOOK = '''
Fatal: Cannot install commit-msg hook into .git/hooks , please check your system and permissions.
'''

# 写入 PATH_BACKUP 作为备份
SET_PATH_BACKUP = '''
Backup PATH into {} ...
'''

# 不支持的操作系统
FATAL_UNSUPPORTABLE_OS = '''
Fatal: your OS: {} is still unsupportable, welcome for your Pull Request!
'''

# 成功写入 PATH
SUCCESS_REGISTER = '''
Success: registered GitMask into your system PATH
'''