# Travel App

## Setup
### The first thing to do is to clone the repository:

- git clone https://github.com/dhanya-mohan11/Travel.git
- cd Travel
  
### Create a virtual environment to install dependencies in and activate it:

- pip install virtualenv
- virtualenv venv
- venv\Scripts\activate

### Then install the dependencies:

- pip install -r requirements.txt

  * Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
### Once pip has finished downloading the dependencies: 

- cd travel_app
- python manage.py runserver

And navigate to http://127.0.0.1:8000/

### To create a superuser for the Django admin : 
- python manage.py createsuperuser

  * Note that the email address is optional. If you created a superuser, access the Django admin interface at http://127.0.0.1:8000/admin/ and login using the superuser credentials.
    
#### To test the project, first generate a Token in the admin interface or by using a Postman. 

## To generate a Token (using Postman):
http://127.0.0.1:8000/api-token-auth/

- Method : POST 
- Body : raw :  
  {
    "username" : "dhanya",
    "password" : "12345"
  }


#### Using that Token, to check the API using a Postman:

## To List all destinations :

  http://127.0.0.1:8000/api/destinations/
  
- Method : GET 
- Headers : Key : Authorization , Value : Token (Generated Token)

## To Create a new destination :

  http://127.0.0.1:8000/api/destinations/create/
  
- Method : POST 
- Headers : Key : Authorization , Value : Token (Generated Token)
- Body : raw :  
  {
    "name": "Fort Kochi",
    "country": "India",
    "description": "Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts.",
    "best_time_to_visit": "December",
    "category": "Beach",
    "created_at": "2024-05-18T09:12:13.374082Z",
    "updated_at": "2024-05-19T05:44:31.562644Z"
}

## To retrieve a destination :

  http://127.0.0.1:8000/api/destinations/retrieve/1
  
- Method : GET 
- Headers : Key : Authorization , Value : Token (Generated Token)

## To update a destination :

  http://127.0.0.1:8000/api/destinations/update/1
  
- Method : PUT 
- Headers : Key : Authorization , Value : Token (Generated Token)
- Body : raw :  
  {
    "name": "Marine drive",
    "country": "India",
    "description": "Lorem ipsum is placeholder text.",
    "best_time_to_visit": "January",
    "category": "Mountain",
    "created_at": "2024-05-18T09:12:13.374082Z",
    "updated_at": "2024-05-19T12:27:56.553691Z"
} 

## To destroy a destination :

  http://127.0.0.1:8000/api/destinations/destroy/1
  
- Method : DELETE 
- Headers : Key : Authorization , Value : Token (Generated Token)
   * If we send the API, data will be successfully deleted. If we send it again, "Not found !!" message will be occured.

