
-- https://campus.datacamp.com/courses/introduction-to-sql-server/groups-strings-and-counting-things?ex=10 

-- Extract the length of string
SELECT description, LEN(description, 20) AS first_20_left 
FROM grid 

-- Extract the first 20 left characters 
SELECT description, LEFT(description, 20) AS first_20_left 
FROM grid 

-- Extract the rear 20 left characters 
SELECT description, RIGHT(description, 20) AS first_20_left 
FROM grid 

-- Find the first _ witihin the URL column 
SELECT CHARINDEX ('_', url) AS char_location  
FROM courses  


-- Extract the character start, and number of characters to extract 
SELECT SUBSTRING(url, 12, 12) AS target_selection, url  
FROM courses  


-- Extract the character start, and number of characters to extract 
SELECT TOP(5) REPLACE(url, '_', '-') AS replace_with_hyphen
FROM courses  





-- Complete the query to find `Weather` within the description column
SELECT 
  description, 
  CHARINDEX('Weather', description) 
FROM 
  grid
WHERE description LIKE '%Weather%';



-- Complete the query to find the length of `Weather'
SELECT 
  description, 
  CHARINDEX('Weather', description) AS start_of_string,
  LEN('Weather') AS length_of_string 
FROM 
  grid
WHERE description LIKE '%Weather%'; 




-- Select the region column
SELECT 
  nerc_region,
  -- Sum the demand_loss_mw column
  SUM(demand_loss_mw) AS demand_loss
FROM 
  grid
  -- Exclude NULL values of demand_loss
WHERE 
  demand_loss_mw IS NOT NULL
  -- Group the results by nerc_region
GROUP BY
  nerc_region
  -- Order the results in descending order of demand_loss
ORDER BY 
  demand_loss DESC;



-- WHERE is used to filter rows before any grouping occurs. 
--Once you have performed a grouping operation, you may want to further restrict the number of rows returned. 
--This is a job for HAVING. In this exercise, you will modify an existing query to use HAVING, 
--so that only those results with a sum of over 10000 are returned.

SELECT 
  nerc_region, 
  SUM (demand_loss_mw) AS demand_loss 
FROM 
  grid 
  -- Remove the WHERE clause
GROUP BY 
  nerc_region 
  -- Enter a new HAVING clause so that the sum of demand_loss_mw is greater than 10000
HAVING
  SUM(demand_loss_mw) > 10000 
ORDER BY 
  demand_loss DESC;



  

-- declaring 
  DECLARE @test_int INT 
  DECLARE @my_artist VARCHAR(100)

  SET @test_int = 5 

  SELECT -- 
  FROM -- 
  WHERE artist = @test_int
  AND value = @test_value 



  DROP TABLE --




  -- Declare your variables
DECLARE @start DATE
DECLARE @stop DATE
DECLARE @affected INT;
-- SET the relevant values for each variable
SET @start = '2014-01-24'
SET @stop  = '2014-07-02'
SET @affected =  5000 ;

SELECT 
  description,
  nerc_region,
  demand_loss_mw,
  affected_customers
FROM 
  grid
-- Specify the date range of the event_date and the value for @affected
WHERE event_date BETWEEN @start AND @stop
AND affected_customers >= @affected;


-- creating a temporary table 
"""
Sometimes you might want to 'save' the results of a query so you can do some more work with the data. 
You can do that by creating a temporary table that remains in the database until SQL Server is restarted. 
In this final exercise, you'll select the longest track from every album and add that into a temporary table which 
you'll create as part of the query.
"""
SELECT  album.title AS album_title,
  artist.name as artist,
  MAX(track.milliseconds / (1000 * 60) % 60 ) AS max_track_length_mins
-- Name the temp table #maxtracks
INTO #maxtracks
FROM album
-- Join album to artist using artist_id
INNER JOIN artist ON album.artist_id = artist.artist_id
-- Join track to album using album_id
INNER JOIN track ON track.album_id = album.album_id
GROUP BY artist.artist_id, album.title, artist.name,album.album_id
-- Run the final SELECT query to retrieve the results from the temporary table
SELECT album_title, artist, max_track_length_mins
FROM  #maxtracks
ORDER BY max_track_length_mins DESC, artist;