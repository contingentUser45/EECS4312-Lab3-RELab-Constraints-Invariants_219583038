# Task 2: Requirement Classification

I selected 8 questions and categorized each by type

1. *Invariant* **Can it dispense the same medication to the same patient more than once within a fixed period?**
   <br>Justification: This defines a system wide safety property that must always hold.

2. *Invariant* **Are maximum dose limits defined per dispensing or over a time period?**
   <br>Justification: This controls how the doses are controlled as a condition that must be true over changes.

3. *Invariant* **different patients receive the same medication independently?, Invariant**
   <br>Justification: This expresses a condition that must always hold across all system states.

4.  *Constraint* **Are patient identifiers unique?**
   <br>Justification: This limits the structure and validity of identifying data.

5. *Constraint* **Is there a maximum allowable dose for each medication?**
   <br>Justification: This restricts acceptable input values for medication dosage.

6. *Constraint* **Do controlled substances require stricter limits?**
   <br>Justification: Certain drugs are listed as controlled substances according to Canadian Law, with additional restrictions.

7. *Functional Requirement* **What should happen if the system trys to dispense medicine exceeding the allowed dosage?**
   <br>Justification: This defines system behavior in response to invalid operations.

8. *Functional Requirement* **Should the system track dispensing per patient?**
   <br>Justification: This specifies core behavior the system must provide.

   
