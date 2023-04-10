# N-Gram Extractor

This program is a Python-based n-gram extractor for processing text data in Excel files. It analyzes input text, extracts n-grams (contiguous sequences of n words), and calculates the frequency of each n-gram. The results are then saved to an output Excel file containing the original data along with the most frequent n-gram and its frequency for each text entry. Additionally, a separate sheet in the output file lists all unique n-grams and their frequencies.

## Features
- Read input data from an Excel file
- Extract n-grams of variable length (2 to 5 words) from the text
- Calculate the frequency of each n-gram
- Save the results to an output Excel file
- Requires minimal user input and runs on Windows systems without Python installed
## Usage
- Ensure that the input file (输入数据.xlsx) is in the same directory as the executable.
- Run the executable (ngram_extractor.exe) by double-clicking it or running it from the command line.
- The program will process the input data and save the results to a new Excel file (输出结果.xlsx) in the same directory.
## Requirements
1. Python 3.6 or newer
2. pandas
3. openpyxl
Installation
To run the script directly, install the required packages using pip:

``pip install pandas openpyxl``

To package the script into a standalone executable for Windows, use pyinstaller:
``pip install pyinstaller``
``pyinstaller --onefile ngram_extractor.py``

The packaged executable will be located in the dist folder.

[Download package windows version](https://github.com/jellzone/ngram_extractor/releases/tag/windows)
