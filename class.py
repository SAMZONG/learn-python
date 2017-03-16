#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test class file'

__author__ = 'SAMZONG'

class Student(object):
	
	def __init__(self,name,score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print('%s: %s' % (self.name,self.score))


bart = Student('Bart Simpon',59)
lisa = Student('Lisa Simpon',87)

bart.print_score()
lisa.print_score()
