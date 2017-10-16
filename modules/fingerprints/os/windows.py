#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import re

class Windows:
	@staticmethod	
	def run(os):
		_ = False
		for item in os.items():
			_ = re.search(r'windows|win32',str(item),re.I) is not None
			if _:
				return "Windows"
				break