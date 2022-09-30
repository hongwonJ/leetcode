# Write your MySQL query statement below

SELECT player_id, player_name, SUM(
    IF(Wimbledon = player_id, 1, 0)
    + IF(Fr_open = player_id, 1, 0)
    + IF(US_open = player_id, 1, 0)
    + IF(Au_open = player_id, 1, 0)
) AS grand_slams_count
FROM Players JOIN Championships
GROUP BY player_id
HAVING grand_slams_count != 0