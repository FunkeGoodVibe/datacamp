-- https://app.datacamp.com/learn/courses/joining-data-in-sql



-- Return all cities with the same name as a country
SELECT name FROM cities
INTERSECT
SELECT name FROM countries

-- Return all cities that do not have the same name as a country
SELECT name FROM cities
EXCEPT 
SELECT name FROM countries 


-- Select fields with aliases
SELECT c.code as country_code, name, year, inflation_rate
FROM countries AS c
-- Join to economies (alias e)
JOIN economies AS e 
-- Match on code field using table aliases
ON c.code = e.code 

--vs 

SELECT c.name AS country, l.name AS language, official
FROM countries AS c
INNER JOIN languages AS l
-- Match using the code column
USING(code)





-- Select relevant fields
SELECT name, fertility_rate
FROM countries AS c
-- Inner join countries and populations, aliased, on code
INNER JOIN populations AS p
ON c.code = p.country_code



--Modify your query so that you are joining to economies on year as well as code. 
SELECT name, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code
-- Add an additional joining condition such that you are also joining on year
	AND p.year = e.year;




SELECT 
    c1.name AS city,
    code,
    c2.name AS country,
    region,
    city_proper_pop
FROM cities AS c1
-- Perform an inner join with cities as c1 and countries as c2 on country code
INNER JOIN countries c2 
ON c1.country_code = c2.code 
ORDER BY code DESC;




-- 
SELECT name, region, gdp_percapita
FROM countries AS c
LEFT JOIN economies AS e
-- Match on code fields
ON c.code = e.code 
-- Filter for the year 2010
WHERE year = 2010;




-- Modify this query to use RIGHT JOIN instead of LEFT JOIN
SELECT countries.name AS country, languages.name AS language, percent
FROM languages
RIGHT JOIN countries
USING(code)
ORDER BY language;


-- img of full join
-- https://assets.d-camp.com/production/repositories/6053/datasets/2122f52c767c4634f769c21488e03c912d04880f/full_join2.png
-- A FULL JOIN combines a LEFT JOIN and a RIGHT JOIN. 
-- As you can see in this diagram, no values are faded out as they were in earlier diagrams. 
-- This is because the FULL JOIN will return all ids, irrespective of whether they have a match in the other table being joined.


SELECT name AS country, code, region, basic_unit
FROM countries
-- Join to currencies
FULL JOIN currencies 
USING (code)
-- Where region is North America or name is null
WHERE region = 'North America' OR name is NULL
ORDER BY region;



-- Complete the FULL JOIN with countries as c1 on the left and languages as l on the right, using code to perform this join.
-- Next, chain this join with another FULL JOIN, placing currencies on the right, joining on code again.

SELECT 
	c1.name AS country, 
    region, 
    l.name AS language,
	basic_unit, 
    frac_unit
FROM countries as c1 
-- Full join with languages (alias as l)
FULL JOIN languages l 
  using(code)
-- Full join with currencies (alias as c2)
FULL JOIN currencies c2
  using(code)
WHERE region LIKE 'M%esia';




-- Complete the code to perform an INNER JOIN of countries AS c with languages AS l using the code field to obtain the languages currently spoken in the two countries.
SELECT c.name AS country, l.name AS language
-- Inner join countries as c with languages as l on code
FROM countries c 
INNER JOIN languages l
ON c.code = l.code 
WHERE c.code IN ('PAK','IND')
	AND l.code in ('PAK','IND');



--Complete the join of countries AS c with populations as p.
--Filter on the year 2010.
--Sort your results by life expectancy in ascending order.
--Limit the result to five countries.
SELECT 
	c.name AS country,
    region,
    life_expectancy AS life_exp
FROM countries AS c
-- Join to populations (alias as p) using an appropriate join
RIGHT JOIN populations p 
ON c.code = p.country_code
-- Filter for only results in the year 2010
WHERE p.year = '2010'
-- Sort by life_exp
ORDER BY p.life_expectancy
-- Limit to five records
LIMIT 5;




-- Comparing a country to itself 
-- Select aliased fields from populations as p1
SELECT p1.country_code, p1.size AS size2010, p2.size AS size2015
FROM populations p1
-- Join populations as p1 to itself, alias as p2, on country code
INNER JOIN populations p2 
ON p1.country_code = p2.country_code




-- Query that determines all pairs of code and year from economies and populations, without duplicates
SELECT code as country_code, year
FROM economies 
UNION 
SELECT country_code, year
FROM populations
ORDER BY country_code, year ASC



