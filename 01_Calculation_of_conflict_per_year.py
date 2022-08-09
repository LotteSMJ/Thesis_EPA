#import the data set of all conflict events
data = pd.read_csv('AcledData.csv', delimiter = ';')

#find out which type of events are present in the data set
print(data['sub_event_type'].unique())
print(data.head())
print(data.columns)

#select the type of conflicts one wants to include
type_conflict = ['Abduction/forced disappearance', 'Armed clash', 'Attack',
 'Looting/property destruction', 'Remote explosive/landmine/IED', 'Shelling/artillery/missile attack', 'Grenade',
 'Non-state actor overtakes territory',    'Violent demonstration','Suicide bomb', 'Government regains territory']

data = data[data['sub_event_type'].isin(type_conflict)]

# create a seperate dataset for each year of the data set
df_2010 = data.loc[data['year'] == 2010]
df_2011 = data.loc[data['year'] == 2011]
df_2012 = data.loc[data['year'] == 2012]
df_2013 = data.loc[data['year'] == 2013]
df_2014 = data.loc[data['year'] == 2014]
df_2015 = data.loc[data['year'] == 2015]
df_2016 = data.loc[data['year'] == 2016]
df_2017 = data.loc[data['year'] == 2017]
df_2018 = data.loc[data['year'] == 2018]
df_2019 = data.loc[data['year'] == 2019]
df_2020 = data.loc[data['year'] == 2020]
df_2021 = data.loc[data['year'] == 2021]
df_2022 = data.loc[data['year'] == 2022]


print(data.info())

#save the dataset in each year in a seperate csv file.
path = r'C:\Users\lotte\PycharmProjects\conflict_per_year\calculated_eacht_year'
#funded.to_csv(path+'greenl.csv')
df_2010.to_csv(path+'df_2010.csv')
df_2011.to_csv(path+'df_2011.csv')
df_2012.to_csv(path+'df_2012.csv')
df_2013.to_csv(path+'df_2013.csv')
df_2014.to_csv(path+'df_2014.csv')
df_2015.to_csv(path+'df_2015.csv')
df_2016.to_csv(path+'df_2016.csv')
df_2017.to_csv(path+'df_2017.csv')
df_2018.to_csv(path+'df_2018.csv')
df_2019.to_csv(path+'df_2019.csv')
df_2020.to_csv(path+'df_2020.csv')
df_2021.to_csv(path+'df_2021.csv')
df_2022.to_csv(path+'df_2022.csv')