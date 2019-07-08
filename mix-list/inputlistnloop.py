#! /usr/bin/env python3

def main():
    # Read in the list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: # single line from our file is sline
            # append add to the end of our list
            # rstrip remove any special characters to the right of the str
            # split breaks our string into a list
            # the results is we add a list of dirve and ip to networklists
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists) # display networklists to ensure we recreated

    for driveandip in networklists:
        print ('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
