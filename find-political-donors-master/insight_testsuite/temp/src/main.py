#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:34:22 2017

main.py
wrapper routine for find-political-donors.py
gather input and setting path

@author: Miao YU
"""

from find_political_donors import find_political_donors
import sys

# Read input from shell input
input_file = sys.argv[1]
output_by_zip = sys.argv[2]
output_by_date = sys.argv[3]

# Run function
find_political_donors(input_file, output_by_zip, output_by_date)