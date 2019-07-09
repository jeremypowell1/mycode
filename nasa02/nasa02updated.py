#! /usr/bin/python3

import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=qLzmA3O1fFgAAezhhtwg1rrTsdM34mLbNs60Qyi6'

    neourl = neourl + startdate + mykey
    neojson = (requests.get(neourl)).json()

    print(neojson)

main()
