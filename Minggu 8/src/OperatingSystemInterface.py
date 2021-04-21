import os
import shutil
print(os.getcwd())      # Return the current working directory

os.chdir('/server/accesslogs')   # Change current working directory
print(os.system('mkdir today'))   # Run the command mkdir in the system shell

print(dir(os))

print(help(os))

print(shutil.copyfile('data.db', 'archive.db'))

print(shutil.move('/build/executables', 'installdir'))