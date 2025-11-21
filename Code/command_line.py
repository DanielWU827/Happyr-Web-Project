'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''

import sys
from ProductionCode.category_helper import *
from ProductionCode.random_memory import get_random_memory
from ProductionCode.datasource import DataSource


'''
Print the Help statements
Tells users the possible command_line functions to access our database
'''
def help():
    usage = "Run python3 command_line.py --category to get the list of possible categories.\n"
    usage += "Run python3 command_line.py --random to get a random happy memory!\n"
    usage += "Run python3 command_line.py --category_name to get a story in that specific category.\n"
    usage += "Run python3 command_line.py --help to get help."
    print(usage)

'''
Parse the command line and deal with incorrectly entered information
Arguments: taken through commandline as strings. Normal use should be python3 command_line.py --FEATURE_NAME
Prints output based on feature selected
'''
def main():

    args = sys.argv[1:] # Please don't change [1:] :)
    if not args or len(args) > 1:
        help()
    else:
        ds = DataSource()
        categories = return_categories(ds)
        ds.connection.close()

        if args[0] == "--category":
            print(categories)

        elif args[0] == "--random":
            ds = DataSource()
            try:
                memory_text = get_random_memory(ds)
                print(memory_text if memory_text else "No memories found in the database.")
            finally:
                try:
                    ds.connection.close()
                except Exception:
                    pass

        elif args[0] == "--help":
            help()
        
        elif args[0][2:] in categories: #Suppose the input should be --category_name
            ds = DataSource()
            print(story_in_the_category(ds,args[0][2:]))
            ds.connection.close()

        else:
            print(f"Invalid Input: {args[0]}")
            help()


if __name__ == '__main__':
    main()
