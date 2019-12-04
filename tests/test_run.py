#! /usr/bin/env python

import unittest
import os, tempfile, shutil, filecmp
import sv_panel
import subprocess


class TestRun(unittest.TestCase):

    def setUp(self):
        self.parser = sv_panel.parser.create_parser()

    def test1(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_result_list = cur_dir + "/../data/merge_list.1.txt"
        output_file = tmp_dir+"/COLO829BL.out1.bedpe.gz"
        args = self.parser.parse_args(["merge_control", in_result_list, output_file])
        args.func(args)

        subprocess.check_call(["gunzip", output_file])
        output_file_pref, ext = os.path.splitext(output_file)
        answer_file = cur_dir + "/../data/output_merged_control.1.answer.bedpe"
        self.assertTrue(filecmp.cmp(output_file_pref, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)


    def test2(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_result_list = cur_dir + "/../data/merge_list.2.txt"
        output_file = tmp_dir+"/COLO829BL.out2.bedpe.gz"
        args = self.parser.parse_args(["merge_control", in_result_list, output_file])
        args.func(args)

        subprocess.check_call(["gunzip", output_file])
        output_file_pref, ext = os.path.splitext(output_file)
        answer_file = cur_dir + "/../data/output_merged_control.2.answer.bedpe"
        self.assertTrue(filecmp.cmp(output_file_pref, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)


    def test3(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_result_list = cur_dir + "/../data/merge_list.3.txt"
        output_file = tmp_dir+"/COLO829BL.out3.bedpe.gz"
        args = self.parser.parse_args(["merge_control", in_result_list, output_file])
        args.func(args)

        subprocess.check_call(["gunzip", output_file])
        output_file_pref, ext = os.path.splitext(output_file)
        answer_file = cur_dir + "/../data/output_merged_control.3.answer.bedpe"
        self.assertTrue(filecmp.cmp(output_file_pref, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)


    def test4(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_result_list = cur_dir + "/../data/merge_list.4.txt"
        output_file = tmp_dir+"/COLO829BL.out4.bedpe.gz"
        args = self.parser.parse_args(["merge_control", in_result_list, output_file])
        args.func(args)

        subprocess.check_call(["gunzip", output_file])
        output_file_pref, ext = os.path.splitext(output_file)
        answer_file = cur_dir + "/../data/output_merged_control.4.answer.bedpe"
        self.assertTrue(filecmp.cmp(output_file_pref, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)


    def test5(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_result_list = cur_dir + "/../data/merge_list.5.txt"
        output_file = tmp_dir+"/COLO829BL.out5.bedpe.gz"
        args = self.parser.parse_args(["merge_control", in_result_list, output_file])
        args.func(args)

        subprocess.check_call(["gunzip", output_file])
        output_file_pref, ext = os.path.splitext(output_file)
        answer_file = cur_dir + "/../data/output_merged_control.5.answer.bedpe"
        self.assertTrue(filecmp.cmp(output_file_pref, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)
        
        
    def test11(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()
        in_control = cur_dir + "/../data/COLO829BL.out11.bedpe.gz"
        output_file = tmp_dir+"/COLO829BL.out11.txt"
        args = self.parser.parse_args(["convert_control", in_control, output_file])
        args.func(args)
        
        answer_file = cur_dir + "/../data/COLO829BL.out11.txt"
        self.assertTrue(filecmp.cmp(output_file, answer_file, shallow=False))
        shutil.rmtree(tmp_dir)
