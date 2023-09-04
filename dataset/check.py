import os
# assign directory
directory = 'old_images'
sourcedir = 'old_labels'
destdir =   'old_checked'

# Crea la cartella di destinazione se non esiste già
if not os.path.exists(destdir):
    os.makedirs(destdir)
    
# iterate over files in
# that directory
for filename in os.listdir(directory):
    size = len(filename)
    name = filename[:size - 3]
    target = name + 'txt'
    print(target)
    for files in os.listdir(sourcedir):
        if target in files:
            src = sourcedir + '/' + target
            dest = destdir + '/' + target
            os.rename(src,dest)