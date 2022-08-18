Model predicting points:
- inputs:
  1. predicted xG
  2. predicted xA
  3. predicted CS
  4. predicted bps
- or:
  1. longer timeframe mean yellow cards
  2. longer timeframe mean red cards
  3. weighted average from last 100 days of xG, xA, BPS etc.
- one model for every position


Lineup evaluation model:
- projected points,
- flexibility:
  1. formation,
  2. popular price points,
  3. number of players from one club, e.g. 3xCity,
  4. funds spread over formations
  5. funds spread over players (e.g. 3xPremium)
- riskiness:
  1. average ownership,
  2. number of players from one club, e.g. 3xCity
  3. strength of the bench
  4. expected minutes of players


Player evaluation model:
- expected points,
- ownership,
- explosiveness,
- form,
- fixtures


Other ideas:
- calculating the biggest fixture swing
- one hot encoding for positions


Disclaimers:
Emerson appears twice in epl_players