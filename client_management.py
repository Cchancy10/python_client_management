clients = []

while True:
    choice = input("1. Add Client\n2. Exit\nChoose an option: ")
    if choice == "2":
        break
    elif choice == "1":
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
