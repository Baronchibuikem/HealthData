Name: DataHealth
Language: Python
Frameworks: Django==2.2.7, Bootstrap

A web application that stores health data of its users both for HEALTH WORKERS and PATIENTS.

Key Functionalities:

    An authentication system(Registration, Login and Logout) customized for 2 different type of users.

    A dynamically generated form where authenticated users can submit their health details voluntarily.

    A drop down filter functionality that allows any user to filter through available keywords.

    Series of dynamic table that displays users health details while restricting access to the users
    registered as patients.

    A chart that shows relationships between different fields

On the navbar:

    MedStatistics shows the statistics across different users and can be used for Research, Educational or
    Aid purposes, it also has dropdown filter functionalities.

    MedStore is a restricted view, only accessible to admin users and health workers and shows complete
    health details of all the users that has submitted a medical form.

    Medform shows a form that only authenticated users can fill inorder to help the platform keep
    documenting data for future educational/research/support purposes.

To run this web application:

    Create a new folder and set up your virtual environment inside and activate it
    git clone https://github.com/Baronchibuikem/HealthData
    cd HealthData
    pip install -r requirements.txt
    python manage.py makemigration user
    python manage.py makemigration usersmedhistory
    python manage.py makemigration
    python manage.py migrate user
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

NOTE: on migrations

    It is very important you run "python manage.py makemigration user" and "python manage.py migrate user"
    before running the general "python manage.py migrate" because we are using our own custom User model
    and we want that to be want will be registered in the database aainst using the default django User model.

NOTE: on relationships

    Alot of fields especially in our Medform is dependent(has a foreignKey relationship) to other fields
    like Country, State, Health Challenge, so as a superuser, you will have to create
    data's for this fields in the admin dashboard which will now be accessible to users to choose from
    in the medform.

NOTE: on dropdown filtering functionality

    The values on the dropdown filtering functionality located in the Medstatistic Page unfortunately
    is still static and highly dependent on the Values entered in the respective fields the relate to.
    So if i was to add "Jamaica" as a value in my Country, i will need to go to "illstatistics.html",
    locate the filtering for country and add it as an option. That way it shows up in the dropdown menu
    and the filtering functionality will automatically detect it.

Thanks for checking out this web application and it is open for further improvement.

Demo: http://datahealth4africa.herokuapp.com/
