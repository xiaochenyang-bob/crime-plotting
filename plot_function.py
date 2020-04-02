import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
la = gpd.read_file('data/la-county-neighborhoods-v2/l.a. county neighborhood (v2).shp')
la['slug'] = la['slug'].astype(str)
la[la['slug'] == 'chatsworth']['slug'] = 'chatsworth-reservoir'


def plot_crime(crime, month):
    file_input = 'data/la_crimes/' + str(month) + '/' + crime + 'ByNeighborhood.csv'
    crimes = pd.read_csv(file_input)
    crimes['Neighborhood'] = crimes['Neighborhood'].astype(str)
    merged = la.merge(crimes, left_on='slug', right_on='Neighborhood', how='left')
    merged = merged.to_crs(epsg=3857)
    import contextily as ctx
    ax = merged.plot(column='Crime Amount', cmap='YlGn', figsize=(10, 10));
    ax.set_axis_off()
    ctx.add_basemap(ax)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0, tight=True)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    output_file = "/Users/bobyang/Desktop/crime_prediction/crime_la/" + str(month) + "/" + crime + ".png"
    plt.savefig(output_file)


import os
crime_list = ['theft', 'vehicle_theft', 'burglary', 'fraud', 'assault', 'vandalism', 'robbery', 'sexual_offenses']
parent_directory = "/Users/bobyang/Desktop/crime_prediction/crime_la"
for month in range(2,13):
    directory = str(month)
    os.mkdir(os.path.join(parent_directory, directory))
    for crime in crime_list:
        plot_crime(crime, month)