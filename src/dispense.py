class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """
    MAX_DAILY_DOSES = {
        "Aspirin": 4000,
        "Ibuprofen": 3200,
        "Acetaminophen": 4000,
        "Amoxicillin": 3000,
        "Lorazepam": 10,
    }
    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        if not isinstance(patient_id, str) or not patient_id.strip():
            raise ValueError("Patient ID must be a non-empty string")

        if medication not in DispenseEvent.MAX_DAILY_DOSES:
            raise ValueError(f"Unknown medication: '{medication}'")

        if dose_mg <= 0:
            raise ValueError("Dose must be positive (> 0 mg)")

        max_daily = DispenseEvent.MAX_DAILY_DOSES[medication]
        if dose_mg > max_daily:
            raise ValueError(
                f"Single dose ({dose_mg} mg) exceeds maximum daily dose "
                f"({max_daily} mg) for {medication}"
            )

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants
def invariant_holds(existing_events, new_event):
    """
    Check whether adding a new dispense event preserves all system invariants.
    """
    patient = new_event.patient_id
    med = new_event.medication

    cumulative_dose = new_event.dose_mg

    for event in existing_events:
        if event.patient_id == patient and event.medication == med:
            cumulative_dose += event.dose_mg

    max_daily = DispenseEvent.MAX_DAILY_DOSES.get(med, 0)
    return cumulative_dose <= max_daily
