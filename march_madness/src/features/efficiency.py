def calc_shooting_efficiency(df):
    df['Wshoot_eff'] = df.apply(lambda row: row.WScore / (row.WFGA + 0.475 * row.WFTA), axis=1)
    df['Lshoot_eff'] = df.apply(lambda row: row.LScore / (row.LFGA + 0.475 * row.LFTA), axis=1)


def calc_scoring_opportunity(df):
    df['Wscore_op'] = df.apply(lambda row: (row.WFGA + 0.475 * row.WFTA) / row.Wposs, axis=1)
    df['Lscore_op'] = df.apply(lambda row: (row.LFGA + 0.475 * row.LFTA) / row.Lposs, axis=1)


def calc_offense_rating(df):
    df['Woff_rtg'] = df.apply(lambda row: row.WScore / row.Wposs * 100, axis=1)
    df['Loff_rtg'] = df.apply(lambda row: row.LScore / row.Lposs * 100, axis=1)


def calc_defense_rating(df):
    df['Wdef_rtg'] = df.apply(lambda row: row.Loff_rtg, axis=1)
    df['Ldef_rtg'] = df.apply(lambda row: row.Woff_rtg, axis=1)


def calc_net_efficiency(df):
    df['Wsos'] = df.apply(lambda row: row.Woff_rtg - row.Loff_rtg, axis=1)
    df['Lsos'] = df.apply(lambda row: row.Loff_rtg - row.Woff_rtg, axis=1)