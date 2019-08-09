# def calc_effective_fg_percentage(df):


def calc_turnovers_per_posession(df):
    df['Wto_poss'] = df.apply(lambda row: row.WTO / row.Wposs, axis=1)
    df['Lto_poss'] = df.apply(lambda row: row.LTO / row.Lposs, axis=1)


# def calc_offsensive_rebound_percentage(df):


def calc_free_throw_rate(df):
    df['Wft_rate'] = df.apply(lambda row: row.WFTM / row.WFGA, axis=1)
    df['Lft_rate'] = df.apply(lambda row: row.LFTM / row.LFGA, axis=1)


def calc_four_factors(df):
    # Calculate weighted factors for winners and losers:
    df['Wfour'] = df.apply(lambda row: 0.4 * row.Wefg_pct + 0.25 * row.Wto_poss + 0.2 * row.Worb_pct + 0.15 * row.Wft_rate, axis=1)
    df['Lfour'] = df.apply(lambda row: 0.4 * row.Lefg_pct + 0.25 * row.Lto_poss + 0.2 * row.Lorb_pct + 0.15 * row.Lft_rate, axis=1)
