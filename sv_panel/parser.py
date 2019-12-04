#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ken0-1n
"""

import sys
import argparse
from .version import __version__
from .run import merge_control_main
from .run import convert_control_main

def create_parser():
    prog = "sv_panel"
    parser = argparse.ArgumentParser(prog = prog)
    parser.add_argument("--version", action = "version", version = prog + "-" + __version__)
    subparsers = parser.add_subparsers()
    
    def _create_merge_control_parser(subparsers):
        
        # merge control
        merge_control = subparsers.add_parser("merge_control", help = "Merge, compress and index the lists of GenomonSV results")
        merge_control.add_argument("result_list", metavar = "result_list.txt", default = None, type = str, help = "1st column: sample IDs, 2nd column: tumor type, 3rd column: genomon SV result path")
        merge_control.add_argument("output_file", metavar = "merge_control.bedpe.gz", default = None, type = str, help = "the path of the output file")
        return merge_control

    def _create_convert_control_parser(subparsers):
        
        # convert 
        convert_control = subparsers.add_parser("convert_control", help = "convert the output file of the merge control function to GenomonSV format")
        convert_control.add_argument("merged_control", metavar = "merge_control.bedpe.gz", default = None, type = str, help = "the output file of the merge control function")
        convert_control.add_argument("output_file", metavar = "result.txt", default = None, type = str, help = "the path of the output file")
        return convert_control

    merge_control = _create_merge_control_parser(subparsers)
    merge_control.set_defaults(func = merge_control_main)
    convert_control = _create_convert_control_parser(subparsers)
    convert_control.set_defaults(func = convert_control_main)
    return parser
