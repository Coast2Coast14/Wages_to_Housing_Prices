#!/usr/bin/env python
# coding: utf-8

# In[69]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def wage_inc_percent(wages_2005, wages_2019):
    return (((wages_2019 / wages_2005) - 1) * 100)

def house_price_percent(house_price_2005, house_price_2019):
    return (((house_price_2019 / house_price_2005) - 1) * 100)

def ratio(wage_percent, house_percent):
    return (wage_percent / house_percent)

data = pd.read_excel(r'/Users/elijahwooten/Documents/Coding Project Excel Table.xlsx')
df = pd.DataFrame(data)

for key, value in df[['Median wages in 2005', 'Median wages in 2019']].iteritems():
    wage_percent = wage_inc_percent(df.iloc[:, 1], df.iloc[:, 2])
    wage_percent = [float(round(n, 2)) for n in wage_percent]

for key, value in df[['Housing Price Index in 2005', 'Housing Price Index in 2019']].iteritems():
    house_percent = house_price_percent(df.iloc[:, 3], df.iloc[:, 4])
    house_percent = [float(round(n, 2)) for n in house_percent]

numbers = []
for a, b in zip(wage_percent, house_percent):
    percents = a, b
    numbers.append(ratio(percents[0], percents[1]))
    new_nums = [abs(float(round(n, 2))) for n in numbers]

df.insert(3, 'Wage Percentages from 2005 to 2019', wage_percent)
df.insert(6, 'Housing Price Percentages from 2005 to 2019', house_percent)
df.insert(7, 'Wage Percentages to Housing Price Percentages', new_nums)

# Bar Chart of Wage Percentages from 2005 to 2019 by City
plt.figure(figsize = (15, 5))
plt.bar(df['City'], df['Wage Percentages from 2005 to 2019'])
plt.title('Wage Percentages from 2005 to 2019 by City')
plt.xticks(rotation = 90)
plt.show()

# Bar Chart of Housing Price Percentages from 2005 to 2019
plt.figure(figsize = (15, 5))
plt.bar(df['City'], df['Housing Price Percentages from 2005 to 2019'])
plt.title('Housing Price Percentages from 2005 to 2019 by City')
plt.xticks(rotation = 90)
plt.show()

# Bar Chart of Wage Percentages to Housing Price Percentages by City
plt.figure(figsize = (15, 5))
plt.bar(df['City'], df['Wage Percentages to Housing Price Percentages'], align = 'center')
plt.title('Wage Percentages to Housing Price Percentages by City')
plt.xticks(rotation = 90)
plt.show()


# In[65]:


# Works Cited:
# https://fred.stlouisfed.org
# https://www.deptofnumbers.com
# https://en.wikipedia.org

