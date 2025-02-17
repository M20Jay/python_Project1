import csv

import pandas as pd
import plotly
import plotly.io as pio
from matplotlib import pyplot as plt
#print(plt.style.available)

plt.style.use('fivethirtyeight')

ages_x=[25,26,27,28,29,30,31,32,33,34,35]

dev_y=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(ages_x,dev_y,color='#444444',linestyle='--', label ="All Devs")

py_dev_y=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(ages_x,py_dev_y,color='#5a7d9a',linewidth=3, label ='Python')

js_dev_y =[37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]
plt.plot(ages_x,js_dev_y,color='#adad3b',linewidth=3, label ='Java')


plt.xlabel("Ages")
plt.ylabel('Median Salary (USD')
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('plt.png')
plt.show()

# Matplotlib - plotting bar graphs
import numpy as np
from collections import Counter
from collections import Counter
x_indexes = np.arange(len(ages_x))
width= 0.25

ages_x=[25,26,27,28,29,30,31,32,33,34,35]

dev_y=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.bar(x_indexes-width,dev_y,width= width, color='#444444',linestyle='--', label ="All Devs")

# py_dev_y=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
# plt.bar(x_indexes,py_dev_y,width= width, color='#5a7d9a',linewidth=3, label ='Python')
#
# js_dev_y =[37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]
# plt.bar(x_indexes+width,js_dev_y,width= width,color='#adad3b',linewidth=3, label ='Java')


plt.xlabel("Ages")
plt.ylabel('Median Salary (USD')

plt.xticks(ticks=x_indexes,labels=ages_x)
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('plt.png')
plt.show()

# Importing Data to Pycharm
#with open('/Users/martinjames/Documents/Self-Research/Academic work 2024/Python Analysis/Data/data.csv') as csv_file:
    #csv_reader = csv.DictReader(csv_file)

df =pd.read_csv('/Users/martinjames/Documents/Self-Research/Academic work 2024/Python Analysis/Data/data.csv')
ids= df['Responder_id']
lang_responses =df['LanguagesWorkedWith']

language_counter= Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)
#plt.ylabel("Programming Languages")
plt.xlabel('Number of People who Use')
plt.title('Most Popular Languages')

plt.show()


print(plt.style.available)

# Plotting pie charts
plt.style.use('fivethirtyeight')
slices =[120,80,30,30]
labels = ['Sixty', 'Forty','Extra1','Extra 2']
colors =['#008fd5','#fc4f30', '#e5ae37','#6d904f']

plt.pie(slices, labels =labels, colors=colors,  wedgeprops={'edgecolor':'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()



# Pie chart example 2
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices_1 = [59219, 55466, 47544, 36443, 35917]
labels_1 = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode =[0,0,0,0.1,0]

plt.pie(slices_1, labels =labels_1,explode=explode,shadow=True,
        startangle=90,autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()

# Stack Plots
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f


# Line plots
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('/Users/martinjames/Documents/Self-Research/Academic work 2024/Python Analysis/Data/data (1).csv')
ages =data['Age']
dev_salaries=data['All_Devs']
py_salaries = ['Python']
js_salaries =data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
plt.plot(ages, js_salaries,label = 'Python')

overall_median = 57287

plt.fill_between(ages,dev_salaries, overall_median,
                 where=(dev_salaries>overall_median),
                 interpolate=True,alpha =0.25, label ='Above Average')

plt.fill_between(ages,dev_salaries, overall_median,
                 where=(dev_salaries<=overall_median),
                 interpolate=True,color ='red', alpha =0.25, label ='Below Media')

plt.legend()
plt.title('Median Salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD')

plt.tight_layout()
plt.show()


#
