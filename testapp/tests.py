# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Template, Context

class SampleTagTest(TestCase):

    def assertRenderEquals(self, tag_code, expected):
        t = Template("{% load testapp_tags %}" + tag_code)
        content = t.render(Context({}))
        self.assertEquals(content, expected)

    def test_tag_with_no_args_prints_nothing(self):
        self.assertRenderEquals("{% testtag %}", '')

    def test_tag_with_single_arg_prints_arg(self):
        self.assertRenderEquals("{% testtag 'yo' %}", "Args: yo")

    def test_tag_with_multiple_args_prints_arg_list(self):
        self.assertRenderEquals("{% testtag 'yo' 'hey' %}", "Args: yo, hey")

