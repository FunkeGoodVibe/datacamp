
#https://app.datacamp.com/learn/skill-tracks/data-manipulation-with-python
####################################
# Inspecting the dataframe
####################################
# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

####################################
# Parts of a dataframe
####################################
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

####################################
# Sorting and subsetting rows & columns
####################################
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[
    (homelessness["family_members"] < 1000) 
    & 
    (homelessness["region"] == "Pacific")
    ]

# See the result
print(fam_lt_1k_pac)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)


####################################
# Q: Filter the USA states in the state canu
####################################
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)


####################################
# Q: Filter the USA states in the state canu
####################################

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_homeless col as proportion of total homeless population to the state population
homelessness["p_homeless"] = homelessness["total"] / homelessness["state_pop"]

# See the result
print(homelessness)

##########

jobs["date_of_bith"].min()
jobs["date_of_bith"].max()

def percentage30(column):
    return column.quantile(0.3) #returns 30% columns

jobs["weight_kg"].agg(percentage30) #pass function, returns 30 percentile for given column


###
jobs["weight_kg"]
jobs["weight_kg"].cumsum() # returns the cumalative sum


.cummax()
.cummin()
.cumprod()
