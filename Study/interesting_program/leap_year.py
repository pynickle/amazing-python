"""
Copyright: Copyright (c) 2019
License : WTFPL License
owner : pynickle
title : amazing-python study projects
description : projects for studying python
"""

x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
	print(True)
else:
	print(False)
