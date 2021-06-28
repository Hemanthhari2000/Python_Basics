#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Dec 20 16:36:32 2020

@author: hemanth


Problem Statement:
	Consider that a number is represented as an array. You need to add a number 1 to it's ones place.
	The result array should be printed

	testcase:
		input:
			Enter Array Elements:  [1, 2, 3]
		output:
			[1, 2, 4]

	tip: assume that we just add 1 to a number which is given as an array.

Solution:
"""

def add_one(given_array):
	carry = 1
	result = [0]*len(given_array)
	for num in given_array[::-1]:
		sum = num + carry
		if sum == 10:
			carry = 1
		else:
			carry = 0
		result[given_array.index(num)] = sum % 10
	if carry == 1:
		result = [0]* (len(given_array) + 1)
		result[0] = 1

	return result

def main():
	array = list(map(int, input("Enter Array Elements:\t").split()))
	result_array = add_one(array)
	print(result_array)

main()