import os
import re
import sys

def txt_file_reader(directory, regex_pattern):
    # Compile regex
    regex = re.compile(regex_pattern)
    
    try:
        # List files in given directory
        # folders = os.walk(directory)
        # print(folders, 'folders...')
        for file_name in os.listdir(directory):
            # check if file contains .txt and process if it does
            if file_name.endswith('.txt'):
                file_path = os.path.join(directory, file_name)

                # open file in read mode
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, 1):
                        # Check if regex matches the line
                        if regex.search(line):
                            match = f'{file_name}:{line_number}'
                        
                            # break
            print(match)        
    except (OSError, NotADirectoryError, Exception ):
        print(f'Error: Problem reading file!')
        

if __name__ == '__main__':
    # check the arguments passed during runtime
    if len(sys.argv) != 3:
        print("Usage: script.py <directory> <regex_pattern>")
        sys.exit(1)
    # Get first argument which should be the directory 
    directory = sys.argv[1]
    # Get second argument which should be the regex
    regex_pattern = sys.argv[2]
    
    txt_file_reader(directory, regex_pattern)
