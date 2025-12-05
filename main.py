import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

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
colors = ["#63C5DA","#3389df","#2832C2","#48AAAD"]
plt.pie(zodiac_counts.values, labels=zodiac_counts.index, colors=colors, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
plt.title('Distribution of Zodiac Elements') 
plt.axis('equal')
plt.savefig('zodiac_element_pie.png', bbox_inches='tight')
plt.close()

# BAR CHART
hog_house = df['Hogwarts House'].value_counts()
colors = ["#7F0909","#194729","#222F5B","#000000","#ecb939"]
bars = plt.bar(hog_house.index, hog_house.values, color=colors[:len(hog_house)])
plt.xlabel('Hogwarts House')
plt.ylabel('Amount of students in house')
plt.savefig('hog_house_bar.png', bbox_inches='tight')

house_images = {
    "Gryffindor": "gryff.png",
    "Slytherin": "slyth.png",
    "Ravenclaw": "raven.png",
    "Hufflepuff": "huff.png",
    "the hat": "hat.webp"
}

for bar in bars:
    house = bar.get_x() + bar.get_width()/2 

    height = bar.get_height()             

    # Load image
    img = mpimg.imread(house_images[bar.get_x()]) 

    imagebox = OffsetImage(img, zoom=0.15)  
    ab = AnnotationBbox(imagebox, (house, height),
                        frameon=False,
                        xybox=(0, 20),      
                        xycoords='data',
                        boxcoords='offset points')

    plt.gca().add_artist(ab)

# Save figure
plt.savefig('hog_house_bar.png', bbox_inches='tight')
plt.show()




