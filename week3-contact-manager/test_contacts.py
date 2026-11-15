
import unittest
from contacts_manager import (
    validate_phone,
    validate_email,
    search_contacts
)


class TestContactManager(unittest.TestCase):

    def setUp(self):
        self.contacts = {
            "John Doe": {
                "phone": "1234567890",
                "email": "john@example.com",
                "address": "Main Street",
                "group": "Friends"
            },
            "Sarah Smith": {
                "phone": "9876543210",
                "email": "sarah@example.com",
                "address": "Park Road",
                "group": "Work"
            }
        }

    def test_valid_phone(self):
        valid, phone = validate_phone("1234567890")
        self.assertTrue(valid)
        self.assertEqual(phone, "1234567890")

    def test_invalid_phone(self):
        valid, phone = validate_phone("12345")
        self.assertFalse(valid)
        self.assertIsNone(phone)

    def test_valid_email(self):
        self.assertTrue(validate_email("john@example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("johnexample.com"))

    def test_search_partial_name(self):
        result = search_contacts(self.contacts, "john")
        self.assertIn("John Doe", result)

    def test_search_phone(self):
        result = search_contacts(self.contacts, "9876543210")
        self.assertIn("Sarah Smith", result)

    def test_search_no_match(self):
        result = search_contacts(self.contacts, "Rahul")
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
