#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <django-quicktag - Easily create templatetags that takes args and kwargs>
# Copyright (C) <2010>  Enrico Batista da Luz <rico.bl@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='django-quicktag',
    version='0.6.1',
    description='Easily create templatetags that takes args and kwargs',
    author=u'Enrico Batista da Luz',
    author_email='rico.bl@gmail.com',
    url='http://github.com/ricobl/django-quicktag/',
    packages=['quicktag'],
)

