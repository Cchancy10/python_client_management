clients = []

while True:
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email address: ")
    phone = input("Phone Number: ")

    client = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
}

    clients.append(client)
    print(clients)
