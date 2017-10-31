#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:14:31 2017

find-political-donors.py
function to implement data processing

@author: Miao YU
"""

import statistics
import math
import datetime

def find_political_donors(input_file, output_by_zip, output_by_date):
                    
    f = open(input_file,"r") 
    
    # Read file line by line
    my_list = []
    for line in f:
        my_list.append(line)
        
    # Convert to matrix
    my_matrix = []
    for line in my_list:
        my_matrix.append(line.split("|"))
        
    # Rmove items that OTHER_ID is not empty
    my_matrix_filtered = []
    for line in my_matrix:
        if len(line[15]) == 0:
            my_matrix_filtered.append(line)
            
    # Variables for precessing by zip
    # Here we use a list to keep the CMTE_ID
    recipient_list_zip = []
    zip_code_matrix = []
    amount_cube_by_zip = []
    medianvals_by_zip = []
    
    # Process data by zip and calculate median values
    for i in range(0, len(my_matrix_filtered)):    
        line = my_matrix_filtered[i]
        recipient = line[0]
        amount = int(line[14])
        amount_str = line[14]
        zip_code = line[10]
        amount_list_zip = []
        # Input checking
        if len(recipient) == 0 or len(amount_str) == 0:
            # Ignore and skip for empty CMTE_ID and TRANSACTION_AMT
            continue
        if len(zip_code) > 5:
            # Only consider the first five characters
            zip_code = zip_code[0:5]    
        if len(zip_code) < 5:
            # Ignore and skip for calculating medianvals_by_zip.txt
            continue        
        # Add entry
        if recipient in recipient_list_zip:
            # If recipient already in list
            index_recipient = recipient_list_zip.index(recipient)
            zip_code_list = zip_code_matrix[index_recipient]
            # zip code related processing
            if zip_code in zip_code_list:                    
                # If recipient received donation from that zip code before            
                index_zip_code = zip_code_list.index(zip_code)
                amount_cube_by_zip[index_recipient][index_zip_code].append(amount)
                amount_list_zip = amount_cube_by_zip[index_recipient][index_zip_code]
            else:
                # Recipient not receive donation from that zip code yet
                zip_code_matrix[index_recipient].append(zip_code)
                amount_list_zip = [amount]
                amount_cube_by_zip[index_recipient].append(amount_list_zip)
        else:
            # Recipient not in list yet
            recipient_list_zip.append(recipient)
            index_recipient = len(recipient)-1
            zip_code_matrix.append([zip_code])
            amount_list_zip = [amount]
            amount_cube_by_zip.append([amount_list_zip])
        # Calculate median value
        median = math.ceil(statistics.median(amount_list_zip))
        total = sum(amount_list_zip)
        medianvals_by_zip.append([recipient,zip_code,str(median),\
                                  str(len(amount_list_zip)),str(total)])
      
    # Output medianvals_by_zip.txt     
    f = open(output_by_zip,"w") 
    for line in medianvals_by_zip:
        line_str = "|".join(line)
        f.write(line_str)
        f.write("\n")
    f.close()
        
    # Variables for precessing by date
    recipient_list_date = []
    date_matrix = []
    date_str_matrix = []
    amount_cube_by_date = []
    
    # Process data by date and calculate median values
    for i in range(0, len(my_matrix_filtered)):
        line = my_matrix_filtered[i]
        recipient = line[0]
        amount = int(line[14])
        amount_str = line[14]
        date_str = line[13]
        amount_list_date = []
        # Input checking
        if len(recipient) == 0 or len(amount_str) == 0:
            # Ignore and skip for empty CMTE_ID and TRANSACTION_AMT
            continue            
        if len(date_str) != 8:
            # Ignore and skip invalid date format for calculating medianvals_by_date.txt
            continue    
        date = datetime.datetime.strptime(date_str,"%m%d%Y")        
        # Add entry
        if recipient in recipient_list_date:
            # If recipient already in list
            index_recipient = recipient_list_date.index(recipient)
            date_list = date_matrix[index_recipient]
            # date related processing
            if date in date_list:
                index_date = date_list.index(date)
                amount_cube_by_date[index_recipient][index_date].append(amount)
            else:
                date_matrix[index_recipient].append(date)
                amount_cube_by_date[index_recipient].append([amount])
                date_str_matrix[index_recipient].append(date_str)
        else:
            # Recipient not in list yet
            recipient_list_date.append(recipient)
            index_recipient = len(recipient)-1
            amount_list_date = [amount]
            date_matrix.append([date])
            amount_cube_by_date.append([amount_list_date])
            date_str_matrix.append([date_str])
        
    # Output medianvals_by_date.txt
    medianvals_by_date = []
    recipient_list_sorted = [line for line in recipient_list_date]
    recipient_list_sorted.sort()
    for recipient in recipient_list_sorted:
        index_recipient = recipient_list_date.index(recipient)
        date_list = date_matrix[index_recipient]
        date_list_sorted = [line for line in date_matrix[index_recipient]]
        date_list_sorted.sort()
        for date in date_list_sorted:
            index_date = date_list.index(date)
            amount_list = amount_cube_by_date[index_recipient][index_date]
            median = math.ceil(statistics.median(amount_list))
            total = sum(amount_list)
            date_str = date_str_matrix[index_recipient][index_date]
            medianvals_by_date.append([recipient,date_str,str(median),\
                                  str(len(amount_list)),str(total)])            
    
    f = open(output_by_date,"w") 
    for line in medianvals_by_date:
        line_str = "|".join(line)
        f.write(line_str)
        f.write("\n")
    f.close()