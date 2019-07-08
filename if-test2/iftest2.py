#! /usr/bin/python3

#ipchk = '192.168.0.1'

ipchk = input('Input an IP address: ') # prompts for user input

#if ipchk:
    #print ('Looks like the IP address was set: ' + ipchk)
#else: # if input is not provided
    #print ('You did not provide input.')

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
    print('It looks like the IP address of the gateway was set: ' + ipchk + '.' + ' This is not recommended.')
elif ipchk: # if any data is provided
    print('It looks like the IP address was set: ' + ipchk)
else:
    print('You did not provide input.')
