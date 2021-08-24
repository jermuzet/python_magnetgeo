#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
Provides tools to un/serialize data from json
"""

import json

import Shape
import ModelAxi
import Model3D
import Helix
import Ring
import InnerCurrentLead
import OuterCurrentLead
import Insert

# From : http://chimera.labs.oreilly.com/books/1230000000393/ch06.html#_discussion_95
# Dictionary mapping names to known classes

classes = {
    'Shape' : Shape,
    'ModelAxi' : ModelAxi,
    'Model3D' : Model3D,
    'Helix' : Helix,
    'Ring' : Ring,
    'InnerCurrentLead' : InnerCurrentLead,
    'OuterCurrentLead' : OuterCurrentLead,
    'Insert' : Insert
}

def serialize_instance(obj):
    """
    serialize_instance of an obj
    """
    d = {'__classname__' : type(obj).__name__}
    d.update(vars(obj))
    return d

def unserialize_object(d):
    """
    unserialize_instance of an obj
    """
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

