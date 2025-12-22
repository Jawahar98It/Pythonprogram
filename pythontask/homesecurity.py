# Take usernames
username_list = input("Enter usernames separated by commas: ").split(",")
username_list = [user.strip() for user in username_list]

print("Number of users:", len(username_list))

admin = username_list[0]  # First user is admin

while True:
    print(f"\nHi, my name is {username_list}, and I am your system security reboot")
    name = input("Enter your name to continue: ").strip()

    if name in username_list:
        print(f"Hello {name}!")

        # Ask admin only about removal
        if name == admin:
            remove = input("Do you want to remove a user? (yes/no): ").lower()

            if remove == "yes":
                print("Current users:", username_list)
                user_to_remove = input("Enter username to remove: ").strip()

                if user_to_remove in username_list and user_to_remove != admin:
                    username_list.remove(user_to_remove)
                    print("Updated user list:", username_list)
                else:
                    print("Cannot remove this user.")
            elif remove == "no":
                print("No changes made.")
            else:
                print("Invalid input.")

            print("Access Granted. Welcome!")
            break
        else:
            print("Access Granted. Welcome!")
            break
    else:
        print("Access Denied. Try again.")
