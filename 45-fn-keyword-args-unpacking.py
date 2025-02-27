# 1. Unpacking dictionary
def setup_db_connection(hostname, port, username, password):
    print(hostname, port, username, password)
    return {
        "hostname": hostname,
        "port": port,
        "username": username,
        "password": password,
    }


data = {
    "hostname": "localhost",
    "username": "admin",
    "password": "admin123",
    "port_value": 3674,
}

data["port"] = data["port_value"]
del data["port_value"]

setup_db_connection(**data)


# 2. Unpacking dictionary or list
def create_user(username, email, password):
    # Creating user...
    return {"username": username, "email": email, "password": password}


user_details = {
    "username": "Aye-123",
    "email": "Aye@gmail.com",
    "password": "Aye1341513",
}

created_user = create_user(**user_details)
print(created_user)

user_other_details = ["alice-462", "alice@alice.com", "alice235423"]
other_created_user = create_user(*user_other_details)
print(other_created_user)
