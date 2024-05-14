# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temp=[]
#     for row in data:
#         if row[1]!='temp':
#             number=int(row[1])
#             temp.append(number)
#     print(temp)
import pandas
data=pandas.read_csv("weather_data.csv")
average_temp=data["temp"].mean()
max_temp=data["temp"].max()
# print(data[data.temp==max_temp])
monday=data[data.day=="Monday"]
print(monday)
print(type(monday))
x=monday.temp[0]
print(x)
temp_far=(x*9/5)+32
print(temp_far)

# import pandas
# data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# a=data["Primary Fur Color"].value_counts()
# print(a)
# print(type(a))
# df=pandas.DataFrame(a)
# x=df.to_csv("count.csv")