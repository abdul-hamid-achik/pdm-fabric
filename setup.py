
# -*- coding: utf-8 -*-
from setuptools import setup

import codecs

with codecs.open('README.md', encoding="utf-8") as fp:
    long_description = fp.read()
ENTRY_POINTS = {
    'pdm': [
        'pdm_fabric = pdm_fabric.main:reg_commands',
    ],
}

setup_kwargs = {
    'name': 'pdm-fabric',
    'version': '0.0.2',
    'description': 'pdm shortcuts for Fabric projects',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'Abdul Hamid <abdulachik@icloud.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sicksid/pdm-fabric',
    'packages': [
        'pdm_fabric',
    ],
    'package_data': {'': ['*']},
    'long_description_content_type': 'text/markdown',
    'python_requires': '>=3.7',
    'entry_points': ENTRY_POINTS,

}


setup(**setup_kwargs)
