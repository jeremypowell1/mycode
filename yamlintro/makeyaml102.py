#! /usr/bin/python3

import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arthur Dent", "species": "Human"}]

    ## display the python data (a list containing two dictionaries)
    print(hitchhikers)

    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)

main()
