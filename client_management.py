clients = []
next_client_id = 1001

while True:
    choice = input("1. Add Client\n2. Find Client\n3. Update Phone Number\n4. Delete Client\nQ. Quit\n Choose an option: ").upper()
    if choice == "Q":
        break
    elif choice == "1":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email address: ")
        phone = input("Phone Number: ")

        client = {
            "client_id" : next_client_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone
         }

        clients.append(client)
        next_client_id += 1
        print(clients)

    elif choice == "2":
        search_client = input("Enter the client ID of the client you want to find: ")
        found = False
        for client in clients:
            if client["client_id"] == int(search_client):
                print(client)
                found = True
               
        if not found:
            print("Client not found.")
    

    elif choice == "3":
        update_client = input("Enter the client ID of the client you want to update: ")
        found = False
        for client in clients:
            if client["client_id"] == int(update_client):
                new_phone = input("Enter the new phone number: ")
                client["phone"] = new_phone
                print("Phone number updated.")
                print(client["phone"])
                found = True

        if not found:
            print("Client not found.")

    elif choice == "4":
        delete_client = input("Enter the Client ID of the client you want to delete: ")

        found = False
        for client in clients:
            if client["client_id"] == int(delete_client):
                clients.remove(client)
                print("Client deleted.")
                found = True
        if not found:
            print("Client not found.")