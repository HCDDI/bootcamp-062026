import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "bus_data.json")


class Route:
    def __init__(self, route_id, origin, destination, stops, departure_time):
        self.route_id = route_id
        self.origin = origin
        self.destination = destination
        self.stops = stops
        self.departure_time = departure_time

    def matches(self, origin=None, destination=None):
        if origin and origin.lower() != self.origin.lower():
            return False
        if destination and destination.lower() != self.destination.lower():
            return False
        return True

    def to_dict(self):
        return {
            "route_id": self.route_id,
            "origin": self.origin,
            "destination": self.destination,
            "stops": self.stops,
            "departure_time": self.departure_time,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["route_id"],
            data["origin"],
            data["destination"],
            data["stops"],
            data["departure_time"],
        )

    def __str__(self):
        return f"{self.route_id}: {self.origin} -> {self.destination} at {self.departure_time}"


class Driver:
    def __init__(self, driver_id, name, license_number, phone):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.phone = phone

    def to_dict(self):
        return {
            "driver_id": self.driver_id,
            "name": self.name,
            "license_number": self.license_number,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["driver_id"],
            data["name"],
            data["license_number"],
            data["phone"],
        )

    def __str__(self):
        return f"Driver {self.driver_id}: {self.name} ({self.license_number})"


class Passenger:
    def __init__(self, ticket_id, name, bus_id, seat_number, age=None, phone=None):
        self.ticket_id = ticket_id
        self.name = name
        self.bus_id = bus_id
        self.seat_number = seat_number
        self.age = age
        self.phone = phone

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "name": self.name,
            "bus_id": self.bus_id,
            "seat_number": self.seat_number,
            "age": self.age,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ticket_id"],
            data["name"],
            data["bus_id"],
            data["seat_number"],
            data.get("age"),
            data.get("phone"),
        )

    def __str__(self):
        return f"{self.ticket_id}: {self.name} on {self.bus_id}, seat {self.seat_number}"


class Bus:
    def __init__(self, bus_id, route, capacity, driver=None):
        self.bus_id = bus_id
        self.route = route
        self.capacity = capacity
        self.driver = driver
        self.seats_booked = {}

    def available_seats(self):
        return self.capacity - len(self.seats_booked)

    def book_seat(self, passenger):
        if self.available_seats() == 0:
            raise ValueError("Bus is full")
        seat_number = 1
        while seat_number in self.seats_booked:
            seat_number += 1
        self.seats_booked[seat_number] = passenger
        return seat_number

    def cancel_seat(self, seat_number):
        self.seats_booked.pop(seat_number, None)

    def seat_map(self):
        rows = []
        for seat in range(1, self.capacity + 1):
            rows.append("X" if seat in self.seats_booked else "_")
        return " ".join(rows)

    def to_dict(self):
        return {
            "bus_id": self.bus_id,
            "route_id": self.route.route_id,
            "capacity": self.capacity,
            "driver_id": self.driver.driver_id if self.driver else None,
            "seats_booked": {str(seat): passenger.to_dict() for seat, passenger in self.seats_booked.items()},
        }

    @classmethod
    def from_dict(cls, data, route_lookup, driver_lookup):
        route = route_lookup[data["route_id"]]
        driver = driver_lookup.get(data.get("driver_id"))
        bus = cls(data["bus_id"], route, data["capacity"], driver)
        for seat, passenger_data in data["seats_booked"].items():
            passenger = Passenger.from_dict(passenger_data)
            bus.seats_booked[int(seat)] = passenger
        return bus

    def __str__(self):
        driver_name = self.driver.name if self.driver else "Unassigned"
        return f"{self.bus_id}: route {self.route.route_id}, driver {driver_name}, {self.available_seats()} seats available"


