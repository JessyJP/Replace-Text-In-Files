import text_replacement_file_processor  # replace this with the actual name of your module

# Define the command to be executed
command = []

command.append("")
command.append("-h")

# Replace the word 'Hello' with 'Hi' in all files
command.append(' -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in all files, but don't write the changes to the files
command.append(' -v -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in all files, print detailed output
command.append(' -d -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in file5.txt only
command.append(' -t Hello -s Hi -i test_dir/file5.txt')

# Replace multiple words in all files
command.append(' -t Hello test -s Hi exam -i test_dir')

# Execute the command
for cmd in command:
       text_replacement_file_processor.main(cmd.split())
