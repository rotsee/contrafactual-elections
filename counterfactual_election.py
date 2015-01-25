#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""This script will simulates possible election results for a Swedish
   municipality, using the modified Sainte-Laguë method, and partially
   known results
"""

from tests import MoveVoters

###############################
# SETTINGS ####################
###############################
cfg_seats = {
    'norr': 31,
    'syd': 30,
    'test': 5
}
cfg_results = {
    'syd': {
        'V': 2067,
        'S': 8586,
        'MP': 2246,
        'C': 2227,
        'FP': 1085,
        'KD': 919,
        'M': 8180,
        'SD': 2089,
        'FI': 401,
        'OVR': 204
    },
    'norr': {
        'V': 2037,
        'S': 9607,
        'MP': 1713,
        'C': 2227,
        'FP': 968,
        'KD': 1089,
        'M': 7915,
        'SD': 2163,
        'FI': 254,
        'OVR': 179
    }
}
cfg_blocks = {'alliansen': ['C', 'FP', 'KD', 'M'],
              'rodgrona': ['V', 'S', 'MP'],
              'sd': ['SD']}
"""{ ward: { party_1: votes, ... } }
"""
cfg_tests = [{
    "test_class": MoveVoters,  # Name of test class
    "params": {
        "numvoters": 226,
        "from": "norr",
        "to": "syd"
    }
}]
"""These are the tests to run aganist the results."""
###############################
# END OF SETTINGS #############
###############################


def main():
    for test_settings in cfg_tests:
        test = test_settings["test_class"](cfg_results,
                                           cfg_seats,
                                           blocks=cfg_blocks,
                                           params=test_settings["params"])
        test.run()


if __name__ == '__main__':
    main()
