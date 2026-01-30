# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import unittest
from dispense import DispenseEvent, invariant_holds


class TestMedicationDispensingRequirements(unittest.TestCase):

    def test_rejects_non_positive_dose(self):
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Aspirin", 0, 1)
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Aspirin", -5, 1)

    def test_rejects_non_positive_or_non_integer_quantity(self):
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Ibuprofen", 400, 0)
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Ibuprofen", 400, -2)
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Ibuprofen", 400, 1.5)

    def test_rejects_unknown_medication(self):
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "UnknownDrug", 100, 1)

    def test_rejects_single_dose_exceeding_max_daily(self):
        with self.assertRaises(ValueError):
            DispenseEvent("P001", "Aspirin", 5000, 1)

    def test_prevents_duplicate_dispense_same_medication(self):
        existing = [
            DispenseEvent("P001", "Ibuprofen", 400, 1),
        ]
        duplicate = DispenseEvent("P001", "Ibuprofen", 200, 1)
        self.assertFalse(invariant_holds(existing, duplicate))

        different_med = DispenseEvent("P001", "Aspirin", 500, 1)
        self.assertTrue(invariant_holds(existing, different_med))

    def test_enforces_max_cumulative_dose(self):
        existing = [
            DispenseEvent("P001", "Aspirin", 2000, 1),
            DispenseEvent("P001", "Aspirin", 1500, 1),
        ]
        too_much = DispenseEvent("P001", "Aspirin", 1000, 1)
        self.assertFalse(invariant_holds(existing, too_much))

        acceptable = DispenseEvent("P001", "Aspirin", 400, 1)
        self.assertTrue(invariant_holds(existing, acceptable))

    def test_allows_different_patient_same_medication(self):
        existing = [
            DispenseEvent("P001", "Aspirin", 3000, 1),
        ]
        different_patient = DispenseEvent("P002", "Aspirin", 3000, 1)
        self.assertTrue(invariant_holds(existing, different_patient))


if __name__ == "__main__":
    unittest.main()