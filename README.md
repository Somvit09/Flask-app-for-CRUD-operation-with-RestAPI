# Flask-app-for-CRUD-operation-with-RestAPI
Flask application for CRUD operations with RestAPI
setup the application -----
1. download the project -- git clone https://github.com/Somvit09/Flask-app-for-CRUD-operation-with-RestAPI.git
2. cd Flask-app-for-CRUD-operation-with-RestAPI
3. create an virtual enviornment by ---- python3 -m venv venv
4. activate the envionment -- source venv/bin/activate
5. download all the pakages by --- pip install -r requirements.txt
6. start the mongodb compass app and connect the server to mongodb://localhost:27017
7. run command --- flask run or python3 app.py and test the application in postman

To get all the users  route - [GET] 127.0.0.1:8000/users

![Screenshot from 2023-04-29 20-22-44](https://user-images.githubusercontent.com/91347841/235310336-ebc3ad58-4c0d-49f7-af24-005037e1f384.jpg)

To get a particular user route - [GET] 127.0.0.1:8000/users/644d2a4be791c3cc21987b18

![Screenshot from 2023-04-29 20-23-54](https://user-images.githubusercontent.com/91347841/235310393-02f7540a-1f76-4f0e-8b20-afe9cb59676d.jpg)

To create an user route - [POST] 127.0.0.1:8000/users and add the data to the body->raw and set the data to json

![Screenshot from 2023-04-29 20-27-46](https://user-images.githubusercontent.com/91347841/235310485-eed94666-f2db-4a4e-b25b-f53b704a1441.jpg)

To update an user's data route - [PUT] 127.0.0.1:8000/users/644d2a4be791c3cc21987b18 and add the updated data to the body->raw and set the data to json

![Screenshot from 2023-04-29 20-29-50](https://user-images.githubusercontent.com/91347841/235310548-a30a2b74-7bf2-41e3-90a1-2211d915d136.jpg)

To delete an user route - [DELETE] 127.0.0.1:8000/users/644d2a4be791c3cc21987b18

![Screenshot from 2023-04-29 20-30-10](https://user-images.githubusercontent.com/91347841/235310647-63a06c54-df2c-4ce3-9354-901a236a58b4.jpg)

At last get all the users

![Screenshot from 2023-04-29 20-31-14](https://user-images.githubusercontent.com/91347841/235310669-ac6c22e3-eaa6-48c8-b08f-113b9435751b.jpg)

[Screencast from 2023-04-29 20-34-03.webm](https://user-images.githubusercontent.com/91347841/235310690-e22679da-487d-40fc-883d-b760e149efe4.webm)