class BookingSystem:
    def __init__(self, storage_file=DATA_FILE):
        self.routes = {}
        self.buses = {}
        self.drivers = {}
        self.passengers = {}
        self.next_ticket_id = 1
        self.storage_file = storage_file
        self.load_state()

    def _next_ticket_id(self):
        ticket = f"T{self.next_ticket_id:03d}"
        self.next_ticket_id += 1
        return ticket

    def add_route(self, route_id, origin, destination, stops, departure_time):
        if route_id in self.routes:
            raise ValueError(f"Route {route_id} already exists")
        route = Route(route_id, origin, destination, stops, departure_time)
        self.routes[route_id] = route
        self.save_state()
        return route

    def add_driver(self, driver_id, name, license_number, phone):
        if driver_id in self.drivers:
            raise ValueError(f"Driver {driver_id} already exists")
        driver = Driver(driver_id, name, license_number, phone)
        self.drivers[driver_id] = driver
        self.save_state()
        return driver

    def add_bus(self, bus_id, route_id, capacity, driver_id=None):
        if bus_id in self.buses:
            raise ValueError(f"Bus {bus_id} already exists")
        route = self.routes.get(route_id)
        if route is None:
            raise ValueError(f"Route {route_id} does not exist")
        driver = self.drivers.get(driver_id) if driver_id else None
        bus = Bus(bus_id, route, capacity, driver)
        self.buses[bus_id] = bus
        self.save_state()
        return bus

    def assign_driver(self, bus_id, driver_id):
        bus = self.buses.get(bus_id)
        if bus is None:
            raise ValueError(f"Bus {bus_id} not found")
        driver = self.drivers.get(driver_id)
        if driver is None:
            raise ValueError(f"Driver {driver_id} not found")
        bus.driver = driver
        self.save_state()
        return bus

    def list_routes(self):
        return list(self.routes.values())

    def list_buses(self):
        return list(self.buses.values())

    def list_drivers(self):
        return list(self.drivers.values())

    def search_routes(self, origin=None, destination=None):
        return [route for route in self.routes.values() if route.matches(origin, destination)]

    def book_ticket(self, name, bus_id, age=None, phone=None):
        bus = self.buses.get(bus_id)
        if bus is None:
            raise ValueError(f"Bus {bus_id} does not exist")
        if bus.available_seats() == 0:
            raise ValueError(f"Bus {bus_id} is full")

        ticket_id = self._next_ticket_id()
        passenger = Passenger(ticket_id, name, bus_id, None, age, phone)
        seat_number = bus.book_seat(passenger)
        passenger.seat_number = seat_number
        self.passengers[ticket_id] = passenger
        self.save_state()
        return passenger

    def cancel_ticket(self, ticket_id):
        passenger = self.passengers.pop(ticket_id, None)
        if passenger is None:
            raise ValueError(f"Ticket {ticket_id} not found")
        bus = self.buses.get(passenger.bus_id)
        if bus is not None:
            bus.cancel_seat(passenger.seat_number)
        self.save_state()
        return passenger

    def get_passenger(self, ticket_id):
        return self.passengers.get(ticket_id)

    def get_bus_passengers(self, bus_id):
        bus = self.buses.get(bus_id)
        if bus is None:
            raise ValueError(f"Bus {bus_id} does not exist")
        return list(bus.seats_booked.values())

    def show_schedule(self):
        return [str(route) for route in sorted(self.routes.values(), key=lambda r: r.departure_time)]

    def get_bus_seat_map(self, bus_id):
        bus = self.buses.get(bus_id)
        if bus is None:
            raise ValueError(f"Bus {bus_id} not found")
        return bus.seat_map()

    def save_state(self):
        data = {
            "routes": [route.to_dict() for route in self.routes.values()],
            "drivers": [driver.to_dict() for driver in self.drivers.values()],
            "buses": [bus.to_dict() for bus in self.buses.values()],
            "passengers": [passenger.to_dict() for passenger in self.passengers.values()],
            "next_ticket_id": self.next_ticket_id,
        }
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_state(self):
        if not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.routes = {item["route_id"]: Route.from_dict(item) for item in data.get("routes", [])}
        self.drivers = {item["driver_id"]: Driver.from_dict(item) for item in data.get("drivers", [])}
        self.buses = {
            item["bus_id"]: Bus.from_dict(item, self.routes, self.drivers)
            for item in data.get("buses", [])
        }
        self.passengers = {
            item["ticket_id"]: Passenger.from_dict(item)
            for item in data.get("passengers", [])
        }
        self.next_ticket_id = data.get("next_ticket_id", 1)


