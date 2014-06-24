# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 15:28:03 2014

@author: FCanesin
"""


def validatespec(spec, indict, name):
    """ Function to validate input dictionary from provided specification

        Parameters
        ----------
        spec: dict : specification dictionary, in the form {key:type}
        indict: dict : dictionary to validade agains specification
        name: string : name of dictonary to make errors more verbose
    """
    missing_key = "SPEC ERROR: Missing {0} key in {1} dict"
    wrong_type = "SPEC ERROR: {0} must be of {1}"
    for item in spec:
        if item not in indict:
            raise Exception(missing_key.format(item, name))
        keytype_fail = True
        if (type(spec[item]) is tuple) or (type(spec[item]) is list):
            for outcome in spec[item]:
                if type(indict[item]) is outcome:
                    keytype_fail = False
            if keytype_fail:
                raise Exception(wrong_type.format(item, spec[item]))
        else:
            if type(indict[item]) is not spec[item]:
                raise Exception(wrong_type.format(item, spec[item]))
