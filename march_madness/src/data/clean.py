from data import *


def drop_location(df):
    return df.drop(['WLoc'])


def drop_num_ot(df):
    return df.drop(['NumOT'])


def merge_team_with_conference_with_season_results(df):
    df_team_conferences = get_teams_conferences_as_df()
    df_teams = get_teams_as_df()
    df_conferences = get_conferences_as_df()

    # Merge the conference dataframes to eventually use the full conference name:
    df_conference_names = df_team_conferences.merge(df_conferences, on=['ConfAbbrev'])

    # Pre-merge tidying to match with winner and loser IDs:
    win_teams = df_teams.rename(columns={'TeamID': 'WTeamID'})[['WTeamID', 'TeamName']]
    win_confs = df_conference_names.rename(columns={'TeamID': 'WTeamID'})[['Season', 'WTeamID', 'Description']]
    lose_teams = df_teams.rename(columns={'TeamID': 'LTeamID'})[['LTeamID', 'TeamName']]
    lose_confs = df_conference_names.rename(columns={'TeamID': 'LTeamID'})[['Season', 'LTeamID', 'Description']]

    # Merge winning team name and conference, losing team name and conference with season results:
    return df.merge(win_teams, on='WTeamID').rename(columns={'TeamName': 'WTeamName'}) \
        .merge(win_confs, on=['Season', 'WTeamID']).rename(columns={'Description': 'WConfName'}) \
        .merge(lose_teams, on='LTeamID').rename(columns={'TeamName': 'LTeamName'}) \
        .merge(lose_confs, on=['Season', 'LTeamID']).rename(columns={'Description': 'LConfName'})


def calc_two_point_shot_stats(df):
    df['WFGM2'] = df.WFGM - df.WFGM3
    df['WFGA2'] = df.WFGA - df.WFGA3
    df['LFGM2'] = df.LFGM - df.LFGM3
    df['LFGA2'] = df.LFGA - df.LFGA3
