"""
Project Name: Text Replacement File Processor
Author: Your Name
Date: May 11, 2023
License: MIT License

Summary:
The Text Replacement File Processor is designed specifically to facilitate mass text replacement tasks. Whether for data cleaning, content 
modification, or other text transformation needs, this tool provides a flexible and efficient solution. Its behavior can be extensively customized 
through command-line arguments, making it a highly adaptable tool for a wide range of text replacement requirements.

Description:
This is a command-line tool designed for text replacement in multiple files or directories based on user-defined strings or regular expressions. 
The program accepts various command-line arguments that control its behavior, including whether to commit changes, verbosity of output, 
recursion through directories, and more. It is capable of identifying and ignoring binary files, focusing solely on the processing of text files.

MIT License:

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import sys
import os
import re
from tabulate import tabulate

# Color codes
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"


def is_binary(file_path):
    """
    Check if a file is binary.

    :param file_path: The path to the file to check.
    :return: True if the file is binary, False otherwise.
    """
    with open(file_path, 'rb') as file:
        CHUNKSIZE = 1024
        while True:
            chunk = file.read(CHUNKSIZE)
            if b'\0' in chunk:  # Check for null bytes
                return True
            #end
            if len(chunk) < CHUNKSIZE:
                break  # End of file
            #end
        #end
    #end
    return False
#end

def validate_input(args):
    """
    Validate the input arguments.

    :param args: The parsed command line arguments.
    """
    # Prepare the search strings
    search_types = args.text or args.extendedtext or args.regex

    # Prepare the replacement strings
    if len(args.substitute) == 1 and len(search_types) > 1:
        args.substitute = args.substitute * len(search_types)
    elif len(search_types) != len(args.substitute):
        print(f"{RED}Error: The number of search strings does not match the number of substitution strings.{RESET}")
        sys.exit(1)
    #end

    # Extra checks
    if args.regex and (args.normal or args.match_whole_word_only or args.match_case):
        print(f"{RED}Error: The -r option cannot be used with -n, -w, or -c.{RESET}")
        sys.exit(1)
    #end

    # Print the state of each input argument in green
    print(f"{CYAN}Input Arguments:{RESET}")
    print(f"{CYAN}Virtual: {GREEN}{args.virtual}{RESET}")
    print(f"{CYAN}Detail: {GREEN}{args.detail}{RESET}")
    print(f"{CYAN}Normal: {GREEN}{args.normal}{RESET}")
    print(f"{CYAN}Match whole word only: {GREEN}{args.match_whole_word_only}{RESET}")
    print(f"{CYAN}Match case: {GREEN}{args.match_case}{RESET}")
    print(f"{CYAN}Search strings: {GREEN}{search_types}{RESET}")
    print(f"{CYAN}Substitution strings: {GREEN}{args.substitute}{RESET}")
    # print(f"{CYAN}Input files/directories: {GREEN}{args.input_list}{RESET}")
    # print(f"{CYAN}Recursive OFF: {GREEN}{args.recursive_OFF}{RESET}")
    # print(f"{CYAN}Interactive mode ON: {GREEN}{args.interactive_mode_ON}{RESET}")

    # Print the search and substitution strings in a table like formatting
    # print(f"\n{BLUE}{'Search Strings':<20}{RESET}{MAGENTA}{'Substitution Strings':<20}{RESET}")
    # for search_str, subst_str in zip(search_types, args.substitute):
    #     print(f"{BLUE}{search_str:<20}{RESET}{MAGENTA}{subst_str:<20}{RESET}")

    # Prepare the data with no colours
    # data = [["Search Strings", "Substitution Strings"]] + list(zip(search_types, args.substitute))

    # Prepare the data
    header = [[f"{BLUE}Search Strings{RESET}", f"{MAGENTA}Substitution Strings{RESET}"]]
    data = [[f"{BLUE}{search_str}{RESET}", f"{MAGENTA}{subst_str}{RESET}"] for search_str, subst_str in zip(search_types, args.substitute)]
    data = header + data

    # Print the data as a table
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
#end

    # If the -d option is true, list the input strings
    # if args.detail:
    #     print(f"\n{GREEN}Input files/directories:{RESET}")
    #     for path in args.input_list:
    #         print(path)

def process_file(path, CTL):
    """
    Process a single file.

    :param path: The path of the file to process.
    :param CTL: The control structure containing parsed command line arguments.
    """
    # Load the file content
    try:
        with open(path, 'r') as file:
            content = file.readlines()
        #end
    except Exception as e:
        print(f"{RED}Error: Failed to read the file {path}. {e}{RESET}")  # Print in red
        return
    #end

    # Prepare the search and replacement strings
    search_types = CTL.text or CTL.extendedtext or CTL.regex
    replacements = dict(zip(search_types, CTL.substitute))

    # Prepare the search flags
    flags = 0
    if CTL.normal:
        flags |= re.IGNORECASE
    #end
    if CTL.match_whole_word_only:
        flags |= re.WORD
    #end

    # Initialize the replacement print buffer
    print_buffer = []

    # Perform the replacements and collect detailed info
    for i, line in enumerate(content):
        for search_str, subst_str in replacements.items():
            new_line, n = re.subn(search_str, subst_str, line, flags=flags)
            if n > 0:
                print_buffer.append(
                    f"Replace Lm:{i+1} Col:{line.find(search_str)+1} Pos:{line.find(search_str)+len(search_str)} "
                    f"full line with the [{search_str}] in green and full line with the replacement part in red[{subst_str}]"
                )
            #end
            content[i] = new_line
        #end
    #end

    # Print the detailed changes
    if CTL.detail:
        print(f"File substitutions [{len(print_buffer)}] in : {path}")
        for line in print_buffer:
            print(line)
        #end
    #end

    # Write the changes to the file
    if not CTL.virtual:
        try:
            with open(path, 'w') as file:
                file.writelines(content)
            #end
        except Exception as e:
            print(f"{RED}Error: Failed to write to the file {path}. {e}{RESET}")  # Print in red
        #end
    #end
#end

def process_inputfileOrDirectoryPath(path, CTL):
    """
    Process file or directory path.

    :param path: The path to process.
    :param CTL: The control structure containing parsed command line arguments.
    """
    # Check if path exists
    if not os.path.exists(path):
        print(f"{RED}Error: The path {path} does not exist.{RESET}")  # Print in red
        sys.exit(1)
    #end

    # Check if path is a file or a directory
    if os.path.isfile(path):
        # Check if file is binary
        if is_binary(path):
            if CTL.detail:
                print(f"The file {path} is binary and will be ignored.")
            #end
            return
        else:
            process_file(path, CTL)
        #end
    elif os.path.isdir(path):
        # If recursive-OFF is not set, process directory recursively
        if not CTL.recursive_OFF:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if not is_binary(file_path):
                        process_file(file_path, CTL)
                    #end
                #end
            #end
        #end
    #end
#end

def main(args):
    parser = argparse.ArgumentParser()

    # -v, --virtual: If set, changes are not committed to files after processing.
    parser.add_argument("-v", "--virtual", action="store_true", help="Do not commit changes to files after processing.")
    # -d, --detail: If set, verbose output is produced as files are processed.
    parser.add_argument("-d", "--detail", action="store_true", help="Produce verbose output when processing files.")

    # Search Tokens:
    # -n, --normal: If set, includes upper or lower case in any sequence of strings. This is set to TRUE by default.
    parser.add_argument("-n", "--normal", action="store_true", default=True, help="Include upper or lower case in any sequence of strings.")
    # -w, --match-whole_word_only: If set, matches any string of characters only in the appropriate case. This is set to FALSE by default.
    parser.add_argument("-w", "--match-whole_word_only", action="store_true", help="Match any string of characters only in the appropriate case.")
    # -c, --match-case: If set, -n is disabled. This is set to FALSE by default.
    parser.add_argument("-c", "--match-case", action="store_true", help="Disable -n if this is set.")

    # Search token options:
    # -t, --text: Accepts a list of text strings to search for.
    parser.add_argument("-t", "--text", nargs='+', help="List of text strings to search for.")
    # -e, --extendedtext: Accepts a list of text strings with extended characters to search for.
    parser.add_argument("-e", "--extendedtext", nargs='+', help="List of text strings with extended characters to search for.")
    # -r, --regex: Accepts a list of regular expressions to search for.
    parser.add_argument("-r", "--regex", nargs='+', help="List of regular expressions to search for.")

    # -s, --substitute: Accepts a list of replacement strings or file-paths.
    parser.add_argument("-s", "--substitute", nargs='+', help="List of replacement strings or file-paths.")

    # File Input:
    # -i, --input-list: Accepts a list of input files or directories.
    parser.add_argument("-i", "--input-list", nargs='+', help="List of input files or directories.")

    # --recursive-OFF: If set, processing will not be recursive.
    parser.add_argument("--recursive-OFF", action="store_true", help="Disable recursive processing.")
    # --interactive-mode-ON: If set, a special mode will be activated.
    parser.add_argument("--interactive-mode-ON", action="store_true", help="Activate special mode.")

    # Check if no arguments were provided
    if len(args)==0:
        parser.print_help(sys.stderr)
        from SummaryScreen import printSummaryScreen
        printSummaryScreen()
        sys.exit(1)
    #end

    CTL = parser.parse_args(args)

    # validate the input arguments
    validate_input(CTL)

    # loop over the input strings listed in the -i
    for path in CTL.input_list:
        process_inputfileOrDirectoryPath(path, CTL)
    #end
#end

# This allows the module to be runnable from the command line
if __name__ == "__main__":
    main(sys.argv[1:])
#end
