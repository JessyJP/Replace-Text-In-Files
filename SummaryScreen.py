import random
import types
import Author_ASCII_art

def printSummaryScreen():
    # Get a list of all function names in the Author_ASCII_art module
    author_functions = [f for f in dir(Author_ASCII_art) if callable(getattr(Author_ASCII_art, f)) and not f.startswith("__")]
    
    # Select a random function name from the list
    function_name = random.choice(author_functions)

    # Get the function object associated with the string name
    printAuthor = getattr(Author_ASCII_art, function_name)

    # Call the function
    printAuthor()

    # # Test START ==============
    # for function_name  in author_functions:
    #     print(function_name)
    #     # Get the function object associated with the string name
    #     printAuthor = getattr(Author_ASCII_art, function_name)
    #     # Call the function
    #     printAuthor()
    # # Test END   ==============

    # Print App Name
    # printAppName()

    # Print Description
    print(r"""
    Summary:
        The Text Replacement File Processor is designed specifically to facilitate mass text replacement tasks. Whether for data cleaning, content 
        modification, or other text transformation needs, this tool provides a flexible and efficient solution. Its behavior can be extensively customized 
        through command-line arguments, making it a highly adaptable tool for a wide range of text replacement requirements.
    """)
#end

## ====================================== Software Application name ASCII art ======================================

def printAppName():
     print(r"""
 /$$$$$$$$                       /$$           /$$$$$$$                      /$$                                                                   /$$           /$$$$$$$$ /$$ /$$                 /$$$$$$$                                                                                 
|__  $$__/                      | $$          | $$__  $$                    | $$                                                                  | $$          | $$_____/|__/| $$                | $$__  $$                                                                                
   | $$     /$$$$$$  /$$   /$$ /$$$$$$        | $$  \ $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$        | $$       /$$| $$  /$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
   | $$    /$$__  $$|  $$ /$$/|_  $$_/        | $$$$$$$/ /$$__  $$ /$$__  $$| $$ |____  $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/        | $$$$$   | $$| $$ /$$__  $$      | $$$$$$$/ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$
   | $$   | $$$$$$$$ \  $$$$/   | $$          | $$__  $$| $$$$$$$$| $$  \ $$| $$  /$$$$$$$| $$      | $$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$          | $$__/   | $$| $$| $$$$$$$$      | $$____/ | $$  \__/| $$  \ $$| $$      | $$$$$$$$|  $$$$$$ |  $$$$$$ | $$  \ $$| $$  \__/
   | $$   | $$_____/  >$$  $$   | $$ /$$      | $$  \ $$| $$_____/| $$  | $$| $$ /$$__  $$| $$      | $$_____/| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$      | $$      | $$| $$| $$_____/      | $$      | $$      | $$  | $$| $$      | $$_____/ \____  $$ \____  $$| $$  | $$| $$      
   | $$   |  $$$$$$$ /$$/\  $$  |  $$$$/      | $$  | $$|  $$$$$$$| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$/      | $$      | $$| $$|  $$$$$$$      | $$      | $$      |  $$$$$$/|  $$$$$$$|  $$$$$$$ /$$$$$$$/ /$$$$$$$/|  $$$$$$/| $$      
   |__/    \_______/|__/  \__/   \___/        |__/  |__/ \_______/| $$____/ |__/ \_______/ \_______/ \_______/|__/ |__/ |__/ \_______/|__/  |__/   \___/        |__/      |__/|__/ \_______/      |__/      |__/       \______/  \_______/ \_______/|_______/ |_______/  \______/ |__/      
                                                                  | $$                                                                                                                                                                                                                      
                                                                  | $$                                                                                                                                                                                                                      
                                                                  |__/                                                                                                                                                                                                                      
""")
#end