class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = float(bill_amount)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = float(bill_amount)

    def calculate_bill(self):
        return self.bill_amount
    

class SeniorPatient(Patient):
    def calculate_bill(self):
        super().calculate_bill()
        discount = 0.2 
        return self.bill_amount * (1 - discount)

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        super().calculate_bill() 
        discount = 0.15 
        return self.bill_amount * (1 - discount)

patient1 = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patient1_bill = patient1.calculate_bill()
senior_patient_bill = senior_patient.calculate_bill()
philhealth_patient_bill = philhealth_patient.calculate_bill()

print("Hospital Billing System")
print("------------------------")

print(f"Patient: {patient1.get_name()}")
print(f"Original Bill: {patient1.get_bill_amount()}")
print(f"Final Bill: {patient1_bill}")

print(f"\nSenior Patient: {senior_patient.get_name()}")
print(f"Original Bill: {senior_patient.get_bill_amount()}")
print(f"Final Bill: {senior_patient_bill}")

print(f"\nPhilHealth Patient: {philhealth_patient.get_name()}")
print(f"Original Bill: {philhealth_patient.get_bill_amount()}")
print(f"Final Bill: {philhealth_patient_bill}")