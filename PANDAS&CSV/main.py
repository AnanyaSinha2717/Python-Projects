# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)
# ------------------------------------------------------------
# import csv

# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas

# data = pandas.read_csv("weather_data.csv")
# max_temp = data.temp.max()

# get data in columns
# print(data.condition)

# get data in rows
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# print((monday.temp[0]) * 9/5 + 32, 'F')

# create database from scratch
data_dict = {
    'students': ['Amy', 'Yo', 'Me'],
    'marks': [76, 89, 100]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)