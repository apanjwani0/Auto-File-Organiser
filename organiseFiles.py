# Ptyhon program to organize files of a directory 
import os 
import sys 
import shutil 

# This function organizes contents of sourcePath into multiple 
# directories using the file types provided in extensionToDir 
def OrganizeDirectory(sourcePath, extensionToDir): 
	#print(type(sourcePath))
	print(sourcePath)
	if not os.path.exists(sourcePath): 
		print ("The source folder '" + sourcePath +
			"' does not exist!!\n") 
	else:
		for file in os.listdir(sourcePath): 
			file = os.path.join(sourcePath, file) 

			# Ignore if its a directory 
			if os.path.isdir(file): 
				continue

			filename, fileExtension = os.path.splitext(file) 
			fileExtension = fileExtension[1:] 
			#print(fileExtension,filename)
			# If the file extension is present in the mapping 
			if fileExtension in extensionToDir: 

				# Store the corresponding directory name 
				destinationName = extensionToDir[fileExtension] 
				destinationPath = os.path.join(sourcePath, destinationName) 
				#print(destinationName,destinationPath)
				# If the directory does not exist 
				if not os.path.exists(destinationPath): 
					print ("Creating new directory for `" + fileExtension +
						"` files, named - `" + destinationName + "'!!") 

					# Create a new directory 
					os.makedirs(destinationPath) 

				# Move the file 
				shutil.move(file, destinationPath) 

def main(directory,extensionToDir):
    # if len(sys.argv) != 2:
    #     print("Usage: <program> <source path directory>")
    #     return
    #print(os.getcwd())
    #sourcePath = sys.argv[1]
    #extensionToDir = {}
    #extensionToDir["pdf"] = "PDFs"
    #extensionToDir["jpg"] = "Images"
    #print(sourcePath)
    print("") 
    OrganizeDirectory(directory, extensionToDir)

def calledFromOther(directory,typeFolder):
	main(directory,typeFolder)

if __name__ == "__main__": 
	main() 
