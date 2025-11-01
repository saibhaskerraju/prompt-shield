from fastapi import FastAPI
from openai import AsyncAzureOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from data.employee import get_all_employees

load_dotenv()

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"


class requestBody(BaseModel):
    prompt: str

app = FastAPI()

@app.post("/prompt")
async def read_haiku(request: requestBody):
    # Build employee data string from the imported employees list
    employee_data = "Employee Database:\n\n"
    for i, emp in enumerate(get_all_employees(), 1):
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