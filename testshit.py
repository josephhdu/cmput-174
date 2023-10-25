filename = 'data_1.txt'
filemode = 'r'
file = open(filename,filemode)
contents = file.read()
print(contents)
file.close()