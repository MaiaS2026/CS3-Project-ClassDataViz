import pandas as pd
from matplotlib import pyplot as plt

# Set style theme
plt.style.use('seaborn-v0_8-deep')

# Read CSV into DataFrame
df = pd.read_csv('class-data-v1.csv')
df = df.head(8) # Limit to first 8 rows for our class

# Some cols need type converted (objecr -> datetime, boolean)
df['Birthdate'] = pd.to_datetime(df['Birthdate'])
df['Wakeup Time Weekday'] = pd.to_datetime(df['Wakeup Time Weekday'], format='%H:%M').dt.time
df['Wakeup Time Weekend'] = pd.to_datetime(df['Wakeup Time Weekend'], format='%H:%M').dt.time

# ZODIAC PIE CHART
zodiac_counts = df['Zodiac Element'].value_counts()
colors = ["#df3b3b","#3389df","#5f8e5f","#c4c4c4"]
plt.pie(zodiac_counts.values, labels=zodiac_counts.index, colors=colors, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
plt.title('Distribution of Zodiac Elements') 
plt.axis('equal')
plt.savefig('zodiac_element_pie.png', bbox_inches='tight')
plt.close()
