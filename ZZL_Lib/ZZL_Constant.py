import os


NAME_SHORT = 'ZZL'
NAME = 'ZZL'
PACKAGE_NAME = 'ZZL'
CLI_COMMAND = PACKAGE_NAME

VERSION = '2.10.2'
VERSION_PYPI = '2.10.2'

GITHUB_URL = 'https://github.com/Casper233/ZZL'
GITHUB_API_LATEST = 'https://api.github.com/repos/Casper233/ZZL/releases/latest'
DOCUMENTATION_URL = 'https://github.com/Casper233/ZZL#readme'

PACKAGE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
LOGGING_FILE = os.path.join('logs', '{}.log'.format(NAME_SHORT))
