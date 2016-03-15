#!/usr/bin/env python
#-*- coding:utf-8 -*-

# カレントディレクトリにあるファイルを文字列で返す
import os

def run(**args):

	print "[*] In dirlister modules."
	files = os.listdir(".")

	return str(files)

