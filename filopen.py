fileHandle = open('test.txt','w')
fileHandle.write ('This is a test\nreally,it is.')
fileHandle.close()


fileHandle = open('test.txt')
print(fileHandle.read())
fileHandle.close()