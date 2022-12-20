import numpy as np

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years, country

def data_over_time(df,col):

    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
    nations_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
    return nations_over_time

def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    x = temp_df['Name'].value_counts().reset_index().head(15).merge(df, left_on='index', right_on='Name', how='left')[
        ['index', 'Name_x', 'Sport', 'region']].drop_duplicates('index')
    x.rename(columns={'index': 'Name', 'Name_x': 'Medals'}, inplace=True)
    return x

# def athletes_countries(df) :
#
#     # Number of athletes by country
#     athletes = df[['Name','Team']]
#     athletes_country = athletes.groupby('Team').count().reset_index()
#     athletes_country.columns = ['country', 'count']                    # Set the correct variables'names
#     athletes_country = athletes_country.sort_values('count', ascending = False)
#     athletes_country.country = athletes_country.country.replace("United States","United States of America")
#     athletes_country.country = athletes_country.country.replace("Great Britain","United Kingdom")
#     athletes_country.country = athletes_country.country.replace("Czechoslovakia","Czechia")
#     athletes_country.country = athletes_country.country.replace("West Germany","Germany")
#     athletes_country.country = athletes_country.country.replace("Soviet Union","Russia")
#
#     # geopandas
#     world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
#     athletes_country_final = world.merge(athletes_country, how = 'left', left_on=['name'], right_on=['country'])
#
#     return athletes_country_final
#
# def medals_countries(df) :
#     medal_country = fetch_medal_tally(df, "Overall", "Overall")
#     medal_country.region = medal_country.region.replace("USA","United States of America")
#     medal_country.region = medal_country.region.replace("UK","United Kingdom")
#
#     # # geopandas
#     world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
#     medals_country_final = world.merge(medal_country, how = 'left', left_on=['name'], right_on=['region'])
#     return medals_country_final

