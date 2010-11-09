#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from quicktag import quicktag

register = template.Library()

@register.tag
@quicktag()
def testtag(*args, **kwargs):
    output = ''
    if args:
        output += 'Args: %s'  % ', '.join(args)
    return output

