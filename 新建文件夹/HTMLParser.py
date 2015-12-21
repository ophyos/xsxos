#!/usr/bin/python
""" This work is part of the CHTML project. EYX """

import codecs
def lex(line):
	return True;
	


if __name__ == "__main__":
	f = codecs.open("chtml.def", "r", "utf-8")
	print "________________________________"
	for i in range(6):
		f.xreadlines()
		
	for line in f.xreadlines():
#		print "Line:", line
		if len(line)>0:
			tmp = line.split('</ ')
			if len(tmp) and len(tmp[0])>1:
				print "->"
				for i in tmp:
					print "|", i,

