# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from django.template import Template, Context

def assert_render_equals(tag_code, expected, context=None):
    t = Template("{% load dummyapp_tags %}" + tag_code)
    content = t.render(Context(context or {}))
    assert_equals(content, expected)

