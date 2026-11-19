#To run the code->  uvicorn main:app --reload

#For virtual environment -> python -m venv venv
#To activate the virtual environment -> .\venv\Scripts\Activate.ps1

#Now in this environment we can install anything like pip install fastapi uvicorn

# if we write /docs in the url then we can see the documnet of the api--> this is known as swagger ui where we can test our api without postman

#path parameter --> used for dynamic routing or used to identify specific resource (see lec-3 code)
#with datatype

#Query parameter-->> user for searching and filtering (see lec-4 code)
#optional parameter-->> we can give default value so if they are missing then it does not show error and show their default values