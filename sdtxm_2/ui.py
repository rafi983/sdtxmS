from models import Admin
from system import BusSystem


def run_cli() -> None:
    system = BusSystem()
    admin = Admin(username="admin", password="1234")
    fare = 500

    while True:
        print("\nUser Menu")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if admin.login(username, password):
                print("Login successful.")
                while True:
                    print("\nAdmin Menu")
                    print("1. Add Bus")
                    print("2. View All Buses")
                    print("3. Logout")
                    admin_choice = input("Select an option: ").strip()

                    if admin_choice == "1":
                        number = input("Bus number: ").strip()
                        route = input("Route: ").strip()
                        seats_input = input("Total seats: ").strip()
                        try:
                            seats = int(seats_input)
                            system.add_bus(number=number, route=route, seats=seats, admin=admin)
                            print("Bus added.")
                        except ValueError as exc:
                            print(f"Error: {exc}")
                    elif admin_choice == "2":
                        system.show_buses()
                    elif admin_choice == "3":
                        admin.is_logged_in = False
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option. Please choose 1, 2, or 3.")
            else:
                print("Invalid credentials.")

        elif choice == "2":
            bus_number = input("Bus number: ").strip()
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            try:
                system.book_ticket(bus_number, name, phone)
                print(f"Ticket booked. Fare: ৳{fare}")
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            system.show_buses()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

