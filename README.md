# music-collection
A small application built with Django Framework, should be able to store artist names, their albums and songs

How to run this project locally? (Windows)



* Install [python](https://www.python.org/downloads/) 3.8 or later  
* Clone or download the project to your local environment  
* Open a command prompt, navigate to the project root and run the command  
> pip install -r requirements.txt
* Install [postgreSQL](https://www.postgresql.org/download/)
> You don't need any Stack Builder tools but create a password that you will remember for the super user.
* In the Windows search tab, type ***psql*** and open the postgreSQL shell
* Press enter 4 times, the prompt will ask for the password created during installation.
* Create a database for the application with the command
> CREATE DATABASE *music_collection*;  
> **Note:** You can change *music_collection* to whatever name you prefer.
* There is a directory called *contrib* in the root of the project, inside it there is the *env_sample* file 
* Copy the env_sample file and paste it into the *musics* directory
* Rename the file to .env
> **Attention!** This file will contain your local variables and should not be uploaded to any repository, the **.env** name is already in the .gitignore file
* Change the constant variables in the *.env* file according to their values and according to the template
> **P.S:**  
> ***SECRET_KEY*** must be any string  
> ***DATABASE_URL*** The example fields written in capital letters must be changed, the default values are:  
> **USERNAME** = postgres   
> **PASSWORD** = The password you created when installing postgresql  
> **HOST** = localhost  
> **DBNAME** = music_collection if you have not changed the command provided in this guide.
* From the command prompt at the root of the project, run the command:
> python manage.py migrate  
>
> **Note:** This command will create the structure that this project expects in your local database.
* In the same terminal, create a superuser with the command:
> python manage.py createsuperuser  
>
> **Note:** For testing purposes, you can enter *admin* in all fields
* Perform the collection of static files, in the same terminal run the command:
> python manage.py collectstatic
* Now let's run the server:
> python manage.py runserver  
> 
> **Note:** If everything went well, the application will be listening at http://127.0.0.1:8000 and can also be accessed at http://localhost:8000
