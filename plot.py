import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
crimes = pd.read_csv('data/crime1ByNeighborhood.csv')
chicago = gpd.read_file('data/geo_export_a4f39ffc-2b87-4410-bc02-19a95c82dbb2.shp')
#print(chicago["area_numbe"].head(2))
#we can plot a basic graph now
# chicago.plot()
# plt.show()
#merge two data sets
chicago['area_numbe'] = chicago['area_numbe'].astype(int)
crimes['NeighborhoodId'] = crimes['NeighborhoodId'].astype(int)
merged = chicago.merge(crimes, left_on = 'area_numbe', right_on = 'NeighborhoodId', how='left')
#try to label the neighborhood
chicago['coords'] = chicago['geometry'].apply(lambda x: x.representative_point().coords[:])
chicago['coords'] = [coords[0] for coords in chicago['coords']]
#add a background
merged = merged.to_crs(epsg=3857)
import contextily as ctx
#plot the graph
ax = merged.plot(column='Crime Amount', cmap = 'YlGn', figsize=(10,10));
for idx, row in chicago.iterrows():
    plt.annotate(s=row['community'], xy=row['coords'], horizontalalignment='center', fontsize=2, fontweight="bold" )
ax.set_axis_off()
ctx.add_basemap(ax)
#remove the white margin
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(0,0, tight=True)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig("/Users/bobyang/Desktop/crime_prediction/crime_by_district/robbery_chicago.png")
plt.show()
