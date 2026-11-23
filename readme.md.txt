#To run the code->  uvicorn main:app --reload

#For virtual environment -> python -m venv venv
#To activate the virtual environment -> .\venv\Scripts\Activate.ps1

#Now in this environment we can install anything like pip install fastapi uvicorn

# if we write /docs in the url then we can see the documnet of the api--> this is known as swagger ui where we can test our api without postman

#path parameter --> used for dynamic routing or used to identify specific resource (see lec-3 code)
#with datatype

#Query parameter-->> user for searching and filtering (see lec-4 code)
#optional parameter-->> if they are missing then it does not show error
#default parameter-->> if they are mising then shows its default values

#post api-> post api cannot be test on browser we need to test it on postman or we can use swagger ui 
#In this we can pass the data as dictionary
#pyndatic: used to validate or define data structure


#pydantic model-->> Also used to create schema(lec-6)
#nested model-->connect one class to another class or we can use class into another class


#crud operation-->> lec-7

# Path + Body + Query --> lec-8

#Response model-->>it is used to hide data from frontend like sensitive information,even though sensitive data come fron databse but we will not show it to frontend(lec-9)
