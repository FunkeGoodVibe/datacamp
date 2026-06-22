#

#SparkSession - allows you to access your spark cluster and critical for using PySpark. 

from pyspark.sql import SparkSession

#1.1 init session 
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()
# .builder() sets up a session 
# .getOrCreate() will either get an existing session or create a new one if none exists.
# .appName() helps manage multiple sessions (by giving them a name).
print(my_spark)


#1.2 read the spark dataframe
census_adult = spark.read.csv("adult_reduced.csv")
census_adult.show()

#1.3 Create a DataFrame from CSV 
census_df = spark.read.csv("path/to/census.csv", header=True, inferSchema=True)

#1.4 Show schema 
.showSchema() 

#1.5 GroupBy
row_count = census_df.count()
print(f"Number of rows in the DataFrame: {row_count}")  

#1.6 GroupBy and Count
census_df.groupBy("gender").count().show()
census_df.groupBy("gender").agg({"salary_usd":"avg"}).show()


#.sum() 
#.min() 
#.max()

#Key dunction for PySpark analytics 
#.select(): selects specific columns from the DataFrame.
#.filter(): filters rows based on a condition.
#.groupBy(): groups rows based on one or more columns.
#.agg(): performs aggregate functions on grouped data.


#1.7 Filtered and Select
filtered_census_df = census_df.filter(df["age"] > 30).select("age", "occupation")
filtered_census_df.show() 


""" Advantage: PySpark Can distribute data and computations across many modes, enabling faster processing of large datasets."""


#1.8 Load the CSV file into a DataFrame
salaries_df = spark.read.csv("salaries.csv", header=True, inferSchema=True)
row_count = salaries_df.count()
print(f"Total rows: {row_count}")

salaries_df.groupBy("company_size").agg({"salary_in_usd": "avg"}).show() # Group by company size and calculate the average of salaries
salaries_df.show()



# 1.9 Filtering by company 
# Average salary for entry level in Canada
CA_jobs = ca_salaries_df.filter(ca_salaries_df["company_location"] == "CA").filter(ca_salaries_df['experience_level']
 == "EN").groupBy().avg("salary_in_usd")

CS_jobs = df.filter(df["location"]=="EN")\
            .filter(df["experience">5])\
            .groupBy().avg("salary_in_usd")
CA_jobs.show()

#1.10 - CSV files - delimited data. 
#       JSON files - semi-structured data. Hierarchical data.
#       Parquet files - optimised for storage and querying, often used in data negineering. 

#https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.read_csv


#1.11 Load the dataframe
census_df = spark.read.json("adults.json")
salary_filtered_census = census_df.filter(census_df["age"]>40)
salary_filtered_census.show()

#1.12 Handling missing data 
df_cleaned = df.na.drop() 
df_cleaned = df.where(col("columnName").isNotNull()) #filter out nulls 

#use .na.fill({"column":value}) to replace nulls with a specific value. 
df_filled = df.na.fill({"age":0})


#1.13 Column operations 
df = df.withColumn("age_plus_5", df["age"] + 5) #create a new column
df = df.withColumnRenamed("old_column_name", "new_column_name") #rename a column
df = df.drop("column_name") #drop a column - reduce memory usage.


# 1.13 - Activity - Create a new column 'weekly_salary'
census_df_weekly = census_df.withColumn("weekly_salary", census_df["income"]/52) # Rename the 'age' column to 'years'
census_df_weekly = census_df_weekly.withColumnRenamed("age", "years")
census_df_weekly.show() # Show the result

#1.14 row operations 
filtered_df = df.filter(df["salary"] > 50000) #filter rows based on a condition
grouped_avg_df = df.groupBy("department").avg({"salary", "age"}) #group rows and calculate average salary
grouped_sum_df = df.groupBy("department").sum({"salary"}) #group rows and calculate sum salary



#1.15 joins in pyspark 
#combine rows from two or more dataframes absed on common columns 
df_joined = df.join(df2, on="id", how="inner") #joining on id column using an inner join
df_joined = df.join(df2, df1.Id == df2.Name, "inner") #joining on columns with the different names 

#1.16 Union operations
df_union = df1.union(df2) #combine two dataframes with the same schema  


#1.17 - Working with Arrays and Maps
#Arrays: Useful for storing within columns, syntax: ArrayType(stringType(), False)
from pyspark.sql.functions import array, struct, lit 
df = df.withColumn("scores", array(lit(85), lit(90), lit(78))) #create an array column with three scores

#1.18 Maps: Key-value pairs, helpful for storing structured data within a single column, syntax: MapType(StringType(), IntegerType(), False)
from pyspark.sql.types import MapType, StringType, IntegerType  
schema = StructType([

    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("address", MapType(StringType(), StringType()), True)
])

#1.17 activity 
"""
Examine the airports DataFrame. Note which key column will let you join airports to the flights table.
Join the flights with the airports DataFrame on the "dest" column. Save the result as flights_with_airports.
Examine flights_with_airports again. Note the new information that has been added.
"""
airports.show() # Examine the data
airports = airports.withColumnRenamed("faa", "dest")# .withColumnRenamed() renames the "faa" column to "dest"
flights_with_airports = flights.join(airports, on="dest", how="leftouter") # Join the DataFrames
flights_with_airports.show() # Examine the new DataFrame


#1.18 UDF's 
"""
UDF's are custom functions to work with data using pyspark dataframes.
Advantage: 
1) Reuse and repeat common tasks, 
2) registered directly with Spark, and can be shared, 
3) pyspark <dataframes> (for small datasets)
4) pandas <udfs> (for large datasets)
"""
#define the function 
def to_uppercase(s):
    return s.upper() if s else None 

to_uppercase_udf = udf(to_uppercase, StringType()) #register the function

df = df.withColumn("name_upper#Apply the UDF to the DataFrame 


#1.19 udf activity 
"""
Register the function age_category as a UDF called age_category_udf.
Add a new column to the DataFrame df called "category" that applies the UDF to categorize people based on their age. The argument for age_category_udf() is provided for you.
Show the resulting DataFrame.
""" 
age_category_udf = udf(age_category, StringType()) # Register the function age_category as a UDF
age_category_df_2 = age_category_df.withColumn("category", age_category_udf(age_category_df["age"])) # Apply your udf to the DataFrame
age_category_df_2.show()

#1.20 - udf pandas activity 

"""
Define the add_ten_pandas() function as a pandas UDF.
Add a new column to the DataFrame called "10_plus" that applies the pandas UDF to the df column "value".
Show the resulting DataFrame.
"""
# Define a Pandas UDF that adds 10 to each element in a vectorized way
@pandas_udf(DoubleType())
def add_ten_pandas(column):
    return column + 10

df.withColumn("10_plus", add_ten_pandas(df["value"])) # Apply the UDF and show the result
df.show()

"""
What is parralisation in pyspark?
- automatically parralising data and computations across mulitple nodes in a cluster
- distributed processing of large datasets across multiple nodes 
- worker nodes process data in parallel, combining at the end of a task 
- faster processing at scale (think gb or tb)
"""

#1.21 - creating an rdd (resilient distributed datasets)
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDDExample").getOrCreate() 
census_df = spark.read.csv("/census.csv") #create a df drom a csv

census_rdd = sensus_df.rdd #covert df to rdd 
census_rdd.collect() #show the rdd's content using collect 