"""
Copyright: Copyright (c) 2019
License : WTFPL License
owner : pynickle
title : amazing-python study projects
description : projects for studying python
"""

from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
	if n < 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
	
for i in range(10):
	print(fibonacci(i))
