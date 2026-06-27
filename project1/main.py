1

from transport_manager import TransportManager
from vehicles import Bus, MiniVan
from drivers import Driver
from fare import RouteFare, SpecialTripFare



def display_main_menu():

    print("\n" + "=" * 60)
    print("ACE Engineering College Transportation Portal")
    print("=" * 60)

    print("1. Add New Bus")
    print("2. Add New MiniVan")
    print("3. Add New Driver")
    print("4. Display All Vehicles")
    print("5. Display All Drivers")
    print("6. Calculate Route Fare")
    print("7. Calculate Special Trip Fare")
    print("8. Search Vehicle")
    print("9. Dashboard")
    print("0. Exit")

    print("=" * 60)




def main():

    manager = TransportManager("Mr. Ramesh")

    while True:

        try:
            display_main_menu()
            choice = input("Enter Choice : ").strip()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully.")
            break

        if choice == "1":

            print("\nADD BUS")

            vehicle_id = input("Vehicle ID : ")

            if not Bus.validate_vehicle_id(vehicle_id):
                print("Invalid Vehicle ID")
                continue

            capacity = int(input("Capacity : "))
            route = int(input("Route Number : "))

            ac = input("AC Bus (yes/no): ").lower()
            has_ac = ac == "yes"

            bus = Bus(
                vehicle_id,
                capacity,
                route,
                has_ac
            )

            manager.add_bus(bus)

        elif choice == "2":

            print("\nADD MINIVAN")

            vehicle_id = input("Vehicle ID : ")

            if not MiniVan.validate_vehicle_id(vehicle_id):
                print("Invalid Vehicle ID")
                continue

            capacity = int(input("Capacity : "))
            purpose = input("Trip Purpose : ")

            van = MiniVan(
                vehicle_id,
                capacity,
                purpose
            )

            manager.add_minivan(van)


        elif choice == "3":

            print("\nADD DRIVER")

            try:

                driver = Driver(

                    input("Driver ID : "),
                    input("Driver Name : "),
                    input("License Number (16 chars): "),
                    input("Contact Number : ")

                )

                manager.add_driver(driver)

            except ValueError as e:

                print(e)


        elif choice == "4":

            manager.display_all_vehicles()


        elif choice == "5":

            manager.display_all_drivers()


        elif choice == "6":

            print("\nROUTE FARE")

            sid = input("Student ID : ")
            distance = float(input("Distance (KM): "))
            ptype = input("Pass Type (Monthly/Semester): ")

            try:

                fare = RouteFare(
                    sid,
                    distance,
                    ptype
                )

                fare.display_fare_summary()

            except ValueError as e:

                print(e)



        elif choice == "7":

            print("\nSPECIAL TRIP")

            sid = input("Student ID : ")
            distance = float(input("Distance (KM): "))
            students = int(input("No. of Students : "))

            fare = SpecialTripFare(
                sid,
                distance,
                students
            )

            fare.display_fare_summary()


        elif choice == "8":

            vid = input("Vehicle ID : ")

            manager.search_vehicle(vid)



        elif choice == "9":

            manager.display_dashboard()



        elif choice == "0":

            print("\nThank you for using ACE Transportation Portal.")
            print("Goodbye!")

            break

        else:

            print("Invalid Choice.")



if __name__ == "__main__":
    main()