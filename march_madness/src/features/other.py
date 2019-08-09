def calc_team_impact_estimate(df):
    # Impact Estimate -
    # First calculate the teams' overall statistical contribution (the numerator):
    Wie = df.apply(lambda row: row.WScore + row.WFGM + row.WFTM - row.WFGA - row.WFTA + row.WDR + (
                0.5 * row.WOR) + row.WAst + row.WStl + (0.5 * row.WBlk) - row.WPF - row.WTO, axis=1)
    Lie = df.apply(lambda row: row.LScore + row.LFGM + row.LFTM - row.LFGA - row.LFTA + row.LDR + (
                0.5 * row.LOR) + row.LAst + row.LStl + (0.5 * row.LBlk) - row.LPF - row.LTO, axis=1)

    # Then divide by the total game statistics (the denominator):
    df['Wie'] = Wie / (Wie + Lie) * 100
    df['Lie'] = Lie / (Lie + Wie) * 100


def calc_assist_ratio(df):
    df['Wast_rtio'] = df.apply(lambda row: row.WAst / (row.WFGA + 0.475 * row.WFTA + row.WTO + row.WAst) * 100, axis=1)
    df['Last_rtio'] = df.apply(lambda row: row.LAst / (row.LFGA + 0.475 * row.LFTA + row.LTO + row.LAst) * 100, axis=1)


def calc_block_percentage(df):
    df['Wblk_pct'] = df.apply(lambda row: row.WBlk / row.LFGA2 * 100, axis=1)
    df['Lblk_pct'] = df.apply(lambda row: row.LBlk / row.WFGA2 * 100, axis=1)


def calc_steal_percentage(df):
    df['Wstl_pct'] = df.apply(lambda row: row.WStl / row.Lposs * 100, axis=1)
    df['Lstl_pct'] = df.apply(lambda row: row.LStl / row.Wposs * 100, axis=1)


def calc_3_pt_attempt_percentage(df):
    df['W3pta_pct'] = df.apply(lambda row: row.WFGA3 / row.WFGA * 100, axis=1)
    df['L3pta_pct'] = df.apply(lambda row: row.LFGA3 / row.LFGA * 100, axis=1)
