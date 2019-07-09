#! /usr/bin/python3

import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arthur Dent", "species": "Human"}]

    ## display the python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open new file in write mode
    ## USAGE: yaml.dump (input data, file like object)
    zfile = open("galaxyguide.yaml", "w")

    yaml.dump(hitchhikers, zfile)

    zfile.close()

main()
