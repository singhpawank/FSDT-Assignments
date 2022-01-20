
# REST API
This is a rest api to create users and events.     
This is created with django rest framework. 

### 1. <span style="color: yellow;">POST</span>     Add User
```
http://localhost:8000/api/user
```

Post request to add user

**Body** Raw(json)

```json       
{
    "name" : "Pawan Kumar",
    "gender" : "M",
    "email" : "pawankumar@gmail.com"
}
```

**Examples**
1. Add user Pawan    

    Request
    ```json
    curl --location --request POST 'http://localhost:8000/api/user' \
    --data-raw '{
        "name" : "Pawan Kumar",
        "gender" : "M",
        "email" : "pawankumar@gmail.com"
    }'
    ```

    Response           
    ```json
    {   
        "uid": "5e0c287d-bfce-41f2-8994-0de69bfdbcaf",
        "name": "Pawan Kumar",
        "gender": "M",
        "email": "pawankumar@gmail.com"
    }
    ```
    ***Status Code:*** 200


2. Add a user with existing email
    Request
    ```json
    curl --location --request POST 'http://localhost:8000/api/user' \
    --data-raw '{
        "name" : "Pawan Kumar",
        "gender" : "M",
        "email" : "pawankumar@gmail.com"
    }'
    ```

    Response 

    ```json
    {
        "email": [
        "user with this email already exists."
    ]
    }
    ```
    ***Status Code:*** 200

<br>



### 2. <span style="color: yellow;">POST</span>     Add Event
```
http://localhost:8000/api/event
```
POST request to add an user

**Body:** Raw(JSON)

```json        
{
    "user_id" : "9fb33889-e71e-4767-9792-7a9619fb44dc",
    "name" : "Birthday" ,
    "occurance" : "Y",
    "startDate" : "2022-01-01",
    "endDate": "2050-12-31"

}
```
Examples:
1. Add an event for a user 

    Request
    ```json
        curl --location --request POST 'http://localhost:8000/api/event' \
        --data-raw '{  
        "user_id": "9fb33889-e71e-4767-9792-7a9619fb44dc",
        "name": "Birthday",
        "occurance": "Y",
        "startDate": "2022-01-01",
        "endDate": "2050-12-31"
    }'
    ```
    Response
    ```json
    {
        "id": 3,
        "name": "Birthday",
        "occurance": "Y",
        "startDate": "2022-01-01",
        "endDate": "2050-12-31",
        "user_id": "9fb33889-e71e-4767-9792-7a9619fb44dc"
    }
    ```
    ***Status Code:*** 200

<br>

### 3. <span style="color: green;">GET</span> Show user
```
http://localhost:8000/api/user
```
GET request to Show users in the table

```json
[
    {
        "uid": "2fd3a274-e425-4df6-89bb-743108daa243",
        "gender": "Male",
        "name": "Aman Kumar",
        "email": "amankumar@gmail.com"
    },
    {
        "uid": "5e0c287d-bfce-41f2-8994-0de69bfdbcaf",
        "gender": "Male",
        "name": "Pawan Kumar",
        "email": "pawankumar@gmail.com"
    }
]
```
### 4. <span style="color: green;">GET</span> Show events
```
http://localhost:8000/api/event
```
GET request to Show events in the table

```json
[
    {
        "id": 4,
        "occurance": "WEEKLY",
        "name": "Quiz",
        "startDate": "2022-01-20",
        "endDate": "2022-03-30",
        "user_id": "5e0c287d-bfce-41f2-8994-0de69bfdbcaf"
    },
    {
        "id": 5,
        "occurance": "YEARLY",
        "name": "Birthday",
        "startDate": "2022-01-01",
        "endDate": "2050-12-31",
        "user_id": "2fd3a274-e425-4df6-89bb-743108daa243"
    }
]
```

