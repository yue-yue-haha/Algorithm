#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/6/2 10:52
# @File     : 面试题64. 求1+2+…+n.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def sumNums(self, n: int) -> int:
		return int((n ** 2 + n) / 2)
