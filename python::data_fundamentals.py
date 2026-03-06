

##
#https://app.datacamp.com/learn/skill-tracks/python-data-fundamentals

#Python lists.......
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50 

# Change "living room" to "chill zone"
areas[4] = "chill zone"

##

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

##

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)

##

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command ** 
areas_copy = list(areas)  #to create a _copy_ of a list, without reference the original use list(x)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)



#Functions and Packages ------

"""

help(max)
?max

"""

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse =True)

# Print out full_sorted
print(full_sorted)


# String Methods 

# string to experiment with: place
place = "poolhouse"
print(place)
# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place_up)


# Print out the number of o's in place
print(place.count("o"))



#

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))


# Print out how often 9.50 appears in areas
print(areas.count(9.50))


#

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

#

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

#

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# 

# Remove the correct number from the list x

x = [9, 2, 8, 4, 5] 
x.remove(5)
print(x)



#will change the list they're called on 
x.append() 
x.remove(y)
x.reverse() 


#NumPy 
import numpy as np

python_list = [1,2,3]
numpy_array = np.array([1,2,3])

python_list + python_list
#res
[1,2,3,1,2,3]

numpy_array + numpy_array 
#res
array([2,4,6])


##
bmi[1]

bmi > 22
#array([False, True, True])

bmi[bmi > 22]
array([23.442])


##
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)


# Print out type of np_baseball
print(type(np_baseball))


#

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# 

import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


# In Pandas, if one element is a string, numpy would force all other items to be a string. 

#
# NUMPY - # Select the entire second column of np

import numpy as np
1
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
#print(np_baseball[49][:])
print(np_baseball[49:])


# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
#returns = [43,34,45,32,45,75,23]

# Print out height of 124th player
print(np_baseball[124][0])

# 
#Generate Data 

#arguments for np.random.normal
height = np.round(np.random.normal(1.75, 0.20, 5000),2)

weight = np.round(np.random.normal(60.32, 15, 5000),2)

np_city = np.column_stack((height, weight))


####

import numpy as np

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:,0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

###

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))