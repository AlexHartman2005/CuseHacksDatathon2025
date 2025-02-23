import pandas as pd
import matplotlib.pyplot as plt


file1 = pd.read_csv('Parking_Violations_-_2023_-_Present.csv')

dates = list(file1.issued_date)

for index in range(0, len(dates)):
    item = dates[index]
    dates[index] = item[0:item.find(" ")]

yearonedates = []
for item in dates:
    if item.startswith('2023'):
        yearonedates.append(item)




first_third = 0
second_third = 0
last_third = 0

for item in yearonedates:
    if int(item[8:]) <= 10:
        first_third += 1
    elif int(item[8:]) <= 20:
        second_third += 1
    else: 
        last_third += 1

morelikely = round(((last_third-first_third) / first_third * 100), 2)


#graphing thirds
thirds = ['First Third', 'Second Third', 'Last Third']
countofthirds = [first_third, second_third, last_third]

fig, ax = plt.subplots()
bar_cotainer = ax.bar(thirds, countofthirds, color=['blue', 'orange', 'red'])
ax.set(ylabel='Count', title='Tickets Per Third Of Month', ylim = (0, 25000))
ax.bar_label(bar_cotainer, fmt='{:,.0f}')



first_half_of_month = 0
second_half_of_month = 0

for item in yearonedates:
    if int(item[8:]) <= 15:
        first_half_of_month += 1
    else:
        second_half_of_month += 1




# i used the matplotlib documentation for pie charts to base this code:
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

halves = 'First Half', 'Second Half'
countofhalves = [first_half_of_month, second_half_of_month]

fig, ax = plt.subplots()
ax.pie(countofhalves, labels=halves, autopct='%1.1f%%', colors=['blue', 'red'])
ax.set(title = 'Tickets by Half of Month')

#months

months = {"January" : 0, "Febuary" : 0, "March" : 0, "April" : 0, "May" : 0, "June" : 0, "July" : 0, "August" : 0, "September" : 0, "October" : 0, "November" : 0, "December" : 0}



for item in yearonedates:
    month_num = int(item.split("/")[1]) 
    month_name = list(months.keys())[month_num-1] 
    months[month_name] += 1 
##print(months)

plt.figure(figsize=(12,6))
plt.bar((list(months.keys())), (list(months.values())), color="blue")
plt.xticks(rotation=90, fontsize = 5)
plt.title("Number of Tickets per Month")
plt.xlabel("Month")
plt.ylabel("Number of tickets")


#halves of months
halvesmonths = {"First Half of January" : 0, "Second Half of January" : 0, 
                "First Half of Febuary" : 0, "Second Half of Febuary" : 0, 
                "First Half of March" : 0, "Second Half of March" : 0, 
                "First Half of April" : 0, "Scond Half of April" : 0, 
                "First Half of May" : 0, "Second Half of May" : 0, 
                "First Half of June" : 0, "Second Half of June" : 0,
                "First Half of July" : 0, "Second Half of July" : 0, 
                "First Half of August" : 0, "Second Half of August" : 0, 
                "First Half of September" : 0, "Second Half of September" : 0, 
                "First Half of October" : 0, "Second Half of October" : 0, 
                "First Half of November" : 0, "Second Half of November" : 0, 
                "First Half of December" : 0, "Second Half of December" : 0} 


for item in yearonedates:
    day_num = int(item.split("/")[2]) 
    month_num = int(item.split("/")[1])
    if day_num < 16:
        halfofmonth = list(halvesmonths.keys())[(month_num*2)-2] 
    else:
        halfofmonth = list(halvesmonths.keys())[(month_num*2)-1]
    halvesmonths[halfofmonth] += 1 


#print(halvesmonths)

blue_red_alternate = ["blue" if i % 2 == 0 else "red" for i in range(len((list(halvesmonths.keys()))))]


plt.figure(figsize=(12,6))
plt.bar((list(halvesmonths.keys())), (list(halvesmonths.values())), color=blue_red_alternate)
plt.xticks(rotation=90, fontsize = 4)
plt.title("Number of Tickets Per Half of Month")
plt.xlabel("Half of Month")
plt.ylabel("Number of tickets")


days = {}
for index in range(1, 32):
    k = range(0,32)[index]
    days[k] = 0

for item in yearonedates:
    day_num = int(item.split("/")[2])
    days[day_num] +=1

fig, ax = plt.subplots()
ax.plot((list(days.keys())), (list(days.values())))
ax.set(xlabel = 'Day Number', ylabel = 'Number of Tickets', title = 'Tickets By Day Number (Total)')



#dailyaverage


day_average = {}

for key,value in days.items():
    if key < 29:
        day_average[key] = value // 12
    elif key < 31:
        day_average[key] = value // 11
    else:
        day_average[key] = value // 7

dailyaverage = len(yearonedates) // 365

#again based on starter code from matplotlib documentation
#https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py

plt.figure()
x = day_average.keys()
y = day_average.values()
plt.stem(x, y, bottom = dailyaverage)
plt.xlabel('Day Number')
plt.ylabel('Number of Tickets')
plt.title('Deviation from Average Tickets per Day')
plt.show()


mostday = day_average[14]


print("You are " + str(morelikely) + "% to get ticketed in the last third of the month compared to the first")
print("There seems to be a general trend up as the month goes on, but this is only one year of data so the sample size isn't massive")
