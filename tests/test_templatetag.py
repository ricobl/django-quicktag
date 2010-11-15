# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from django.template import Template, Context

def assertRenderEquals(tag_code, expected, context=None):
    t = Template("{% load dummyapp_tags %}" + tag_code)
    content = t.render(Context(context or {}))
    assert_equals(content, expected)

def test_tag_with_no_args_prints_nothing():
    assertRenderEquals("{% sampletag %}", '')

def test_tag_with_single_arg_prints_arg():
    assertRenderEquals("{% sampletag 'yo' %}", "Args: yo")

def test_tag_with_multiple_args_prints_arg_list():
    assertRenderEquals("{% sampletag 'yo','hey' %}", "Args: yo, hey")
    # Vary spacing around comma
    assertRenderEquals("{% sampletag 'yo', 'hey' %}", "Args: yo, hey")
    assertRenderEquals("{% sampletag 'yo' ,'hey' %}", "Args: yo, hey")
    assertRenderEquals("{% sampletag 'yo' , 'hey' %}", "Args: yo, hey")

def test_tag_with_single_kwarg_prints_keyword_and_value():
    assertRenderEquals("{% sampletag kw1='yo' %}", "Kwargs: kw1=yo")

def test_tag_with_multiple_kwargs_prints_a_keyword_and_value_list():
    assertRenderEquals("{% sampletag kw1='yo',kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
    # Vary spacing around comma
    assertRenderEquals("{% sampletag kw1='yo', kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
    assertRenderEquals("{% sampletag kw1='yo' ,kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
    assertRenderEquals("{% sampletag kw1='yo' , kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")

def test_tag_with_context_prints_keyword_and_value_list():
    assertRenderEquals("{% sampletag_withcontext %}",
                            "Context: myvar=yo", context={'myvar': 'yo'})

def test_tag_prints_filtered_arg():
    assertRenderEquals("{% sampletag 'yo'|upper %}", "Args: YO")

def test_tag_prints_filtered_kwarg():
    assertRenderEquals("{% sampletag kw1='yo'|upper %}", "Kwargs: kw1=YO")

def test_tag_prints_variable_arg():
    assertRenderEquals("{% sampletag myvar %}", "Args: yo", context={'myvar': 'yo'})

def test_tag_prints_variable_kwarg():
    assertRenderEquals("{% sampletag kw1=myvar %}", "Kwargs: kw1=yo", context={'myvar': 'yo'})

def test_tag_with_space_in_arg():
    assertRenderEquals("{% sampletag 'yo hey' %}", "Args: yo hey")

