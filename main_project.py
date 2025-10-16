# main_project.py

from login_module import login_system
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import smtplib
from email.message import EmailMessage

# ================= LOGIN ===================
if not login_system():
    exit()

# ================= INPUT SECTION ===================
students = {}
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

for i in range(n):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter student name: ")
    marks = []
    for j in range(m):
        mark = int(input(f"Enter marks in Subject {j+1}: "))
        marks.append(mark)
    students[name] = marks

# ================= ANALYSIS SECTION ===================
averages = {name: np.mean(marks) for name, marks in students.items()}
topper = max(averages, key=averages.get)
lowest = min(averages, key=averages.get)
class_avg = np.mean(list(averages.values()))

# ================= GRADE SYSTEM ===================
def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    else: return "D"

grades = {name: get_grade(avg) for name, avg in averages.items()}

# ================= REPORT GENERATION ===================
filename = f"report_{datetime.now().strftime('%d_%b_%Y_%H_%M')}.txt"
with open(filename, "w") as f:
    f.write("===== SMART STUDENT PERFORMANCE ANALYZER =====\n")
    for name, marks in students.items():
        f.write(f"\n{name}: {marks} | Average: {averages[name]:.2f} | Grade: {grades[name]}")
    f.write(f"\n\nClass Average: {class_avg:.2f}")
    f.write(f"\nTopper: {topper} ({averages[topper]:.2f})")
    f.write(f"\nLowest: {lowest} ({averages[lowest]:.2f})")
    f.write(f"\nGenerated on: {datetime.now()}\n")

print(f"\nReport saved successfully as '{filename}'")

# ================= GRAPH SECTION ===================
plt.bar(averages.keys(), averages.values(), color='skyblue')
plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

# ================= EMAIL SECTION (OPTIONAL) ===================
send_mail = input("Do you want to email the report? (yes/no): ").lower()

if send_mail == "yes":
    msg = EmailMessage()
    msg["Subject"] = "Student Performance Report"
    msg["From"] = "youremail@gmail.com"
    msg["To"] = "teacher@gmail.com"
    msg.set_content("Please find the attached student performance report.")

    with open(filename, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=filename)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("youremail@gmail.com", "app_password")  # use app password
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

print("\nThank you for using Smart Student Performance Analyzer!")