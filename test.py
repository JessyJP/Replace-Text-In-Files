import text_replacement_file_processor  # replace this with the actual name of your module
import subprocess

script = "text_replacement_file_processor"

# Define the command to be executed
command = []

# command.append('')
# command.append('-h')

# Replace the word 'Hello' with 'Hi' in all files
command.append('-v -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in all files, but don't write the changes to the files
command.append('-v -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in all files, print detailed output
command.append('-v -d -t Hello -s Hi -i test_dir')

# Replace the word 'Hello' with 'Hi' in file5.txt only
command.append('-v -t Hello -s Hi -i test_dir/file5.txt')

# Replace multiple words in all files
command.append('-v t Hello test -s Hi exam -i test_dir')

subprocess.run("cls",shell=True)
# Execute the command
i = 0
for cmd in command:
       i+=1
       print("\n"+100*"="+f"\nSCRIPT CALL:{i}\n"+100*"=")
       arguments = cmd.split()
       text_replacement_file_processor.main(arguments)
#end
