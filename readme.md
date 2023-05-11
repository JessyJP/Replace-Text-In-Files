# Text Replacement File Processor

Text Replacement File Processor is a command-line tool specifically designed for text replacement in multiple files or directories, based on user-defined strings or regular expressions. The tool provides a flexible and efficient solution for a wide range of text replacement requirements.

## Features
- Process multiple files or directories.
- Replace strings or regular expressions.
- Various command-line arguments to control its behavior.
- Capable of identifying and ignoring binary files.
- Option to commit or not commit changes to files after processing.
- Produce verbose output when processing files.
- Include upper or lower case in any sequence of strings.
- Match any string of characters only in the appropriate case.
- Disable matching any string of characters in any sequence if match-case is enabled.
- Accepts a list of text strings, text strings with extended characters, or regular expressions to search for.
- Accepts a list of replacement strings or file-paths.
- Accepts a list of input files or directories.
- Option to disable recursive processing.
- Activate a special interactive mode.

## Usage
To use the Text Replacement File Processor, you would run a command in your terminal similar to the following:

python text_replacement_file_processor.py -v -d -n -t hello world -s hello_world -i input.txt


This command will find instances of "hello" and "world" in the `input.txt` file and replace them with "hello_world". The `-v` flag indicates that changes should not be committed to the file after processing, and the `-d` flag indicates that verbose output should be produced.

To understand all the options and how to use them, use the `-h` or `--help` command:

python text_replacement_file_processor.py -h


## License
This project is licensed under the terms of the MIT License. See [LICENSE](LICENSE) for more details.
Remember to replace python text_replacement_file_processor.py with the actual command that should be used to run your script if it's different. Also, make sure to add more detailed usage instructions and examples if necessary.