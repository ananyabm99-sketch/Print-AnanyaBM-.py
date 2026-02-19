# Doctor Class
class Doctor:
    def __init__(self, doctor_id, name, speciality):
        self.doctor_id = doctor_id
        self.name = name
        self.speciality = speciality
        self.schedule = []   # list of (date, time)

    def is_available(self, date, time):
        return (date, time) not in self.schedule

    def add_schedule(self, date, time):
        self.schedule.append((date, time))


# Patient Class
class Patient:
    def __init__(self, patient_id, name, ailment):
        self.patient_id = patient_id
        self.name = name
        self.ailment = ailment


# Appointment Class
class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def display(self):
        print(f"Appointment: Dr.{self.doctor.name} with {self.patient.name} on {self.date} at {self.time}")


# Hospital Management System
class HospitalManagement:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def book_appointment(self, doctor_id, patient_id, date, time):
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)

        if not doctor or not patient:
            print("Doctor or Patient not found!")
            return

        # Check double booking
        if not doctor.is_available(date, time):
            print("Doctor already booked at this time!")
            return

        # Create appointment
        appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(appointment)
        doctor.add_schedule(date, time)

        print("Appointment booked successfully!")

    def show_appointments(self):
        for app in self.appointments:
            app.display()


# ================== TESTING ==================

hospital = HospitalManagement()

# Add Doctors
d1 = Doctor(1, "Arjun", "Cardiology")
d2 = Doctor(2, "Meera", "Neurology")
hospital.add_doctor(d1)
hospital.add_doctor(d2)

# Add Patients
p1 = Patient(101, "Ravi", "Heart Pain")
p2 = Patient(102, "Ananya", "Headache")
hospital.add_patient(p1)
hospital.add_patient(p2)

# Book Appointments
hospital.book_appointment(1, 101, "2026-02-20", "10:00 AM")
hospital.book_appointment(1, 102, "2026-02-20", "10:00 AM")  # Double booking test
hospital.book_appointment(2, 102, "2026-02-20", "11:00 AM")

# Show all appointments
hospital.show_appointments()