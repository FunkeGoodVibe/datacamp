## introduction 

"""
API - refers to web application using HTTP protocol to trasmit data 
Web App - application that serves traffic over the web. 
Web Framework - software framework that helps to build web applications.

FastAPI is a fast way to build high-performance APIs using Python
"""

"""
#FastAPI: Very Fast 
#LowCode and Easy to Learn: Python annoations and hints
#Robust: Production-ready code with autodoc 
#Standards-based: Based on OpenAPI and JSON schema 
"""



"""
Flask: Build web-based GUIs apps | ORM optional 
FASTAPI: Builds APIs | ORM optional 
Django: Build web-based GUIs apps and APIs

"""

from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#fastapi dev main.py 


#Notes 
"""
1. Can't run FastAPI server with the "run this code" button. 
2. Define server code in the Python editior as man.py instead 
3. Run it from the terminal using 'fastapi dev main.py
4. Verify that the logs in the terminal show 'Application startup complete
5. Stop the live server by pressing 'Control + C'
6. You should install FastAPI in your own python enviornment to get used to practicing there.
"""