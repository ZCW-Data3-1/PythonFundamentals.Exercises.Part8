import os

path = "/Users/dhannya/Projects"
path_to_file = 'file_in_dir.txt'
# we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        # append the file name to the list
        filelist.append(os.path.join(root, file))

# print all the file names
for name in filelist:
    print(name)

with open(path_to_file, 'w') as file:
    file.writelines(line+'\n' for line in filelist)
    print('Lines are written to file.')
