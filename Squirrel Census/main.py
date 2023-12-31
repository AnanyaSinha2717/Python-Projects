import pandas
count = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
df = pandas.DataFrame(data_dict).to_csv("Squirrel_count.csv")
print(df)