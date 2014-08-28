# -*- coding: utf-8 -*-

__version__ = '0.6.1'

import re
from django import template
from django.utils.encoding import smart_str

from quicktag.parser import Parser

# Regular expression to find named arguments
# Matches param_name=variable param_name="value" param_name=obj.property
re_kw = re.compile('^([^="\']+)=(.+)')

class QuickTagNode(template.Node):
    """
    Generic node capable of resolving arguments and named arguments
    and passing them to a rendering function.

    The rendering function must return a string to be displayed
    (or an empty string) and can optionally take the context as
    first parameter.

    Sample tag::

        @register.tag(takes_context=True)
        @quick_tag
        def repeat(context, text, num=1):
            return str(text) * int(num)

    Sample usage::

        {% repeat 'quick',num=3 %}
    """
    def __init__(self, func, args, kwargs, takes_context):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.takes_context = takes_context

    def render(self, context):
        """
        Uses the rendering function with the parameters
        and renders the output.

        The parameter parsing is modified from the django
        url templatetag.
        """
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k,'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])

        # Inserts the context if the function accepts
        if self.takes_context:
            args.insert(0, context)

        return self.func(*args, **kwargs)

def parse_args(parser, token):
    """
    Parses arguments and keyword arguments from a templatetag.
    It's slightly modified from django's url tag.
    """

    # Get the template tag bits removing first bit (tag name)
    contents = ''.join(token.split_contents()[1:])
    # Initial arguments
    args = []
    kwargs = {}

    # Use parser to split contents
    arg_parser = Parser(contents)
    arg_parser.parse()

    # Compiles filters for each argument and separate
    # simple and keyword arguments apart
    for arg in arg_parser.stack:
        m = re_kw.match(arg)
        if m:
            kw, arg = m.group(1).strip(), m.group(2)
            kwargs[kw] = parser.compile_filter(arg)
        elif arg:
            args.append(parser.compile_filter(arg))

    # Return the parsed arguments
    return args, kwargs

def quicktag(takes_context=False):
    """
    Decorator to create templatetags capable of parsing arguments
    and keyword arguments.

    The rendering function may optionally take the template context
    and must return a string to render.
    """
    def _wrapper(func):
        """
        Wrapper for the decorator.
        """
        def _tag(parser, token):
            """
            The tag to be registered with `register.tag`.
            """
            # Get parsed args and return the template node
            args, kwargs = parse_args(parser, token)
            return QuickTagNode(func, args, kwargs, takes_context)
        # Copy metadata to the decorated function
        _tag.__name__ = func.__name__
        _tag.__doc__ = func.__doc__
        _tag.__dict__.update(func.__dict__)
        return _tag

    return _wrapper

