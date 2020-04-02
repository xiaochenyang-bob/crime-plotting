import pickle
import pandas as pd
#where you choose the mounth
df_la = pickle.load(open('data/LA-month/df_la_1', 'rb'))
neighborhoods = pd.read_csv('data/neighborhood_info.csv')
#where you define the crime category
df_crime = df_la[df_la['new_category'] == 'sexual_offenses']
def crime_count(neighborhood, df_crime):
    neighborhood = df_crime.apply(lambda x: True if x['neighborhood'] == neighborhood else False, axis=1)
    return len(neighborhood[neighborhood == True].index)
neighborhoods = neighborhoods['neighborhood'].tolist()
dict_crime = {neighborhood:crime_count(neighborhood, df_crime) for neighborhood in neighborhoods}
df_crime_neighborhood = pd.DataFrame.from_dict(dict_crime, orient='index', columns=["Crime Amount"])
df_crime_neighborhood.index.name = 'Neighborhood'
#change name of saved file
df_crime_neighborhood.to_csv(r'data/la_crimes/sexual_offensesByNeighborhood.csv')

