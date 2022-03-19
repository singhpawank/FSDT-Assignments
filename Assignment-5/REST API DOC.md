# REST API User-Item-Booking

This is a rest api to create users events and booking.  
This is created with django rest framework.

### 1. <span style="color: yellow;">POST</span> Add User

```
http://localhost:8000/api/user
```

Post request to add user

**Body** Raw(json)

```json
{
  "name": "User",
  "email": "user@gmail.com"
}
```

**Examples**

1. Add a user

   Request

   curl --location --request POST 'http://localhost:8000/api/user'      
   --data-raw 
   ```json
   '{
      "name" : "user-5",
      "email" : "user5@gmail.com"
   }'
   ```

   Response

   ```json
   {
     "uid": "ee19ecda-8d61-493c-bae1-7c9228905445",
     "name": "user-5",
     "email": "user5@gmail.com"
   }
   ```

   **_Status Code:_** 200

2. Add a user with existing email  
   Request

   
   curl --location --request POST 'http://localhost:8000/api/user'   
   --data-raw 
   ```json
   '{
       "name" : "user-5",
       "email" : "user5@gmail.com"
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

    **_Status Code:_** 200

### 2. <span style="color: yellow;">POST</span> Add Item

```
http://localhost:8000/api/item
```

POST request to add an item

**Body:** Raw(JSON)

```json
{
  "user_uid": "7e34b34a-6287-4938-a763-85ab905763f2",
  "name": "item"
}
```

Examples:

1.  Add an item for a user

    Request

   
    curl --location --request POST 'http://localhost:8000/api/event'   
    --data-raw 
     ```json
     '{
        "user_uid":"7e34b34a-6287-4938-a763-85ab905763f2",
        "name" : "item5"

    }'
    ```

    Response

    ```json
    {
      "id": 6,
      "name": "item5",
      "user_uid": "7e34b34a-6287-4938-a763-85ab905763f2"
    }
    ```

    **_Status Code:_** 200

### 3. <span style="color: yellow;">POST</span> Add a booking

```
http://localhost:8000/api/booking
```

Post request to a booking

**Body** Raw(json)

```json
    {
    "user_uid": "655b9cbf-f12e-4fa6-83a1-384c3c7bcde5",
    "item_id": 4,
    "startDate": "2022-01-24",
    "endDate": "2022-01-26"
    }
```

**Examples**

1. Add a booking

   Request

    curl --location --request POST 'http://localhost:8000/api/booking'   
    --data-raw 
    ```json
    '{
    "user_uid":"058fe5ca-7829-4301-9a14-a04df6b54468",
    "item_id": 6,
    "startDate" : "2022-01-26",
    "endDate" : "2022-01-27"

    }'

    ```

    Response

    ```json
    {
        "id": 6,
        "startDate": "2022-01-26",
        "endDate": "2022-01-27",
        "user_uid": "058fe5ca-7829-4301-9a14-a04df6b54468",
        "item_id": 6
    }
    ```

   **_Status Code:_** 200

2. Add a overlapping booking
   Request

  
    curl --location --request POST 'http://localhost:8000/api/booking'     
    --data-raw 
    ```json
    '{
        "user_uid":"655b9cbf-f12e-4fa6-83a1-384c3c7bcde5",
        "item_id": 6,
        "startDate" : "2022-01-26",
        "endDate" : "2022-01-27"
        }'
    ```

    Response

    ```json
    {
       "message": "This booking for the item is overlapping with another booking."

    }
    ```
   **_Status Code:_** 200

### 4. <span style="color: green;">GET</span> Show user

```
http://localhost:8000/api/user
```

GET request to Show users in the table

```json
[
    {
        "uid": "058fe5ca-7829-4301-9a14-a04df6b54468",
        "name": "user-3",
        "email": "user3@gmail.com"
    },
    {
        "uid": "0a2c4211-44c7-4a27-a385-a52ed7bf2339",
        "name": "pawan",
        "email": "pawan@gmail.com"
    },
    {
        "uid": "195895f5-7545-4c85-8687-a7dd3b77a279",
        "name": "user",
        "email": "user@gmail.com"
    },
    .
    .
    .
]
```

### 5. <span style="color: green;">GET</span> Show items

```
  http://localhost:8000/api/item
```

GET request to Show items in the table

```json
[

    {
        "id": 1,
        "name": "item1",
        "user_uid": "0a2c4211-44c7-4a27-a385-a52ed7bf2339"
    },
    {
        "id": 3,
        "name": "item2",
        "user_uid": "0a2c4211-44c7-4a27-a385-a52ed7bf2339"
    },
    {
        "id": 4,
        "name": "item3",
        "user_uid": "195895f5-7545-4c85-8687-a7dd3b77a279"
    },
    .
    .
    .

]
```

### 6. <span style="color: green;">GET</span> Show booking

```
http://localhost:8000/api/booking
```

GET request to Show bookings in the table

```json
[

    {
        "id": 2,
        "startDate": "2022-01-23",
        "endDate": "2022-01-23",
        "user_uid": "655b9cbf-f12e-4fa6-83a1-384c3c7bcde5",
        "item_id": 1
    },
    {
        "id": 3,
        "startDate": "2022-01-24",
        "endDate": "2022-01-26",
        "user_uid": "655b9cbf-f12e-4fa6-83a1-384c3c7bcde5",
        "item_id": 4
    },
    {
        "id": 4,
        "startDate": "2022-01-25",
        "endDate": "2022-01-27",
        "user_uid": "7e34b34a-6287-4938-a763-85ab905763f2",
        "item_id": 3
    },

    .
    .
    .
]
```
