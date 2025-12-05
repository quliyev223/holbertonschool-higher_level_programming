-- Script to list all cities of California
-- Using a subquery because JOIN is not allowed

-- 1. Subquery: select the id of the state named 'California'
--    This will return the unique id of California in the states table
-- 2. Outer query: select id and name from the cities table
--    Only for rows where state_id matches the id from the subquery
-- 3. Order the results by city id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (
SELECT id
FROM states
WHERE name = 'California'
)
ORDER BY id ASC;
