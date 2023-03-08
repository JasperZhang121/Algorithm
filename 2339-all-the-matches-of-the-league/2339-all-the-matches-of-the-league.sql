# Write your MySQL query statement below

SELECT t1.team_name AS home_team, t2.team_name AS away_team
FROM teams t1, teams t2

where t1.team_name!=t2.team_name;