def print_header(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


def get_input(prompt):
    return input(prompt).strip()


def show_menu():
    print_header("Bus Transportation System")
    print("1. Add route")
    print("2. Add driver")
    print("3. Add bus")
    print("4. Assign driver to bus")
    print("5. Search routes")
    print("6. Show all buses")
    print("7. Book ticket")
    print("8. Cancel ticket")
    print("9. Show bus passengers")
    print("10. Show bus seat map")
    print("11. Show schedule")
    print("12. Exit")


def main():
    system = BookingSystem()

    if not system.routes and not system.buses:
        system.add_route("R1", "City A", "City B", ["Stop 1", "Stop 2"], "09:00")
        system.add_route("R2", "City C", "City D", ["Stop 3", "Stop 4"], "14:00")
        system.add_driver("D1", "Carlos", "LIC123", "555-1234")
        system.add_driver("D2", "Mina", "LIC456", "555-5678")
        system.add_bus("B1", "R1", 6, "D1")
        system.add_bus("B2", "R2", 5, "D2")

    while True:
        try:
            show_menu()
            choice = get_input("Choose an option: ")

            if choice == "1":
                route_id = get_input("Route ID: ")
                origin = get_input("Origin: ")
                destination = get_input("Destination: ")
                stops = get_input("Stops (comma separated): ").split(",")
                stops = [stop.strip() for stop in stops if stop.strip()]
                departure = get_input("Departure time: ")
                route = system.add_route(route_id, origin, destination, stops, departure)
                print("Added route:", route)

            elif choice == "2":
                driver_id = get_input("Driver ID: ")
                name = get_input("Name: ")
                license_number = get_input("License number: ")
                phone = get_input("Phone: ")
                driver = system.add_driver(driver_id, name, license_number, phone)
                print("Added driver:", driver)

            elif choice == "3":
                bus_id = get_input("Bus ID: ")
                route_id = get_input("Route ID: ")
                capacity = int(get_input("Capacity: "))
                driver_id = get_input("Driver ID (optional): ")
                driver_id = driver_id or None
                bus = system.add_bus(bus_id, route_id, capacity, driver_id)
                print("Added bus:", bus)

            elif choice == "4":
                bus_id = get_input("Bus ID: ")
                driver_id = get_input("Driver ID: ")
                bus = system.assign_driver(bus_id, driver_id)
                print("Assigned driver to bus:", bus)

            elif choice == "5":
                origin = get_input("Search origin (leave blank to ignore): ") or None
                destination = get_input("Search destination (leave blank to ignore): ") or None
                matches = system.search_routes(origin, destination)
                if not matches:
                    print("No matching routes found")
                for route in matches:
                    print(route)

            elif choice == "6":
                for bus in system.list_buses():
                    print(bus)

            elif choice == "7":
                name = get_input("Passenger name: ")
                bus_id = get_input("Bus ID: ")
                age = get_input("Age (optional): ") or None
                phone = get_input("Phone (optional): ") or None
                passenger = system.book_ticket(name, bus_id, age, phone)
                print("Booked ticket:", passenger)

            elif choice == "8":
                ticket_id = get_input("Ticket ID: ")
                passenger = system.cancel_ticket(ticket_id)
                print("Canceled ticket:", passenger)

            elif choice == "9":
                bus_id = get_input("Bus ID: ")
                passengers = system.get_bus_passengers(bus_id)
                if not passengers:
                    print("No passengers on this bus")
                for passenger in passengers:
                    print(passenger)

            elif choice == "10":
                bus_id = get_input("Bus ID: ")
                print("Seat map:", system.get_bus_seat_map(bus_id))

            elif choice == "11":
                for line in system.show_schedule():
                    print(line)

            elif choice == "12":
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid choice. Please pick a valid option.")

        except Exception as exc:
            print("Error:", exc)


if __name__ == "__main__":
    main()