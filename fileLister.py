import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Create and/or truncate train.txt and test.txt
file_train = open('summary.txt', 'w')  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    file_train.write(current_dir + "/" + title + '.jpg' + "\n")
