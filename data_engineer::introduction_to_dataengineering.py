#####
'''
1) What is data engineering
2) Tools Data engineers use 
3) Extract, Transform, Load
4) Data engineering at datacamp
'''


"""
--------------------------------------------------
|
|   Data Engineers 
        +
|_________________________________________________

"""

# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)

####
#What is parrallel computing 
multiproceessing.pool 

from multiprocessing import Pool 

def take_mean_age(year_and_group):
    year, group = year_and_group 
    return pd.DataFrame({"Age":group["Age"].mean()}, index=[year])

with Pool(4) as p: #4 seperate processes 
    results = p.map(take_mean_age, athletes_events.groupby("Year"))

results_df = pd.concat(results)

#
#dask 