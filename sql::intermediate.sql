-- https://app.datacamp.com/learn/courses/intermediate-sql


-- 1) SELECTING DATA 
-- 2) FILTERINING RECORDS 
-- 3) AGGREGATE FUNCTIONS 
-- 4) SORTING AND GROUPING 


-- Question: -- 1) Select the country and distinct count of certification, with countries with more than 10 different certifications
             -- 2) Select the country and average_budget from films. Filter to countries with an average_budget of more than one billion

-- Count the number of records in the people table
SELECT count(*) as count_records FROM people 


-- Return the unique countries from the films table
SELECT DISTINCT(country)
FROM films;


-- Debug this code
SELECT certification
FROM films
LIMIT 5;


-- Count the Spanish-language films
SELECT COUNT(language) as count_spanish
FROM films
WHERE language = 'Spanish'


-- Select the title and release_year for all German-language films released before 2000
SELECT title, release_year
FROM films 
WHERE  release_year < 2000 AND language = 'German'


-- Find the title and year of films from the 1990 or 1999
SELECT title, release_year
FROM films 
WHERE release_year = 1990 OR release_year = 1999


-- Select the title and release_year for films released between 1990 and 2000
SELECT title, release_year 
FROM films 
WHERE release_year 
BETWEEN 1990 AND 2000


-- Select the names that start with B
SELECT name 
FROM people 
WHERE name LIKE 'B%'


-- Find the title and release_year for all films over two hours in length released in 1990 and 2000
SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year =  2000) AND duration > 120



-- Count the unique titles
SELECT count(distinct(title)) AS nineties_english_films_for_teens
FROM films
-- Filter to release_years to between 1990 and 1999
WHERE release_year BETWEEN 1990 and 1999
-- Filter to English-language films
and language = 'English'
-- Narrow it down to G, PG, and PG-13 certifications
and certification in ('G', 'PG', 'PG-13')


-- List all film titles with missing budgets
SELECT title as no_budget_info
FROM films
WHERE budget IS NULL


-- Query the sum of film durations
SELECT SUM(duration) as total_duration 
FROM films 


-- Calculate the sum of gross from the year 2000 or later
SELECT SUM(gross) as total_gross
FROM films
WHERE release_year >= 2000


-- Round the average number of facebook_likes to one decimal place
SELECT ROUND(AVG(facebook_likes),1) as avg_facebook_likes
FROM reviews


-- Calculate the average budget rounded to the thousands
SELECT ROUND(AVG(budget),-3) as avg_budget_thousands
FROM films


-- Calculate the title and duration_hours from films
SELECT title, (duration/60.0) as duration_hours
FROM films;


-- Round duration_hours to two decimal places
-- Round duration_hours to two decimal places
SELECT title, ROUND((duration / 60.0),2)AS duration_hours
FROM films;


-- Select the release year, duration, and title sorted by release year and duration
SELECT release_year, duration, title
FROM films 
ORDER BY release_year, duration



-- Find the release_year and film_count of each year
SELECT release_year, count(*) as film_count
FROM films 
GROUP BY release_year



-- Find the release_year, country, and max_budget, then group and order by release_year and country
SELECT release_year, country, MAX(budget) as max_budget 
FROM films
GROUP BY release_year, country
ORDER BY release_year, country


-- Select the country and distinct count of certification, 
-- with countries with more than 10 different certifications


-- Select the country and distinct count of certification as certification_count
SELECT country, count(distinct(certification)) as certification_count
FROM films
-- Group by country
GROUP BY country
-- Filter results to countries with more than 10 different certifications
HAVING  count(distinct(certification))  > 10 




-- Select the country and average_budget from films
SELECT country, AVG(budget) as average_budget
FROM films
-- Group by country
GROUP BY country 
-- Filter to countries with an average_budget of more than one billion
HAVING AVG(budget)  > 1000000000 
-- Order by descending order of the aggregated budget
ORDER BY average_budget DESC



