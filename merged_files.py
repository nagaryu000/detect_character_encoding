# coding: utf-8

import csv
import chardet
import os
import sys

TARGET_FILES = os.listdir('.')
OUTPUT_FILE = 'output_files.txt'
CONTENT_LIST = []
WRITING_ENCODING = sys.argv[1]

for target_file in TARGET_FILES:
    if target_file.endswith('.py') or target_file == 'output_files.txt':
        pass
    else:
        with open(target_file, 'rb') as file:
            binary_file = file.read()
            detected_encoding = chardet.detect(binary_file)
            print(detected_encoding)
            write_encoding = detected_encoding['encoding']
            print(write_encoding)
            str_file = binary_file.decode(write_encoding)
            CONTENT_LIST.append(str_file)

with open(OUTPUT_FILE, 'w', encoding=WRITING_ENCODING) as file_out:
    for line in CONTENT_LIST:
        file_out.write(line)