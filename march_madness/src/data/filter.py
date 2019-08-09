def limit_to_games_after_year(df, year):
    return df[df.Season > year]
