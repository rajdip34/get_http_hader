#!/usr/bin/python2

import socket

# create new  object

s = socket.socket()

#set time out 

s.settimeout(2)

# now set terget

terget = 'securityhub.cf'

# for port 80

s.connect((terget,80))

# send the packet

s.send('HEAD /HTTP/1.1\nHost: ' + terget + '\n\n' )

print s.recv(1024)

# for closing the connection

s.close