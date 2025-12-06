-- 9-cities_by_state_join.sql
-- List: cities.id - cities.name - states.name
-- Sorted by cities.id (ascending). Uses one SELECT.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
