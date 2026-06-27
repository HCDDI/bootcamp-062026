import json
import os

from vehicles import Bus, MiniVan
from drivers import Driver


class TransportManager:

    def __init__(self, manager_name, data_file=None):

        self.manager_name = manager_name
        self.data_file = data_file or os.path.join(os.path.dirname(__file__), "transport_data.json")

        self.buses = []
        self.mini_vans = []
        self.drivers = []

        self.load_data()

    def _serialize_bus(self, bus_obj):
        return {
            "type": "bus",
            "vehicle_id": bus_obj.vehicle_id,
            "capacity": bus_obj.capacity,
            "route_number": bus_obj.route_number,
            "has_ac": bus_obj.has_ac,
        }

    def _serialize_minivan(self, van_obj):
        return {
            "type": "minivan",
            "vehicle_id": van_obj.vehicle_id,
            "capacity": van_obj.capacity,
            "trip_purpose": van_obj.trip_purpose,
        }

    def _serialize_driver(self, driver_obj):
        return {
            "type": "driver",
            "driver_id": driver_obj.driver_id,
            "name": driver_obj.name,
            "license_number": driver_obj.license_number,
            "contact": driver_obj.contact,
        }

    def _save_to_file(self):
        data = {
            "buses": [self._serialize_bus(bus) for bus in self.buses],
            "mini_vans": [self._serialize_minivan(van) for van in self.mini_vans],
            "drivers": [self._serialize_driver(driver) for driver in self.drivers],
        }

        with open(self.data_file, "w", encoding="utf-8") as file_handle:
            json.dump(data, file_handle, indent=2)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as file_handle:
                data = json.load(file_handle)
        except (json.JSONDecodeError, FileNotFoundError):
            return

        self.buses = []
        self.mini_vans = []
        self.drivers = []

        for item in data.get("buses", []):
            self.buses.append(Bus(
                item["vehicle_id"],
                item["capacity"],
                item["route_number"],
                item.get("has_ac", False),
            ))

        for item in data.get("mini_vans", []):
            self.mini_vans.append(MiniVan(
                item["vehicle_id"],
                item["capacity"],
                item["trip_purpose"],
            ))

        for item in data.get("drivers", []):
            self.drivers.append(Driver(
                item["driver_id"],
                item["name"],
                item["license_number"],
                item["contact"],
            ))

    def add_bus(self, bus_obj):

        if isinstance(bus_obj, Bus):
            self.buses.append(bus_obj)
            self._save_to_file()
            print("Bus added successfully.")
        else:
            print("Invalid Bus Object.")

    def add_minivan(self, van_obj):

        if isinstance(van_obj, MiniVan):
            self.mini_vans.append(van_obj)
            self._save_to_file()
            print("MiniVan added successfully.")
        else:
            print("Invalid MiniVan Object.")

    def add_driver(self, driver_obj):

        if isinstance(driver_obj, Driver):
            self.drivers.append(driver_obj)
            self._save_to_file()
            print("Driver added successfully.")
        else:
            print("Invalid Driver Object.")

    def display_all_vehicles(self):

        all_vehicles = self.buses + self.mini_vans

        if len(all_vehicles) == 0:
            print("\nNo vehicles available.")
            return

        print("\n" + "=" * 60)
        print("ACE Engineering College Vehicle Fleet")
        print("=" * 60)

        for vehicle in all_vehicles:
            vehicle.display_info()

    def display_all_drivers(self):

        if len(self.drivers) == 0:
            print("\nNo Drivers Registered.")
            return

        print("\n" + "=" * 60)
        print("Registered Drivers")
        print("=" * 60)

        for driver in self.drivers:
            driver.display_info()

    def search_vehicle(self, vehicle_id):

        all_vehicles = self.buses + self.mini_vans

        for vehicle in all_vehicles:

            if vehicle.vehicle_id == vehicle_id:

                print("\nVehicle Found")
                print("-" * 40)

                vehicle.display_info()

                return

        print("Vehicle Not Found.")

    def display_dashboard(self):

        print("\n" + "=" * 60)
        print("TRANSPORT DASHBOARD")
        print("=" * 60)

        print(f"Manager Name       : {self.manager_name}")
        print(f"Total Buses        : {len(self.buses)}")
        print(f"Total MiniVans     : {len(self.mini_vans)}")
        print(f"Total Drivers      : {len(self.drivers)}")

        print("=" * 60)


if __name__ == "__main__":

    manager = TransportManager("Mr. Ramesh")

    bus1 = Bus(
        "AP28Z1234",
        50,
        3,
        True
    )

    bus2 = Bus(
        "AP28Z5678",
        45,
        1,
        False
    )

    van1 = MiniVan(
        "TS09AB4567",
        18,
        "Industrial Visit"
    )

    driver1 = Driver(
        "D001",
        "Ramesh",
        "DL0123456789ABCD",
        "9876543210"
    )

    manager.add_bus(bus1)
    manager.add_bus(bus2)
    manager.add_minivan(van1)
    manager.add_driver(driver1)

    print()

    manager.display_all_vehicles()

    print()

    manager.display_all_drivers()

    print()

    manager.search_vehicle("AP28Z1234")

    print()

    manager.display_dashboard()