from models import Admin, Bus, Passenger


class BusSystem:
    def __init__(self) -> None:
        self.buses: list[Bus] = []
        self.passengers: list[Passenger] = []

    def add_bus(self, number: str, route: str, seats: int, admin: Admin) -> Bus:
        if not admin.is_logged_in:
            raise PermissionError("Admin login required to add a bus")
        if any(existing.number == number for existing in self.buses):
            raise ValueError(f"Bus number already exists: {number}")
        bus = Bus(number=number, route=route, total_seats=seats)
        self.buses.append(bus)
        return bus

    def find_bus(self, number: str) -> Bus | None:
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None

    def book_ticket(self, bus_number: str, name: str, phone: str) -> Passenger:
        bus = self.find_bus(bus_number)
        if bus is None:
            raise ValueError(f"Bus not found: {bus_number}")
        if not bus.book_seat():
            raise ValueError(f"No available seats on bus: {bus_number}")
        passenger = Passenger(name=name, phone=phone, bus=bus)
        self.passengers.append(passenger)
        return passenger

    def book_seat(self, name: str, phone: str, bus_number: str) -> Passenger:
        return self.book_ticket(bus_number=bus_number, name=name, phone=phone)

    def show_buses(self) -> None:
        if not self.buses:
            print("No buses available.")
            return
        for bus in self.buses:
            print(f"{bus.number} | {bus.route} | seats left: {bus.available_seats()}")

