# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2013 Caleb P. Burns
# originally from https://github.com/cpburnz/python-path-specification
#
"""
The *pathspec* package provides pattern matching for file paths. So far
this only includes gitignore style pattern matching.

See "README.rst" or <https://github.com/cpburnz/python-path-specification> for
more information. Or you can always scour the source code.
"""

__author__ = "Caleb P. Burns"
__copyright__ = u"Copyright (c) 2013 Caleb P. Burns"
__created__ = "2013-10-12"
__email__ = "cpburnz@gmail.com"
__license__ = "MPL 2.0"
__project__ = "pathspec"
__status__ = "Development"
__updated__ = "2013-12-17"
__version__ = "0.3.0"

from .gitignore import GitIgnorePattern
from .pathspec import PathSpec
from .pattern import Pattern, RegexPattern
from .util import iter_tree, match_files, RecursionError
