from fastapi import FastAPI
from openai import AsyncAzureOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import date

load_dotenv()

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"


class requestBody(BaseModel):
    prompt: str

app = FastAPI()

# Employee data
employees = [
    {
        "employee_id": "1",
        "first_name": "Sarah",
        "last_name": "Johnson",
        "email": "sarah.johnson@company.com",
        "phone": "+1-555-0123",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 95000,
        "hire_date": date(2020, 3, 15),
        "manager_id": "5",
        "status": "Active",
        "skills": ["Python", "JavaScript", "React", "AWS"],
        "location": "New York, NY"
    },
    {
        "employee_id": "2",
        "first_name": "Michael",
        "last_name": "Chen",
        "email": "michael.chen@company.com",
        "phone": "+1-555-0124",
        "department": "Marketing",
        "position": "Marketing Manager",
        "salary": 78000,
        "hire_date": date(2019, 8, 22),
        "manager_id": "5",
        "status": "Active",
        "skills": ["Digital Marketing", "SEO", "Analytics", "Content Strategy"],
        "location": "San Francisco, CA"
    },
    {
        "employee_id": "3",
        "first_name": "Emily",
        "last_name": "Rodriguez",
        "email": "emily.rodriguez@company.com",
        "phone": "+1-555-0125",
        "department": "Human Resources",
        "position": "HR Specialist",
        "salary": 65000,
        "hire_date": date(2021, 1, 10),
        "manager_id": "5",
        "status": "Active",
        "skills": ["Recruitment", "Employee Relations", "Benefits Administration", "Training"],
        "location": "Chicago, IL"
    },
    {
        "employee_id": "4",
        "first_name": "David",
        "last_name": "Thompson",
        "email": "david.thompson@company.com",
        "phone": "+1-555-0126",
        "department": "Finance",
        "position": "Financial Analyst",
        "salary": 72000,
        "hire_date": date(2020, 11, 5),
        "manager_id": "5",
        "status": "Active",
        "skills": ["Financial Modeling", "Excel", "SQL", "Data Analysis"],
        "location": "Boston, MA"
    },
    {
        "employee_id": "5",
        "first_name": "Jessica",
        "last_name": "Williams",
        "email": "jessica.williams@company.com",
        "phone": "+1-555-0127",
        "department": "Engineering",
        "position": "DevOps Engineer",
        "salary": 88000,
        "hire_date": date(2019, 6, 18),
        "manager_id": "",
        "status": "Active",
        "skills": ["Docker", "Kubernetes", "CI/CD", "AWS", "Terraform"],
        "location": "Austin, TX"
    },
]

@app.post("/prompt")
async def read_haiku(request: requestBody):
    # Build employee data string from the employees list
    employee_data = "Employee Database:\n\n"
    for i, emp in enumerate(employees, 1):
        employee_data += f"""{i}. Employee ID: {emp['employee_id']}
   Name: {emp['first_name']} {emp['last_name']}
   Email: {emp['email']}
   Phone: {emp['phone']}
   Department: {emp['department']}
   Position: {emp['position']}
   Salary: ${emp['salary']:,}
   Hire Date: {emp['hire_date'].strftime('%B %d, %Y')}
   Manager ID: {emp['manager_id']}
   Status: {emp['status']}
   Skills: {', '.join(emp['skills'])}
   Location: {emp['location']}

"""
    
    openai_client = AsyncAzureOpenAI(
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_MODEL"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
    )
    agent = Agent(name="Assistant", instructions=f"""You are an employee information assistant. You can ONLY answer questions about the following employee data. Do not answer any questions outside this scope.

{employee_data}
Instructions:
- Answer ONLY questions about the employees listed above
- If asked about anything outside employee data, politely decline and state you can only provide information about employees
- Provide accurate information from the employee database
- Be helpful and professional in your responses""", model=OpenAIChatCompletionsModel(
        openai_client=openai_client,
        model=os.getenv("AZURE_OPENAI_MODEL")
    ))

    result = await Runner.run(starting_agent=agent, input=request.prompt)
    print(result.final_output)
    return {"message": result.final_output}
    
@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI!"}