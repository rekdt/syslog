from itertools import chain
import time
import os

paths = (
    "//nplqadb1/rman/qa10",
    "//nplqadb1/rman/qa10g",
    "//nplqadb1/rman/qa10ep",
    "//nplqadb1/rman/qa10sig",
    "//nplqadb1/rman/qapatch",
    "//nplpmsdb3/rma/des9i",
    "//tracker2/rman",
    "//Nplvault/rman",
    "//nplbuildsvr/rman"
)

#Declare the variables
search_str = "error" # Word to scan through the file
vardate = time.strftime("%Y_%m_%d") # Print todays date, i.e. 2014_12_02


#Searches directories, finds files, searches through file for a string that matches search_str
def DirectorySearch():
    err_val = False
    txtfile = open("Backup_Summary.txt", "w")
    for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths): # Go through each directory and subdirectory and find files
        for file in files: #For each file found
            if (file.startswith(vardate)) and (file.endswith("_Backup.log")): # If it starts with todays date and backup.log
                file = os.path.join(root, file) #Open the file, (I had to join the folder path with the file to get it to open)
                fileopened = open(file, 'r') #Open file as read only
                for line in fileopened: #Loop each line in the file
                    if search_str.lower() in line.lower(): #Search file with lowercase strings.
                        err_val = True
                        print "Error in file: " + file
                        txtfile.write("Error in file: " + file + "\n")
                fileopened.close() #Close file
    txtfile.close()
    if(err_val == False):
        txtfile = open("Backup_Summary.txt", "w")
        print vardate + " No Errors found"
        txtfile.write(vardate + " No Errors Found")
        txtfile.close()

DirectorySearch()
