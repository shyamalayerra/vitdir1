import json

def calculate_average(grades):
    return sum(grades) / len(grades)

def generate_report(data):
    report = []
    for student, grades in data.items():
        avg = calculate_average(grades)
        report.append(f"{student}: {avg:.2f}")
    return "\n".join(report)

if __name__ == "__main__":
    with open("grades.json") as f:
        data = json.load(f)
    report = generate_report(data)
    with open("report.txt", "w") as f:
        f.write(report)
    print("Report generated successfully!")
