#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from quicktag import quicktag

register = template.Library()

def output_dict(dic):
    return ', '.join(['%s=%s' % (key, value) for key, value in dic.items()])

def output_args(context, *args, **kwargs):
    output = ''
    if context:
        output += 'Context: %s' % output_dict(context)
    if args:
        output += 'Args: %s'  % ', '.join(args)
    if kwargs:
        output += 'Kwargs: %s' % output_dict(kwargs)
    return output

@register.tag
@quicktag()
def sampletag(*args, **kwargs):
    return output_args(None, *args, **kwargs)

@register.tag
@quicktag(takes_context=True)
def sampletag_withcontext(context, *args, **kwargs):
    return output_args(context.dicts[0], *args, **kwargs)
