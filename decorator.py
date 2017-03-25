#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def force_ascii_1(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@force_ascii_1
def fruit_wrap():
    return "Åpple"

print("with wrap: " + fruit_wrap())
