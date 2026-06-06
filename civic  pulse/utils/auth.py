import streamlit as st

USERS = {
    "citizen": {
        "password": "citizen123",
        "role": "Citizen"
    },
    "officer": {
        "password": "officer123",
        "role": "Officer"
    }
}


def login(username, password):

    print("Username:", username)
    print("Password:", password)

    if username in USERS:

        print("User Found")

        if USERS[username]["password"] == password:

            print("Password Correct")

            return USERS[username]["role"]

    print("Login Failed")

    return None