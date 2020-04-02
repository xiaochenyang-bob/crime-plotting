import pickle
import pandas as pd
import os
neighborhoods = pd.read_csv('data/neighborhood_info.csv')


def crime_count(neighborhood, df_crime):
    neighborhood = df_crime.apply(lambda x: True if x['neighborhood'] == neighborhood else False, axis=1)
    return len(neighborhood[neighborhood == True].index)


neighborhoods_list = neighborhoods['neighborhood'].tolist()


#mouth is number 1 to 12, crime is the crime category
def generateCSV(month, crime):
    filename = "data/LA-month/df_la_" + str(month)
    df_la = pickle.load(open(filename, 'rb'))
    df_crime = df_la[df_la['new_category'] == crime]
    dict_crime = {neighborhood: crime_count(neighborhood, df_crime) for neighborhood in neighborhoods_list}
    df_crime_neighborhood = pd.DataFrame.from_dict(dict_crime, orient='index', columns=["Crime Amount"])
    df_crime_neighborhood.index.name = 'Neighborhood'
    outfile = "data/la_crimes/" + str(month) + "/" + crime + "ByNeighborhood.csv"
    df_crime_neighborhood.to_csv(outfile)

crime_list = ['theft', 'vehicle_theft', 'burglary', 'fraud', 'assault', 'vandalism', 'robbery', 'sexual_offenses']
parent_directory = "data/la_crimes"
for month in range(3,13):
    directory = str(month)
    os.mkdir(os.path.join(parent_directory, directory))
    for crime in crime_list:
        generateCSV(month, crime)

