from os import listdir
from os.path import isfile, join
import sys



from utility.user_input import get_user_int

def is_convertable(file=None):
    
    return True

def convert_files(files=None):

    return

specified_dir = sys.argv[1] if len(sys.argv) > 1 else '.'

# Print opening
print("Enter the compiled PDF number, or 0 to just convert\n")

# Gather files and get selection
files = [f for f in listdir(specified_dir) if isfile(join(specified_dir, f)) and is_convertable(f)]

for i in range(len(files)):
    print("[" + str(i + 1) + "] " + str(files[i]))
print()

option = get_user_int(lower=1, upper=len(files))

# Convert files
convert_files(files=files)

