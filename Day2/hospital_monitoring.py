import numpy as np

data = np.array([
    [[80, 37.0, 98], [82, 37.1, 97], [78, 36.9, 99], [79, 37.2, 97]],
    [[110, 38.5, 92], [108, 38.3, 91], [111, 38.7, 90], [109, 38.6, 89]],
    [[70, 36.5, 98], [71, 36.6, 97], [69, 36.7, 99], [72, 36.5, 98]],
    [[85, 37.8, 95], [84, 37.9, 96], [83, 38.0, 95], [82, 37.8, 94]],
    [[95, 37.5, 94], [97, 37.4, 93], [96, 37.6, 92], [98, 37.7, 91]],
])

def display_menu():
    print("\n----- Hospital Monitoring System -----")
    print("1. Show average vitals for each patient")
    print("2. Show vitals at a specific hour for all patients")
    print("3. Detect abnormal vitals (HR>100, Temp>38, SpO2<95)")
    print("4. Identify healthiest patient")
    print("5. Add new patient data")
    print("6. Exit")
    print("--------------------------------------")

def show_patient_averages():
    patient_avg = np.mean(data, axis=1)
    for i, avg in enumerate(patient_avg):
        print(f"\nPatient {i+1} - Avg Heart Rate: {avg[0]:.2f}, Temp: {avg[1]:.2f}°C, SpO2: {avg[2]:.2f}%")

def show_hourly_vitals():
    hour = int(input("Enter hour number (1-4): ")) - 1
    if 0 <= hour < 4:
        print(f"\nVitals at Hour {hour + 1}:")
        for i, patient in enumerate(data):
            hr, temp, spo2 = patient[hour]
            print(f"Patient {i+1}: HR={hr}, Temp={temp}°C, SpO2={spo2}%")
    else:
        print("Invalid hour. Please enter 1 to 4.")

def detect_abnormal_vitals():
    print("\nCritical Vitals (True = abnormal):")
    abnormal_hr = data[:, :, 0] > 100
    abnormal_temp = data[:, :, 1] > 38.0
    abnormal_spo2 = data[:, :, 2] < 95
    critical = abnormal_hr | abnormal_temp | abnormal_spo2

    for i, patient_flags in enumerate(critical):
        print(f"\nPatient {i+1} - Critical readings:")
        for j, flag in enumerate(patient_flags):
            print(f"  Hour {j+1}: {'YES' if flag else 'No issues'}")

def identify_healthiest_patient():
    ideal_vitals = np.array([75, 36.8, 98])
    patient_avg = np.mean(data, axis=1)
    deviation = np.abs(patient_avg - ideal_vitals)
    health_score = np.sum(deviation, axis=1)
    healthiest = np.argmin(health_score)
    print(f"\nHealthiest Patient is Patient {healthiest + 1} (Lowest deviation from ideal vitals).")

def add_new_patient():
    print("\nEnter new patient vitals for 4 hours:")
    new_patient = []
    for i in range(1, 5):
        hr = int(input(f"Hour {i} - Heart Rate: "))
        temp = float(input(f"Hour {i} - Temperature (°C): "))
        spo2 = int(input(f"Hour {i} - SpO2 (%): "))
        new_patient.append([hr, temp, spo2])
    global data
    data = np.vstack([data, [new_patient]])
    print("New patient added successfully!")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        show_patient_averages()
    elif choice == '2':
        show_hourly_vitals()
    elif choice == '3':
        detect_abnormal_vitals()
    elif choice == '4':
        identify_healthiest_patient()
    elif choice == '5':
        add_new_patient()
    elif choice == '6':
        print("Exiting... Stay healthy!")
        break
    else:
        print("Invalid choice. Please try again.")