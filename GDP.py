import json
import csv
from turtle import color, width

#US GDP
with open('NY.GDP.MKTP.json') as json_data:
    gdp_data= json.load(json_data)
    gdp_data = gdp_data[1]
dates = []
values = []

#creating a list of dates and a list of values
for i in gdp_data:
    dates.append(i['date'])
    values.append(i['value'])
int_values_us = []
#same format as data for CH GDP
for x in values:
    int_values_us.append(float(x))

#CH GDP
with open('API_CHN_DS2_en_csv_v2_4670670.csv') as file:
    reader = csv.reader(file)
    data_ch = list(reader)

#creating list of dates and a list of values from specific row of CSV file
values_ch = data_ch[453][4:66]
int_values_ch =[]
for  x in values_ch:
    int_values_ch.append(float(x))
dates_ch = data_ch[4][4:66]

#GRAPHING
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import(AutoMinorLocator, MultipleLocator)
import numpy as np

#format as trillions
#lists of data set -- from low (1960) to high (2021)
year=dates[::-1]
int_values_us=int_values_us[::-1]


# US GDP from 1960 to 2021
#fig, ax = plt.subplots()
plt.bar(year,int_values_us,color ='blue', width=0.5)
plt.title('US GDP from 1960 to 2021')
plt.ylabel('US GDP (Current US $, in trillions)')
plt.xlabel('Year')
plt.xticks(rotation=50,fontsize =5, color='black')
#ax.xaxis.set_tick_params(labelrotation = -50, labelsize = 5, labelcolor = 'black', pad =2, width =0.25)
plt.yticks(fontsize = 7)
plt.yticks(np.arange(min(int_values_us),max(int_values_us)+1,1e12))
#plt.yaxis.set_minor_locator(AutoMinorLocator())
#ax.yaxis.set_tick_params(labelsize = 7)
plt.show()


# US and CH GDP from 1960 to 2021
int_values_ch = int_values_ch
fig, ax =plt.subplots()
ax.plot(year, int_values_us, color = 'blue', label = 'US GDP')
ax.plot(year, int_values_ch, color = 'red', label = 'China GDP')
ax.xaxis.set_tick_params(labelrotation = 50, labelsize = 4, labelcolor = 'black', pad =2)
#ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_tick_params(labelsize = 7)
plt.title('GDP in the US vs. China from 1960 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('GDP (Current US$, in trillions)')
plt.yticks(np.arange(min(int_values_ch),max(int_values_us)+1,step=1e12))
plt.legend(bbox_to_anchor=(1,1), loc='upper left', borderaxespad=0)
plt.show()