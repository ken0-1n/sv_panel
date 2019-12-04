#! /usr/bin/env python

from __future__ import print_function
import sys, os, re, subprocess, gzip
import pysam
from .header_info import header_info
from .utils import header_check, sortBedpe, compress_index_bed
from .mergeFunction import organizeControl

def merge_control_main(args):


    # make directory for output if necessary
    if os.path.dirname(args.output_file) != "" and not os.path.exists(os.path.dirname(args.output_file)):
        os.makedirs(os.path.dirname(args.output_file))

    hout = open(args.output_file + ".temp", 'w')

    tumor_type_list = {}
    gene2type_sample = {}
    with open(args.result_list, 'r') as hin:
        for line in hin:

            label, tumor_type, result_file = line.rstrip('\n').split('\t')
            # label, result_file = line.rstrip('\n').split('\t')
            if tumor_type not in tumor_type_list: tumor_type_list[tumor_type] = 1

            if not os.path.exists(result_file):
                raise ValueError("file not exists: " + result_file)


            num = 1
            with open(result_file, 'r') as hin:
                for line in hin:
                    if line.startswith("#"): continue
                    if header_check(line.rstrip('\n')):
                        line = line.rstrip('\n')
                        header_info.read(line)
                        continue

                    F = line.rstrip('\n').split('\t')
                    inseq = F[header_info.inserted_seq] if F[header_info.inserted_seq] != "---" else ''

                    print('\t'.join([F[header_info.chr_1], str(int(F[header_info.pos_1]) - 1), F[header_info.pos_1], \
                                        F[header_info.chr_2], str(int(F[header_info.pos_2]) - 1), F[header_info.pos_2], \
                                        "junction_" + str(num),  inseq, \
                                        F[header_info.dir_1], F[header_info.dir_2], label, "1"]), file=hout)

                    num = num + 1

    hout.close()

    # utils.processingMessage("sorting the aggregated junction file")
    sortBedpe(args.output_file + ".temp", args.output_file + ".temp.sort")

    # utils.processingMessage("merging the same junction in the aggregated junction file")
    organizeControl(args.output_file + ".temp.sort", args.output_file + ".temp.merged", 20)

    # utils.processingMessage("sorting the merged junction file")
    sortBedpe(args.output_file + ".temp.merged", args.output_file + ".temp.merged.sort")

    # utils.processingMessage("compressing the merged junction file")
    compress_index_bed(args.output_file + ".temp.merged.sort", args.output_file)


    # remove intermediate files
    subprocess.check_call(["rm", "-rf", args.output_file + ".temp"])
    subprocess.check_call(["rm", "-rf", args.output_file + ".temp.sort"])
    subprocess.check_call(["rm", "-rf", args.output_file + ".temp.merged"])
    subprocess.check_call(["rm", "-rf", args.output_file + ".temp.merged.sort"])

