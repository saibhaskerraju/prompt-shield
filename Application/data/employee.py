from datetime import datetime, date
from typing import List, Dict, Any

employees = [
    {
        "employee_id": "EMP001",
        "first_name": "Sarah",
        "last_name": "Johnson",
        "email": "sarah.johnson@company.com",
        "phone": "+1-555-0123",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 95000,
        "hire_date": date(2020, 3, 15),
        "manager_id": "EMP010",
        "status": "Active",
        "skills": ["Python", "JavaScript", "React", "AWS"],
        "location": "New York, NY"
    },
    {
        "employee_id": "EMP002",
        "first_name": "Michael",
        "last_name": "Chen",
        "email": "michael.chen@company.com",
        "phone": "+1-555-0124",
        "department": "Marketing",
        "position": "Marketing Manager",
        "salary": 78000,
        "hire_date": date(2019, 8, 22),
        "manager_id": "EMP009",
        "status": "Active",
        "skills": ["Digital Marketing", "SEO", "Analytics", "Content Strategy"],
        "location": "San Francisco, CA"
    },
    {
        "employee_id": "EMP003",
        "first_name": "Emily",
        "last_name": "Rodriguez",
        "email": "emily.rodriguez@company.com",
        "phone": "+1-555-0125",
        "department": "Human Resources",
        "position": "HR Specialist",
        "salary": 65000,
        "hire_date": date(2021, 1, 10),
        "manager_id": "EMP008",
        "status": "Active",
        "skills": ["Recruitment", "Employee Relations", "Benefits Administration", "Training"],
        "location": "Chicago, IL"
    },
    {
        "employee_id": "EMP004",
        "first_name": "David",
        "last_name": "Thompson",
        "email": "david.thompson@company.com",
        "phone": "+1-555-0126",
        "department": "Finance",
        "position": "Financial Analyst",
        "salary": 72000,
        "hire_date": date(2020, 11, 5),
        "manager_id": "EMP007",
        "status": "Active",
        "skills": ["Financial Modeling", "Excel", "SQL", "Data Analysis"],
        "location": "Boston, MA"
    },
    {
        "employee_id": "EMP005",
        "first_name": "Jessica",
        "last_name": "Williams",
        "email": "jessica.williams@company.com",
        "phone": "+1-555-0127",
        "department": "Engineering",
        "position": "DevOps Engineer",
        "salary": 88000,
        "hire_date": date(2019, 6, 18),
        "manager_id": "EMP010",
        "status": "Active",
        "skills": ["Docker", "Kubernetes", "CI/CD", "AWS", "Terraform"],
        "location": "Austin, TX"
    },
]

def get_all_employees() -> List[Dict[str, Any]]:
    """
    Returns all employee records
    """
    return employees