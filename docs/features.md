# Basketball Stats as features

Box-score data are used to calculate basketball statistics. These are the features to analyze and possibly model.

# Possession

A team's possession ends when the team: 
1) makes a field goal 
2) misses and fails to get the rebound 
3) turns the ball over, or 
4) either makes the last free throw or does not get the rebound. (Or the period ends.) 

This can be estimated as:

poss= $$FGA−OR+TO+0.475FTA$$
 
In any game, the number of possessions is nearly equal for both teams, so efficiency wins!

# EFFICIENCY

## Shooting Efficiency

Number of points per shooting opportunity, estimated as:

shoot_eff = $\frac{Score}{FGA+0.475FTA}$

## Scoring Opportunity

Number of scoring attempts, estimated as:

score_op = $\frac{FGA+0.475FTA}{poss}$

## Offensive Rating

Points scored per 100 possessions, estimated as:

off_rtg=$\frac{Score}{poss}×100$

## Defensive Rating

A team's defensive rating is their opponent's offensive rating:

def_rtg=opp_off_rtg

## Net Efficiency

Sometimes also referred to as Strength of Schedule:

sos = off_rtg−opp_off_rtg

# More on shooting

## True Shooting Percentage

Similar to shooting efficiency but accounts for free throws, estimated as:

ts_pct= $\frac{Score}{2(FGA+0.475FTA)}×100$

## Effective Field Goal Percentage

Adjusts for the fact that some field goals are worth more points than others, estimated as:

efg_pct=$\frac{FGM2+1.5FGM3}{FGA}$

# REBOUNDING

## Offensive Rebound Percentage

orb_pct = $\frac{OR}{OR + opp_DR}$

## Defensive Rebound Percentage

drb_pct= $\frac{DR}{DR+opp_OR}$

## Rebound Percentage

reb_pct=$\frac{orb_pct+drb_pct}{2}$

# OLIVER'S FOUR FACTORS
http://www.basketballonpaper.com/author.html

Shoot, protect, recover, draw, frustrate! I know that's five; keep reading.

Basketball on Paper author Dean Oliver outlines four factors that determine success in basketball:

Effective Field Goal Percentage 

Turnovers per Possession
to_poss=$\frac{TO}{poss}$

Offensive Rebound Percentage 

Free Throw Rate
ft_rate=$\frac{FTM}{FGA}$

So, a team must shoot the ball well, take care of the ball (avoid turnovers), get back missed shots and get to the free throw line (and make them). But Oliver also stresses that these are important to both offense and defense. A team should cover the four factors, but should frustrate their opponent's efforts to do the same.

OTHER FEATURES TO CONSIDER -
From the NBA Advanced Stats page:

What is PACE? What does PACE tell fans besides the speed of the game?
Each team plays at a faster or slower pace, thus inflating or deflating player and team statistics. It is important to look at stats at a per possession level, rather than simply looking at points scored per game.

What is PIE?
It is a simple metric that gives an excellent indication of performance at both the team and player level. It’s a major improvement to our EFF Rating. Notably 2 things changed: (1) We included Personal Fouls, (2) We added a denominator. We feel the key here is the denominator because it acts as an "automatic equalizer". Using the denominator, we find there is no need to consider the "PACE" of the statistics that are being analyzed. In its simplest terms, PIE shows what % of game events did that player or team achieve. The stats being analyzed are your traditional basketball statistics (PTS, REB, AST, TOV, etc..) A team that achieves more than 50% is likely to be a winning team. A player that achieves more than 10% is likely to be better than the average player. A high PIE % is highly correlated to winning. In fact, a team’s PIE rating and a team’s winning percentage correlate at an R square of .908 which indicates a "strong" correlation. We’ve introduced this statistic because we feel it incorporates a bit of defense into the equation. When a team misses a shot, all 5 players on the other team’s PIE rating goes up.

## Team Impact Estimate

IE_numerator=Score+FGM+FTM−FGA−FTA+DR+0.5OR+Ast+Stl+0.5Blk−PF−TO
 
IE=$\frac{IE_numerator}{IE_numerator+opp_IE_numerator}$

## Assist Ratio

The percentage of a team's possessions that end in an assist:

ast_rtio=$\frac{Ast}{FGA+0.475FTA+TO+Ast}×100$

## Block Percentage

Indicates that a team blocked  n%
  of its opponents' shots:

blk_pct=$\frac{Blk}{opp_FGA2}×100$

## Steal Percentage

Indicates that the team stole the ball for  n%
  of its opponents' possessions:

stl_pct=$\frac{Stl}{opp_poss}×100$

## 3-Point Attempt Percentage

3pta_pct=$\frac{FGA3}{FGA}×100$