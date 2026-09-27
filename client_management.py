clients = []

while True:
    choice = input("1. Add Client\n 2. Find Client\n Q. Quit\n Choose an option: ").upper()
    if choice == "Q":
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

    elif choice == "2":
        search_client = input("Enter the first name of the client you want to find: ")
        found = False
        for client in clients:
            if client["first_name"].lower() == search_client.lower():
                print(client)
                found = True
        if not found:
            print("Client not found.")