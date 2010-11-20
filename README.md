# django-quicktag
> Easy templatetags for Django

Easily creates templatetags with flexible arguments and keyword arguments.

    {% write_your_tags with_variables|filters:"args", and="keywords" %}

## Features

* python-like syntax for arguments and keyword arguments
* expands variables and applies template filters
* boilerplate-free: write a function that returns a string and decorate
* configurable access to the template context

## Installation

    sudo pip install django-quicktag

## Simple Usage

    # myapp/templatetags/mytags.py
    from django import template
    from quicktag import quicktag

    register = template.Library()

    @register.tag
    @quicktag() # Don't forget parenthesis
    def tag_without_context(*args, **kwargs):
        ...

    @register.tag
    @quicktag(takes_context=True)
    def tag_with_context(context, *args, **kwargs):
        ...

## Sample templatetags

### Simple argument and simple rendering

Basic example that renders the current date in some format:

    # ...
    @register.tag
    @quicktag() # Don't forget parenthesis
    def quicktoday(date_format):
        """
        Example: {% quicktoday '%d/%m/%Y' %}
        """
        from datetime import date
        return date.today().strftime(date_format)

### Taking and changing context (no rendering)

Takes the template context and sets/updates new variables using keyword arguments.

    # ...
    @register.tag
    @quicktag(takes_context=True)
    def set_vars(context, **kwargs):
        """
        Example:
        {{ var1 }} / {{ var2 }}
        {% set_vars var1="modified var1",var2="modified var2" %}
        {{ var1 }} / {{ var2 }}
        """
        context.update(kwargs)
        return ''

### Rendering any HTML tag with attributes

Takes an HTML tag name and renders keyword arguments as attributes:

    # ...
    @register.tag
    @quicktag()
    def html_tag(tagname, **kwargs):
        """
        Example: {% html_tag "img",src="/media/logo.png",width="100" height="50" %}
        """
        return '<%s %s />' % (tagname, ['%s="%s"' k,v for k,v in kwargs.items()])

### Using render_to_string

Includes the template loader's first match from a list of possible templates:

    # ...
    @register.tag
    @quicktag(takes_context=True)
    def include_any(context, *template_list):
        """
        Example: {% include_any variable_template,"fallback_template.html" %}
        """
        return template.loader.render_to_string(template_list, context)

