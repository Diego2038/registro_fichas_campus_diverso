## How to execute the code

To create the virtual environment download the "virtualenv" library via pip.

<br>

```
pip install virtualenv 
```

<br> 
Create the virtual environment with named "venv"

```
python -m venv venv
```

<br>
To run the virtual environment (from the root folder): <br>
In Windows:<br>

```
.\venv\Scripts\activate
```

In Linux distributions or MacOS:<br>

```
source .\venv\bin\activate
```

<br>
Perform the dependency installations (try to have executed the virtual environment):

```
pip install -r requirements.txt
```

<br>
Perform the dependency installations (try to have run the virtual environment):

```
python manage.py makemigrations
python manage.py migrate
```

<br>
To run the Django server (in development mode):

```
python manage.py runserver
```

<br>
To close the virtual environment:

```
deactivate
``` 

## How to start the app
1. You need to create the admin user, after all the professional users just can be only created by an admin establishing the username and password with the respective security patterns. Therefore use this command:

<br>

```
python manage.py createsuperuser
``` 

<br>


2. Login in the admin panel through <b>{url}/admin/</b> with the respective username and password where you established in the previous step.

3. Search for the ***"APP_PROFESIONAL"*** module, and click the option ***Users***.

4. Click in the button ***"ADD USER"***.

5. Create the user with the username and password (it should be noted that a created password is saved encrypted in the DB)

6. Now, it's already possible to make the Login User request, in this way you can make all the requests of this application (for more information consult the considerations section).

## Considerations
A **.env** file must be created to set the pertinent state variables, just as it is in the **.env.example** file, there the specifications for the connection to the database will be defined. via Postgres.<br><br>
In Postgres you have to create a database with the same name as defined in the **.env** file for the ***NAME_DATABASE*** variable to establish the connection between Django and the database in Postgres.

## How to recreate the postman


1. **Open Postman.**

2. **Import the collection:**
- Click on the **Import** button located in the upper left corner.
- Select the **Upload Files** tab.
- Click **Choose Files** and navigate to the **postman_collections** directory within the project.
- Select the file **api_tests.postman_collection.json** and click **Open**.

3. **Configure environment variables:**
- After importing the collection, check if there are any environment variables required.
- Go to the **Environments** section in Postman.
- Create a new environment or update an existing one with the next necessary variables:
    - **numero_documento** 
    - **id_profesional** 
    - **nick** 
    - **id_seguimiento** 
    - **token** 
    - **url** (this variable must be set to the URL where the server is mounted, if you're executing this code in your local host then establish it as ***localhost:8000***)
- Set the values for these variables according to your local setup.

4. **Run the collection:**
- Select the imported collection **api_tests**.
- Click on the **Run** button to execute the requests in the collection.
- You can also run individual requests by selecting them and clicking the **Send** button.