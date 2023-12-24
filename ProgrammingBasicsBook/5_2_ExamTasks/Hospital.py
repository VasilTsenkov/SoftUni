period = int(input())

SumtreatedPatients = 0
SumuntreatedPatients = 0
doctors = 7

for i in range(1, period + 1):
    patients = int(input())
    if i % 3 != 0:
        if patients <= doctors:
            treatedPatients = patients
            SumtreatedPatients += treatedPatients
        else:
            treatedPatients = doctors
            untreatedPatients = patients - treatedPatients
            SumuntreatedPatients += untreatedPatients
            SumtreatedPatients += treatedPatients
    elif i % 3 == 0:
        if SumuntreatedPatients > SumtreatedPatients:
            doctors += 1
        if patients <= doctors:
            treatedPatients = patients
            SumtreatedPatients += treatedPatients
        else:
            treatedPatients = doctors
            untreatedPatients = patients - treatedPatients
            SumuntreatedPatients += untreatedPatients
            SumtreatedPatients += treatedPatients

print(f"Treated patients: {SumtreatedPatients}.")
print(f"Untreated patients: {SumuntreatedPatients}.")
