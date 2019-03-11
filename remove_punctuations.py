# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:15:46 2018

@author: Cynthia Khan
"""

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''


outFile = open('unpunctuated.txt', 'w')

with open('positive_train.txt', 'r') as f1:
    for row in f1:
        my_str = row
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        outFile.write(no_punct.strip() + ":1" + "\n")
        

#outFile2 = open('unpunctuated_negative.txt', 'w')

with open('unpunctuated_negative.txt', 'r') as f2:
    for row in f2:
        my_str = row
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        outFile.write(no_punct.strip() + ":-1" + "\n")
        
outFile.close()
       
outFile3 = open('test_remarks.txt', 'w')

with open('test.txt', 'r') as f3:
   for row in f3:
       my_str = row
       no_punct = ""
       for char in my_str:
          if char not in punctuations:
             no_punct = no_punct + char
       outFile3.write(no_punct.strip() + "\n")
       
outFile3.close()