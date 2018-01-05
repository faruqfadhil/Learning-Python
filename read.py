fo = open("readWrite.txt", "r+")
str = fo.read(2);
print "Read String is : ", str
# Close opend file
fo.close()