from sys import argv

scr, filename = argv

file = open(filename)

print ("File content:\n %s" % file.read())

file.close()

#w - truncates file, r+ open for read and write with no truncation
#binary mode avaliable, no decoding happens.
#buffering also avaliable
