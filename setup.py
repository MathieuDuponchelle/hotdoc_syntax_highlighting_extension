# -*- coding: utf-8 -*-
#
# Copyright © 2015,2016 Mathieu Duponchelle <mathieu.duponchelle@opencreed.com>
# Copyright © 2015,2016 Collabora Ltd
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

import os

from setuptools import setup, find_packages

SOURCE_DIR = os.path.abspath('./')
PRISM_DIR = os.path.join(SOURCE_DIR, 'hotdoc_syntax_highlighting_extension', 'prism')
PRISM_COMP_DIR = os.path.join(PRISM_DIR, 'components')

with open(os.path.join('hotdoc_syntax_highlighting_extension', 'VERSION.txt'), 'r') as _:
    VERSION = _.read().strip()

DIST_FILES = ['VERSION.txt', 'prism_autoloader_path_override.js']

for root, dirs, files in os.walk(PRISM_COMP_DIR):
    for f in files:
        path = os.path.join(root, f)
        path = os.path.relpath(path, 'hotdoc_syntax_highlighting_extension')
        DIST_FILES.append(path)

DIST_FILES.append(os.path.join(PRISM_DIR, 'plugins', 'autoloader', 'prism-autoloader.js'))
DIST_FILES.append(os.path.join(PRISM_DIR, 'LICENSE'))

setup(
    name = "hotdoc_syntax_highlighting_extension",
    version = VERSION,
    keywords = "syntax highlighting hotdoc",
    url='https://github.com/hotdoc/hotdoc_syntax_highlighting_extension',
    author_email = 'mathieu.duponchelle@opencreed.com',
    license = 'LGPLv2.1+',
    description = ("An extension for hotdoc using prism for syntax highlighting"),
    author = "Mathieu Duponchelle",
    packages = find_packages(),
    package_data = {'hotdoc_syntax_highlighting_extension': DIST_FILES},
    entry_points = {'hotdoc.extensions': 'get_extension_classes = hotdoc_syntax_highlighting_extension.syntax_extension:get_extension_classes'},
)
