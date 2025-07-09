import pandas as pd
import numpy as np
import os

# Get the folder where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Netflix_Dataset.csv')
df = pd.read_csv(file_path)

firt_5_rows = df.head()
all_columns = df.columns

Missing_Values = df.isnull().sum()
df =  df.drop_duplicates(keep='last')

Movies = df[df['type'] == 'Movie'] 
Tv_Shows = df[df['type'] == 'TV Show']
Tv_shows_longer_than_3_seasons = df[(df['type'] == 'TV Show') & (df['duration'] >= '3 Season')]

Indian_Movies = df[(df['type'] == 'Movie') & (df['country'] == 'India')].value_counts().sum()

released_after_2015 = df[df['release_year'] > 2015]


Comedy_Movies = df[df['listed_in'].str.contains('Comedies',na=False)].value_counts().sum()

Love_Movies = df[df['title'].str.contains('Love',na=False)]

Missing_Director_Names = df['director'].fillna('unknown',inplace=True)

Mode_Country = df['country'].mode()[0]
df['country'].fillna(Mode_Country,inplace=True)

df['is_recent'] = np.where(df['release_year'] >= 2020,True,False)
top_10_freq_genres = df['listed_in'].str.split(',').explode().value_counts().head(10)

top_5_most_feautres_directors = df['director'].value_counts().head(5)

movies_per_year = df[df['type'] == 'Movie']['release_year'].value_counts().sort_index()

country_dist = df['country'].value_counts().head(10)

recent = df[df['release_year'] >= 2020]
recent_genres = recent['listed_in'].str.split(',').explode().value_counts().head(10)

print("First 5 row :-",firt_5_rows)
print("All Columns Name:-",all_columns)
print("Data Types in each columns:-",df.dtypes)
print("Missing Values:-",Missing_Values)
print("Movies:-",len(Movies))
print("Tv shos longer than 3 seasons:-",Tv_shows_longer_than_3_seasons)
print("Indian Movies:-",Indian_Movies)
print("Released after 2015:-",released_after_2015)
print("Tv Shows:-",len(Tv_Shows))

print("Comedy Movies:-",Comedy_Movies)
print("Love Movies Count:-",len(Love_Movies))
print("Top 10 frequent genres:-",top_10_freq_genres)
print("Top 5 most featured directors:-",top_5_most_feautres_directors)
print("Movies Per year:-",movies_per_year)
print("Country Wise distribution:-",country_dist)
print("Recent Genres:-",recent_genres)


print("\n\nFinal:-",df)

df.to_csv('Cleaned_Netflix_Dataset.csv',index=False)
