
import json


# import the data from the JSON file

with open('precipitation.json') as precipitation_file:
    raw_prec_data = json.load(precipitation_file)
    
# I want to create a dictionary including only the data for Seattle ("station" : "GHCND:USW00093814")

seattle = []


# The next step goes through all the items (each a dictionay) and then through each dictionary
# If the dictionary derives from Seattle, it is added to a list of  data from seattle
# The list "seattle" saves each measurement as one item

for recording in raw_prec_data:
    for key in recording.keys():
        if recording[key] == "GHCND:US1WAKG0038":
            seattle.append(recording)

# The next steps should create a list with the precipitation of each month as one item
monthly_precipitation = [0]*12

for measurement in seattle:
    complete_date = str(measurement["date"])
    complete_date = complete_date.split("-")
    # month of measurement: moo
    moo = int(complete_date[1])
    #because the index is counted from 0 onwards, it needs to be moo-1 to find the corresponding item in the list
    monthly_precipitation[moo - 1] = monthly_precipitation[moo - 1] + measurement["value"]
print(monthly_precipitation)
    

# monthly_precipitation can now be saved in a json file

with open('monthly_precipitation.json', 'w') as file_output:
    json.dump(monthly_precipitation, file_output)


