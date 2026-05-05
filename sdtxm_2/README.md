# Bus Booking OOP Project

A small command-line bus booking system built with object-oriented programming. It supports an admin login, bus management, ticket booking, and viewing available seats.

## Features

- Admin authentication (default credentials: `admin` / `1234`).
- Add buses with route and seat capacity.
- Book tickets with passenger details.
- View all buses with available seats.
- Fixed fare display for each ticket (৳500).

## Project Structure

- `main.py`: entry point that starts the CLI.
- `ui.py`: user/admin menus and input handling.
- `system.py`: core booking logic and bus management.
- `models.py`: data models (`Bus`, `Passenger`, `Admin`).

## How It Works

1. The program starts in `main.py`, which calls `run_cli()` from `ui.py`.
2. `ui.py` shows a user menu and takes input for login, booking, or viewing buses.
3. `system.py` manages buses and bookings, enforcing rules like seat availability and admin-only bus creation.
4. `models.py` stores the data structures used across the system:
   - `Bus`: tracks route, seat capacity, and bookings.
   - `Passenger`: stores passenger details and the booked bus.
   - `Admin`: validates login and controls access to admin features.

## How To Run

Run the CLI:

```bash
python main.py
```

## Menus

**User Menu**
1. Admin Login
2. Book Ticket
3. View Buses
4. Exit

**Admin Menu** (available after login)
1. Add Bus
2. View All Buses
3. Logout

## Usage Walkthrough

1. Start the program.
2. Choose **Admin Login** and enter:
   - Username: `admin`
   - Password: `1234`
3. Add a bus by providing the bus number, route, and total seats.
4. Return to the user menu and book a ticket:
   - Enter bus number, passenger name, and phone.
   - The system confirms booking and shows a fixed fare of ৳500.
5. Use **View Buses** to see seat availability.

## Validation and Errors

- Duplicate bus numbers are rejected.
- Booking fails when a bus is full or not found.
- Invalid menu choices show a clear prompt to choose a valid option.
- Admin-only actions require a successful login.

## Notes

- This project uses only Python's standard library.
- No external dependencies are required.


