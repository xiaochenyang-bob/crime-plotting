import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
#change the file here
crimes = pd.read_csv('data/la_crimes/4/burglaryByNeighborhood.csv')
la = gpd.read_file('data/la-county-neighborhoods-v2/l.a. county neighborhood (v2).shp')
crimes['Neighborhood'] = crimes['Neighborhood'].astype(str)
la['slug'] = la['slug'].astype(str)
#fix a different name
la[la['slug'] == 'chatsworth']['slug'] = 'chatsworth-reservoir'
merged = la.merge(crimes, left_on = 'slug', right_on = 'Neighborhood', how='left')
merged = merged.to_crs(epsg=3857)
import contextily as ctx
# la['coords'] = la['geometry'].apply(lambda x: x.representative_point().coords[:])
# la['coords'] = [coords[0] for coords in la['coords']]
ax = merged.plot(column='Crime Amount', cmap = 'YlGn', figsize=(10,10), edgecolor = "none", linewidth = 1, legend= True);
#emphasised block
encino = merged[merged.slug == 'encino']
encino.boundary.plot(ax = ax, edgecolor='red', linewidth = 3)
hyde_park = merged[merged.slug == 'hyde-park']
hyde_park.boundary.plot(ax = ax, edgecolor='purple', linewidth = 3)
# for idx, row in la.iterrows():
#     plt.annotate(s=row['slug'], xy=row['coords'], horizontalalignment='center', fontsize=5, fontweight="bold" )
ax.set_axis_off()
ctx.add_basemap(ax)
plt.gca().set_axis_off()
#plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(0,0, tight=True)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
#change the same of saved file here
plt.savefig("/Users/bobyang/Desktop/crime_prediction/final_graphs/4.png")
#plt.show()