departments={}

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},

]

for employee in employees:
    if employee['department'] in departments:
        departments[employee['department']].append(employee['name'])
    else:
        departments[employee['department']]=[employee['name']]
    

print(departments)
    
