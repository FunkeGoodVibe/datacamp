-- test 

-- Select film_id and imdb_score with an imdb_score over 7.0
SELECT film_id, imdb_score
FROM reviews
WHERE imdb_score > 7.0

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

