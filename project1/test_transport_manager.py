import os
import tempfile
import unittest

from transport_manager import TransportManager
from vehicles import Bus
from drivers import Driver


class TransportManagerPersistenceTests(unittest.TestCase):
    def test_data_persists_across_manager_instances(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = os.path.join(temp_dir, "transport_data.json")

            manager1 = TransportManager("Test Manager", data_file=data_file)
            manager1.add_bus(Bus("AP08Z2436", 30, 10, True))
            manager1.add_driver(Driver("D001", "Ramesh", "DL0123456789ABCD", "9876543210"))

            manager2 = TransportManager("Test Manager", data_file=data_file)

            self.assertEqual(len(manager2.buses), 1)
            self.assertEqual(manager2.buses[0].vehicle_id, "AP08Z2436")
            self.assertEqual(len(manager2.drivers), 1)
            self.assertEqual(manager2.drivers[0].driver_id, "D001")


if __name__ == "__main__":
    unittest.main()
