class Bus:
    def __init__(self, number: str, route: str, total_seats: int, booked_seats: int = 0) -> None:
        if total_seats < 0:
            raise ValueError("total_seats must be non-negative")
        if booked_seats < 0 or booked_seats > total_seats:
            raise ValueError("booked_seats must be between 0 and total_seats")
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = booked_seats

    def available_seats(self) -> int:
        return self.total_seats - self.booked_seats

    def book_seat(self) -> bool:
        if self.available_seats() <= 0:
            return False
        self.booked_seats += 1
        return True


class Passenger:
    def __init__(self, name: str, phone: str, bus: "Bus") -> None:
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.is_logged_in = False

    def login(self, username: str, password: str) -> bool:
        self.is_logged_in = username == self.username and password == self.password
        return self.is_logged_in

