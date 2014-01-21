# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2013 Caleb P. Burns
# originally from https://github.com/cpburnz/python-path-specification
#
"""
This module provides compatibility between Python 2 and 3. Hardly
anything is used by this project to constitute including `six`_.

.. _`six`: http://pythonhosted.org/six
"""

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)
