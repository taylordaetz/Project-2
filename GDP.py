import json
import csv

#US GDP
with open('NY.GDP.MKTP.json') as json_data:
    gdp_data= json.load(json_data)
    #print(gdp_data)
    print(type(gdp_data))
    print(type(gdp_data[1]))
    print(json.dumps(gdp_data[1], indent =2))
    gdp_data = gdp_data[1]
    #print(gdp_data)
dates = []
values = []
for i in gdp_data:
    dates.append(i['date'])
    values.append(i['value'])
print(dates)
#print(type(dates[1]))
#print(type(values[1]))
print(values)

#CH GDP
with open('API_CHN_DS2_en_csv_v2_4670670.csv') as file:
    reader = csv.reader(file)
    #print(type(reader))
    data_ch = list(reader)
    print(type(data_ch))

values_ch = data_ch[453][4:66]
values_ch = [int(i) for i in values_ch]
#values_ch = list(map(int,values_ch)) 
#values_ch = [int(i) for i in values_ch]
print(values_ch)
dates_ch = data_ch[4][4:66]
print(dates_ch)

#GRAPHING
import matplotlib.pyplot as plt
import numpy as np

dates=dates[::-1]
values=values[::-1]

plt.title('US GDP (Current US $) per Year')
plt.figure(1)
plt.ylabel('US GDP (Current US $)')
plt.xlabel('Year')
plt.xaxis
plt.bar(dates,values, linewidth=1.0)
fig, ax = plt.subplots()
plt.show()


dates_ch=dates_ch[::-1]
values_ch=values_ch[::-1]
plt.figure(2)
fig, ax = plt.subplots()
ax.bar(dates_ch, values_ch) 
plt.show()




#dictionary =dict(zip(dates,values))
#print(dictionary)

#accumulator for dates and value - create outside of the for loop
#for i in list:
# every item append i[dates] to dates 
#i['date']

#for loop to iterate through:
#   dates.append(i[date])
#   values.append(i[value])
#    accumulator.append(lab_dict[term])
#create a dictionary from two lists
