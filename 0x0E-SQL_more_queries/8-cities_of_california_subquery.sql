--  lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California (but the id can be different)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
USE `hbtn_0d_usa`;

SELECT `cities.id`, `cities.name`
FROM `cities`
WHERE `cities.state_id` IN (
  SELECT `id` FROM `states` WHERE `name` = "California"
);

ORDER BY `cities.id` ASC;
