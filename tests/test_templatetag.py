# -*- coding: utf-8 -*-

from mox import Mox

from tests import assert_render_equals

import quicktag

def test_tag_with_no_args_prints_nothing():
    yield assert_render_equals, "{% sampletag %}", ''

def test_tag_with_single_arg_prints_arg():
    yield assert_render_equals, "{% sampletag 'yo' %}", "Args: yo"

def test_tag_with_multiple_args_prints_arg_list():
    yield assert_render_equals, "{% sampletag 'yo','hey' %}", "Args: yo, hey"
    # Vary spacing around comma
    yield assert_render_equals, "{% sampletag 'yo', 'hey' %}", "Args: yo, hey"
    yield assert_render_equals, "{% sampletag 'yo' ,'hey' %}", "Args: yo, hey"
    yield assert_render_equals, "{% sampletag 'yo' , 'hey' %}", "Args: yo, hey"

def test_tag_with_single_kwarg_prints_keyword_and_value():
    yield assert_render_equals, "{% sampletag kw1='yo' %}", "Kwargs: kw1=yo"

def test_tag_with_multiple_kwargs_prints_a_keyword_and_value_list():
    yield assert_render_equals, "{% sampletag kw1='yo',kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey"
    # Vary spacing around comma
    yield assert_render_equals, "{% sampletag kw1='yo', kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey"
    yield assert_render_equals, "{% sampletag kw1='yo' ,kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey"
    yield assert_render_equals, "{% sampletag kw1='yo' , kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey"

def test_tag_with_context_prints_keyword_and_value_list():
    yield assert_render_equals, "{% sampletag_withcontext %}", "Context: myvar=yo", {'myvar': 'yo'}

def test_tag_prints_filtered_arg():
    yield assert_render_equals, "{% sampletag 'yo'|upper %}", "Args: YO"

def test_tag_prints_filtered_kwarg():
    yield assert_render_equals, "{% sampletag kw1='yo'|upper %}", "Kwargs: kw1=YO"

def test_tag_prints_variable_arg():
    yield assert_render_equals, "{% sampletag myvar %}", "Args: yo", {'myvar': 'yo'}

def test_tag_prints_variable_kwarg():
    yield assert_render_equals, "{% sampletag kw1=myvar %}", "Kwargs: kw1=yo", {'myvar': 'yo'}

def test_tag_with_space_in_arg():
    yield assert_render_equals, "{% sampletag 'yo hey' %}", "Args: yo hey"

def test_tag_uses_parser():
    mox = Mox()

    token_mock = mox.CreateMockAnything()
    token_mock.split_contents().AndReturn(['tagname'])

    parser_mock = mox.CreateMockAnything()

    mox.StubOutWithMock(quicktag, 'Parser')
    quicktag.Parser('').AndReturn(parser_mock)
    parser_mock.parse()
    parser_mock.stack = mox.CreateMockAnything()
    parser_mock.stack.__iter__().AndReturn(iter([]))

    try:
        mox.ReplayAll()
        quicktag.parse_args(None, token_mock)
        mox.VerifyAll()
    finally:
        mox.UnsetStubs()

