# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.82
""" setup of aedev namespace module portion project_vars: project development variables. """
import pathlib
import sys
from typing import Any
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs: dict[str, Any] = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    'description': 'aedev namespace module portion project_vars: project development variables',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'aedev_aedev',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
        'docs': [],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [
        'packaging',
        'setuptools',
        'ae_base',
        'ae_paths',
        'ae_core',
        'ae_shell',
        'ae_managed_files',
        'aedev_base',
        'aedev_commands',
    ],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'aedev_project_vars',
    'package_data': {
        '': [],
    },
    'packages': [
        'aedev',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_project_vars/-/issues',
        'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.project_vars.html',
        'Repository': 'https://gitlab.com/aedev-group/aedev_project_vars',
        'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/project_vars.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/aedev-group/aedev_project_vars',
    'version': '0.3.16',
    'zip_safe': True,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    ...
