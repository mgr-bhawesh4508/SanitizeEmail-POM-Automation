import time

VALID_LOGIN = [
    {
    "email":"bheweshmagar333@gmail.com",
    "password":"Magar@bhawesh4508"
    }
]

INVALID_LOGIN = [
    {
        "email" : "admin@gmail.com",
        "password": "Admin@123"
    },
    {
        "email": "",
        "password":"Admin@123"
    },
    {
        "email":"admin@gmail.com",
        "password": ""
    },
    {
        "email": "",
        "password": ""
    }
]

VALID_SIGNUP =[
    {
        "name": "Bhawesh Magar",
        "email": f"greninja4508+{int(time.time())}@gmail.com",
        "password":"Magar@bhawesh4508"
    }
]
EMAILS = [
    {
        "email": "bheweshmagar333@gmail.com",
        "password": "Magar@bhawesh4508",
        "emails_list": [
            "greninja@gmail.com",
            "ninja.com",
            "hello@gmail.com",
            ".test@email.com",
            "pikachu@@gmail.com"
        ]
    }
]