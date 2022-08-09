
#Data set to merge the amount of IDPs per commune with the shape files.

#import the dataset for both the shape file of Burkina Faso and the IDP count in each month
nb = gpd.read_file('bfa_admbnda_adm3_igb_20200323.shp').set_index('ADM3_PCODE', drop=False)               #import shapefile
data = pd.read_csv('IDP_january_2020.csv',    sep =';')                     #import the data but skip the first row, this does not contain info
data = pd.DataFrame(data)

print(nb.head())
print(data.head())
print(data.info())

#merg adm2 and adm3 column of both dataframes

nb["ad2ad3"] = nb["ADM2_FR"].astype(str) + nb["ADM3_FR"].astype(str)
data["ad2ad3"] = data["Provinces"].astype(str) + data['Communes'].astype(str)

print(nb.head())
print(data.head())

#change objects to floats
cols = ['Masculin Adultes','Féminin Adultes', 'Enfants de moins de 5 ans', 'Enfants de plus de 5 ans', 'Total Enfants', 'Total PDIs']
data[cols] = data[cols].apply(pd.to_numeric, errors='coerce')

#merge dataset
nb = nb.merge(data, on='ad2ad3')

#save new file as shape file.
nb.to_file('IDP_january_2020_round.shp', decoding = "Windows-1252" )