-- Comparing global economies (excluding duplicates!)
-- Select all fields from economies2015
SELECT *
FROM economies2015
-- Set operation
UNION
-- Select all fields from economies2019
SELECT *
FROM economies2019
ORDER BY code, year;



-- Return all cities with the same name as a country
SELECT name
FROM cities
INTERSECT
SELECT name
FROM countries



-- Return all cities that do not have the same name as a country
SELECT name
FROM cities
EXCEPT 
SELECT name
FROM countries 
ORDER BY name;





-- Select country code for countries in the Middle East
SELECT code
FROM countries
WHERE region = 'Middle East'


-- Select unique language names
SELECT DISTINCT(name)
FROM languages
-- Order by the name of the language
ORDER BY name ASC


SELECT code, name
FROM countries
WHERE continent = 'Oceania'
-- Filter for countries not included in the bracketed subquery
  AND code NOT IN
    (SELECT code
    FROM currencies);







-- Diagniosing a problem using ANTI JOIN 

"""
Nice work on semi joins! The anti join is a related and powerful joining tool. 
It can be particularly useful for identifying whether an incorrect number of records appears in a join.
Say you are interested in identifying currencies of Oceanian countries. 
You have written the following INNER JOIN, which returns 15 records. 
Now, you want to ensure that all Oceanian countries from the countries table are included in this result. 
You'll do this in the first step.

SELECT c1.code, name, basic_unit AS currency
FROM countries AS c1
INNER JOIN currencies AS c2
ON c1.code = c2.code
WHERE c1.continent = 'Oceania';
If there are any Oceanian countries excluded in this INNER JOIN, you want to return the names of these countries. You'll write an anti join to this in the second step!

1) 
Begin by writing a query to return the code and name (in order, not aliased) for all countries in the continent of Oceania from the countries table.
Observe the number of records returned and compare this with the provided INNER JOIN, which returns 15 records.

2) Now, build on your query to complete your anti join, by adding an additional filter to return every country 
   code that is not included in the currencies table.

"""


-- Select code and name of countries from Oceania
SELECT code, name
FROM countries
WHERE continent = 'Oceania'


SELECT code, name
FROM countries
WHERE continent = 'Oceania'
-- Filter for countries not included in the bracketed subquery
  AND code NOT IN
    (SELECT code
    FROM currencies);








-- Select average life_expectancy from the populations table
SELECT AVG(life_expectancy)
  FROM populations
-- Filter for the year 2015
WHERE year = '2015'


-- The answer from your query has now been nested into another query; 
-- use this calculation to filter populations for all records where life_expectancy is 1.15 times higher than average.
SELECT *
FROM populations
WHERE life_expectancy > 1.15 * (SELECT AVG(life_expectancy) FROM populations WHERE year = 2015)
  AND year = 2015;





-- Return the name, country_code and urbanarea_pop for all capital cities (not aliased).
-- Select relevant fields from cities table
SELECT name, country_code, urbanarea_pop
FROM cities
-- Filter using a subquery on the countries table
WHERE name in (SELECT capital From countries)
ORDER BY urbanarea_pop DESC;




-- Find top nine countries with the most cities
SELECT countries.name AS country, COUNT(*) AS cities_num
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
GROUP BY country
-- Order by count of cities as cities_num
ORDER BY cities_num DESC, country
LIMIT 9;



SELECT countries.name AS country,
-- Subquery that provides the count of cities   
  (SELECT count(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;





-- Select code, and language count as lang_num
SELECT code, COUNT(*) AS lang_num
FROM languages
GROUP BY code;


-- Select local_name and lang_num from appropriate tables
SELECT local_name, sub.lang_num
FROM countries,
    (SELECT code, COUNT(*) AS lang_num
     FROM languages
     GROUP BY code) AS sub
-- Where codes match    
WHERE countries.code = sub.code
ORDER BY lang_num DESC;







-- Select relevant fields
SELECT code, inflation_rate, unemployment_rate
FROM economies
WHERE year = 2015 
  AND code IN
-- Subquery returning country codes filtered on gov_form
	(SELECT code FROM countries WHERE gov_form LIKE '%Republic%' OR gov_form LIKE '%Monarchy%')
ORDER BY inflation_rate;







-- Select fields from cities
SELECT 
  name, 
  country_code, 
  city_proper_pop, 
  metroarea_pop, 
  city_proper_pop / metroarea_pop * 100 AS city_perc
FROM cities 
-- Use subquery to filter city name
WHERE name IN 
  (SELECT capital 
  FROM countries 
  WHERE (continent = 'Europe' OR continent LIKE '%America') 
  AND metroarea_pop IS NOT NULL )
ORDER BY city_perc DESC 
LIMIT 10 










