#! /usr/bin/env python

# import sys, subprocess
# import my_seq
# from header_info import *

from __future__ import print_function
import sys, os, re

possible_chr = [str(x) for x in range(1, 23)] + ['X', 'Y'] + \
                   ["chr" + str(x) for x in range(1, 23)] + ['chrX', 'chrY']

def header_check(line):

    if "Chr_1" + '\t' + "Pos_1" + '\t' + "Dir_1" + '\t' + "Chr_2" + '\t' + "Pos_2" + '\t' + "Dir_2" + '\t' + "Inserted_Seq" + '\t' + "Variant_Type" in line:
        return True
    else:
        return False


def check_atypical_chromosomes(chr1, chr2):

    if chr1 not in possible_chr or chr2 not in possible_chr:
        return True 
    else:
        return False 


def compress_index_bed(inputFile, outputFile):

    ####################
    # compress by bgzip
    hOUT = open(outputFile, "w")
    subprocess.call(["bgzip", "-f", "-c", inputFile], stdout = hOUT)
    hOUT.close()
    ####################

    ####################
    # index by tabix
    subprocess.call(["tabix", "-p", "bed", outputFile])
    ####################


def sortBedpe(inputFile, outputFile):

    hOUT = open(outputFile, "w")
    subprocess.call(["sort", "-k1,1", "-k2,2n", "-k4,4", "-k5,5n", inputFile], stdout = hOUT)
    hOUT.close()

