import pandas as pd

# def remove_spaces(df,col) :
#     for i in range(df.shape[0]) :
#         if col[i][0] == ' ' :
#             col[i] = col[i][1:]
#     return df

def preprocess(df, region_df) :
    df = df.drop('ID', axis=1)
    df = df.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Unnamed: 0.2'], axis=1)
    # Medals given in 1906 Olympics is not considered by International Olympic Committee.
    df.drop(df[df.Year == 1906].index, inplace=True)
    # Extracting data related to summer olympics only
    df.Season = df.Season.replace(" Summer", "Summer")
    df = df[df.Season == "Summer"]
    # merging with region_df
    df = df.merge(region_df,
                  on="NOC",
                  how='left')
    # Deleting duplicated entries
    df.drop_duplicates(inplace=True)
    # Cleaning Medals column
    df.Medal = df.Medal.replace(" Bronze", "Bronze")
    df.Medal = df.Medal.replace(" Gold", "Gold")
    df.Medal = df.Medal.replace(" Silver", "Silver")
    df.Medal = df.Medal.replace([' OR', ' DQ', ' AC', 'NAFinal', ' WD', 'NA (lap 6)', 'NA (lap 5)',
                                 'NA (lap 3)', ' Disqualified in round twoMatch.',
                                 ' Disqualified in quarter-finalMatch.'], None)

    df = pd.concat([df, pd.get_dummies(df.Medal)], axis=1)

    return df