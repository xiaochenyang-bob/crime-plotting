import pickle
import pandas as pd
df_chicago = pickle.load(open('data/8-crime-chicago-2015', 'rb'))
#df_chicago.to_csv (r'/Users/bobyang/Desktop/crime_prediction/chicago_dataframe.csv', index = False, header=True)
#filter rows for crime_type is one
df_crime1 = df_chicago[df_chicago['crime_type_id'] == 15]
#the total rows of crime1
#print(df_crime1.shape[0])
#print(len(df_crime1.index))
#count the amount of crime 1 happened in the first neighborhood
#neighborhood1 = df_crime1.apply(lambda x: True if x['neighborhood'] == 2 else False , axis=1)
#print(len(neighborhood1[neighborhood1 == True].index))

def crime1_count(id):
    neighborhood = df_crime1.apply(lambda x: True if x['neighborhood'] == id else False, axis=1)
    return len(neighborhood[neighborhood == True].index)


dict_crime1 = {id:crime1_count(id) for id in range(1,78)}
#Specify orient='index' to create the DataFrame using dictionary keys as rows
ids = [i for i in range(1,78)]
df_crime1_neighborhood = pd.DataFrame.from_dict(dict_crime1, orient='index', columns=["Crime Amount"])
df_crime1_neighborhood['NeighborhoodId'] = ids
#print(df_crime1_neighborhood)
df_crime1_neighborhood.to_csv(r'/Users/bobyang/PycharmProjects/draw_chicago/data/crime15ByNeighborhood.csv')