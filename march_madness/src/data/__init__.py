import pandas as pd


def get_tourney_compact_results_as_df():
    return pd.read_csv('../../data/raw/NCAATourneyCompactResults.csv')


def get_regular_season_detailed_results_as_df():
    return pd.read_csv('../../data/raw/RegularSeasonDetailedResults.csv')


def get_teams_as_df():
    return pd.read_csv('../../data/raw/Teams.csv')


def get_teams_conferences_as_df():
    return pd.read_csv('../../data/raw/TeamConferences.csv')


def get_conferences_as_df():
    return pd.read_csv('../../data/raw/Conferences.csv')


def get_current_tourney_teams():
    df_predict = pd.read_csv('../../data/raw/SampleSubmissionStage2.csv')
    grp1 = list(set(df_predict.apply(lambda row: row.ID.split('_')[1], axis=1)))
    grp2 = list(set(df_predict.apply(lambda row: row.ID.split('_')[2], axis=1)))
    return list(set(grp1 + grp2))
