#!/usr/bin/env python3

import requests  # 3rd party URL lookup

# define the main function


def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'  # API URL
    date = input("\tinput a start date in format YYYY-MM-DD\n").strip()
    startdate = (f'start_date={date}')  # start date for data
    enddate = '&end_date=END_DATE'  # create a mechanism to utilize enddate


# replace this with our API key
    mykey = '&api_key=cZrQUSZ4i91XKxcRbczI3GxYt3Cxra3v5akRZjh7'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    # print(neojson)
    print("NEOs are being tracked: ", neojson["element_count"])

    print("The nearest objects' missed distance:")
    i = 0
    while i < neojson["element_count"]:
        try:
            print(neojson["near_earth_objects"][date][i]
                  ["close_approach_data"][0]["miss_distance"]["kilometers"], "km")
            i += 1
        except:
            break
        #     print(neojson["near_earth_objects"][date][i+1]
        #           ["close_approach_data"][0]["miss_distance"]["kilometers"], "km")
        #     i += 2
        # else:
        #     print(neojson["near_earth_objects"][date][i+2]
        #           ["close_approach_data"][0]["miss_distance"]["kilometers"], "km")
        #     i += 3
        # finally:
        #     print(neojson["near_earth_objects"][date][i+3]
        #           ["close_approach_data"][0]["miss_distance"]["kilometers"], "km")
        #     i += 4
        #     # break


# call main
main()
