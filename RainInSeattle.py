
import json


# import the data from the JSON file:
with open('precipitation.json') as precipitation_file:
    raw_prec_data = json.load(precipitation_file)
 
    
# The next steps should create a list with the precipitation of each month as one item:
monthly_precipitation = [0]*12

# The next step goes through all the items (each a dictionay) and then through each dictionary
# If the dictionary derives from Seattle, it is added to a list of  data from seattle
# The list "seattle" saves each measurement as one item
for recording in raw_prec_data:
    if recording["station"] == "GHCND:US1WAKG0038":
            complete_date = str(recording["date"])
            complete_date = complete_date.split("-")
            # month of measurement: moo
            moo = int(complete_date[1])
            #because the index is counted from 0 onwards, it needs to be moo-1 to find the corresponding item in the list:
            monthly_precipitation[moo - 1] = monthly_precipitation[moo - 1] + recording["value"]


# monthly_precipitation can now be saved in a json file:
with open('monthly_precipitation.json', 'w') as file_output:
    json.dump(monthly_precipitation, file_output)


# the precipitation of the whole year is just the sum of each month:
whole_year = sum(monthly_precipitation)


# relative precipitation is monthly_precipitation/whole_year:
relative_precipitation = [0]*12
# -> this list (as above 'month') will list the value for each month as one item, thus has 12 items

for month in range(len(monthly_precipitation)):
    monthly_amount = monthly_precipitation[month]
    monthly_relation = monthly_amount / whole_year 
    relative_precipitation[month] = relative_precipitation[month] + monthly_relation
    #range-command in the for-loop: this time the index can be the variable instead of the variable -1

# The last step creates a dictionary with everything calculated until now
    # yearly, monthly total and monthly relative precipitation
Seattle = {}
Seattle["total_precipitation_year"] = whole_year 
Seattle["total_monthly_precipitation"] = monthly_precipitation 
Seattle["relative_monthly_precipitation"] = relative_precipitation


#Now I want to run this code for each station

#First I create a dictionary and a list for each other station
Cincinnati = {}
cincinnati = []
Maui = {}
maui = []
San_Diego = {}
san_diego = []


import csv
#In the following step I create a dictionary with each station code as key and the station as corresponding value
city_dict = {}
with open("stations.csv") as station_list:
    basic_information = list(read("station_list"))
for station in basic_information:
    city_dict[station[2]] = station[0]

main_dict = {"Cincinnati" : {}, "Maui" : {}, "Seattle" : {}, "San Diego" : {}}

#Then I repeat the steps from above for each station
for recording in raw_prec_data:
    main_dict[ciy_dict[recording["station"]]["totalYearPrecipitation"]] += recording["value"]
    
   


for recording in raw_prec_data:
    ciy_dict[recording["station"]][3] = recording["value"]
