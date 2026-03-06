#
#skill track: https://app.datacamp.com/learn/skill-tracks/building-apis-in-python
#course: 

"""
Types of Web API's

SOAP: 
- DFocus on strict and formal API design
- Enterprise applications

REST:
- Focus on simplicity & scalability
- Most common API architecture 

GraphQL
- Focus on flexibility
- Optimised for performance

postman.com/state-of-api/api-technologies/#gpi-technologies
"""


"""
Working with API's in Python

*****urllib******
- bundled with python
- powerful but not very developer friendly 

from urllib.request import urlopen
api = "https://api.music-catalog.com"

with urlopen(api) as response: 
    data = response.read()
    string = data.decode()
    print(string)


*****requests******

- many powerful builr-in resources
- easier to use 

import requests 
api = "https://api.music-catalog.com/"

response = requests.get(api)
print(response.text)

"""
from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  #data = response.read()
  #string = data.decode(encoding)
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)


"""
Using the requests package
Using urllib to integrate APIs can result in verbose and complex code as you need to take care of a lot of additional things like encoding and decoding responses.

As an alternative to urllib, the requests Python package offers a simpler way to integrate APIs. A lot of functionality is available out of the box with requests, which makes your code a lot easier to write and read. Let's try the same exercise again but now with the requests package.

Remember, as with the previous exercise, the URL for the Lyrics API is http://localhost:3000/lyrics.
"""

# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get("http://localhost:3000/lyrics")

# Print out the text attribute of the response object
print(response.text)


"""
Dissecting the URL 

http:://  = PROTOCOL
350.5th-ave.com = DOMAIN
:80 = PORT
/unit/243 = PATH
?floor=77 = QUERY

Protocol = means of transportation
Domain = the street address of the office building
Port = the gate/door to use when entering the building
Path = the specific office unit inside the building 
Query = any additional instructions
"""

#Adding query parameters with requests

#create the dictionary
query_params = {'floor':77, 'elevator':True}

#pass the dictionary using the 'params' argument
response = requests.get("https://350.5th-ave.com/unit/243", params = query_params)
print(response.url)


"""
Sending data via POST and PUT
"""
#GET = Retrieve a resource 
response = requests.get("https://350.5th-ave.com/unit/243")

#POST = Create a resource 
response = requests.post("https://350.5th-ave.com/unit/243", data={"key":"value"})

#PUT = Update an exisitng resource 
response = requests.put("https://350.5th-ave.com/unit/243", data={"key":"value"})

#DELETE = Remove a resource
response = requests.delete("https://350.5th-ave.com/unit/243")



"""
ACTIVITY 1
"""
# Add the `include_track` parameter
query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)


"""
ACTIVITY 2
"""

# Get a list of all playlists from the API
response = requests.get('http://localhost:3000/playlists') #don't add the last / 
print(response.text)


"""
ACTIVITY 3 - check why 'data' used instead of 'params'
"""

# Create a dictionary with the playlist info
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data = playlist_data)
print(response.text)


"""
ACTIVITY 4
"""

# Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
requests.delete('http://localhost:3000/playlists/2')

# Get the list of all existing playlists again
response = requests.get('http://localhost:3000/playlists')
print(response.text)