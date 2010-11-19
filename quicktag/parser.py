#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser(object):

    def __init__(self, contents):
        self.contents = contents
        self.buffer = ''
        self.stack = []
        self.inside_string = False
        self.quote_type = None

    def parse(self):
        self.previous_char = None
        for char in self.contents:
            self.read_char(char)
            self.previous_char = char
        self.push_stack()

    def push_stack(self):
        self.stack.append(self.buffer.strip())
        self.buffer = ''

    def read_char(self, char):
        if char in ["'", '"']:
            if self.inside_string:
                # Remove previous escape (\) if quote type is the same
                if self.quote_type == char and self.buffer[-1] == '\\':
                    self.buffer = self.buffer[:-1]
                self.inside_string = False
                self.quote_type = None
            else:
                self.inside_string = True
                self.quote_type = char
        elif not self.inside_string and char == ',':
            self.push_stack()
            return
        self.buffer += char

