"# SOA_Task3" 
I have implemented JWT authentication. 
There are 3 new files created as auth_middleware.py, userModel.py and userModule.py
userModel.py file is responsible for User activities such as creating a user, login user, and find user for a specific username. For my JWT implementation I have only implemented dummy class and please reffer this class the person who are implementing user registration and login. 
userModel.py file contains the login end point which will return a JWT on success login. In any abnormal path 403 or 500 will be returned. 
auth_middleware.py file is responsible for implementing the decorator which checks and validate the JWT in every request

A new code added to the main.py file to generate salt for the hash to generate JWT. Whenever application start the salt will be changed. 

I have protected the route /students with the help of my decorator now only authenticatted users can access it.  
