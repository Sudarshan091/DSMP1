company_data = [
    {"name": "Alice", "dept": "Engineering", "salary": 85000},
    {"name": "Bob", "dept": "Sales", "salary": 60000},
    {"name": "Charlie", "dept": "Engineering", "salary": 95000},
    {"name": "Diana", "dept": "HR", "salary": 70000},
    {"name": "Evan", "dept": "Sales", "salary": 65000}
]
def get_employees_by_dept(dataset,target_dept):
    found_employes=[]
    for employee in dataset:
        if employee["dept"]==target_dept:
            found_employes.append(employee['salary'])
    return found_employes
done=get_employees_by_dept(company_data,"Engineering")
print(done)

def calculate_average_salary(dataset,target_dept):
    total_salary=0
    employee_count=0
    for employee in dataset:
        if employee["dept"]==target_dept:
            total_salary+=employee["salary"]
            employee_count+=1
    if employee_count>0:
        average_salary=total_salary/employee_count
        return average_salary
    else:
        return None
average=calculate_average_salary(company_data,"Engineering")
print(average)
def get_top_earner(dataset,target_dept):
    highest_salary=0
    top_earner=""
    for employee in dataset:
        if employee['dept']==target_dept:
            if employee['salary']>highest_salary:
                highest_salary=employee['salary']
                top_earner=employee['name']
    return top_earner
top_earner=get_top_earner(company_data,"Engineering")
print(top_earner)
