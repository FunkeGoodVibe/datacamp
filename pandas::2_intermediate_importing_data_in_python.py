###
#
###

'''
urllib - provides interface for fetching data across the web
urlopen() - accepts urls
'''


from urllib.request import urlretrieve 
url = "www.test.com"
urlretrieve(url, "filename.csv")




# Activity 1: read a url from the internet. 
from urllib.request import urlretrieve
import pandas as pd
url = "https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv" # Assign url of file: url
urlretrieve(url, "winequality-red.csv") # Save file locally
df = pd.read_csv('winequality-red.csv', sep=';') # Read file into a DataFrame and print its head
print(df.head())



#Activity 2: read a url and save to df 
import matplotlib.pyplot as plt
import pandas as pd
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv' # Assign url of file: url
df = pd.read_csv(url, sep=";") # Read file into a DataFrame: df
print(df.head()) # Print the head of the DataFrame

df.iloc[:, 0].hist() # Plot first column of df
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()



#Activity 3: Read a specific excel sheet, along with the head of a single sheet. 
import pandas as pd
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls' # Assign url of file: url
df = pd.read_excel(url, sheet_name=None) # Read in all sheets of Excel file: xls
print(df.keys()) # Print the sheetnames to the shell
print(df['1700'].head()) # Print the head of the first sheet (using its name, NOT its index)
