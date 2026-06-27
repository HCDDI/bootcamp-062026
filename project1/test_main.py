import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, "/workspaces/bootcamp-062026/project1")

import main as main_module


class MainInterruptTests(unittest.TestCase):
    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_main_handles_keyboard_interrupt(self, _mock_input):
        with patch("builtins.print") as mock_print:
            main_module.main()

        output = " ".join(str(call.args[0]) for call in mock_print.call_args_list if call.args)
        self.assertIn("interrupted", output.lower())


if __name__ == "__main__":
    unittest.main()
