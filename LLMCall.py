from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

# Request body model
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response = model.generate_content(request.prompt)
    
    # Get the text content from Gemini response
    result = response.text.strip()
    
    return {"response": result}
