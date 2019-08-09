# Raw Data Files

## NCAATourneyCompactResults.csv

This file identifies the game-by-game NCAA® tournament results for all seasons of historical data. The data is formatted exactly like the RegularSeasonCompactResults data. Note that these games also include the play-in games (which always occurred on day 134/135) for those years that had play-in games. Thus each season you will see between 63 and 67 games listed, depending on how many play-in games there were.

* DayNum=134 or 135 (Tue/Wed) - play-in games
* DayNum=136 or 137 (Thu/Fri) - Round 1
* DayNum=138 or 139 (Sat/Sun) - Round 2
* DayNum=143 or 144 (Thu/Fri) - Round 3, "Sweet Sixteen"
* DayNum=145 or 146 (Sat/Sun) - Round 4, "Elite Eight" or "Regional Finals"
* DayNum=152 (Sat) - Round 5, "Final Four"
* DayNum=154 (Mon) - Round 6, "National Championship"

## RegularSeasonDetailedResults.csv

This file provides team-level box scores for many regular seasons of historical data, starting with the 2003 season.

The column names should be self-explanatory to basketball fans (as above, "W" or "L" refers to the winning or losing team):

* WFGM - field goals made (by the winning team)
* WFGA - field goals attempted (by the winning team)
* WFGM3 - three pointers made (by the winning team)
* WFGA3 - three pointers attempted (by the winning team)
* WFTM - free throws made (by the winning team)
* WFTA - free throws attempted (by the winning team)
* WOR - offensive rebounds (pulled by the winning team)
* WDR - defensive rebounds (pulled by the winning team)
* WAst - assists (by the winning team)
* WTO - turnovers committed (by the winning team)
* WStl - steals (accomplished by the winning team)
* WBlk - blocks (accomplished by the winning team)
* WPF - personal fouls committed (by the winning team)