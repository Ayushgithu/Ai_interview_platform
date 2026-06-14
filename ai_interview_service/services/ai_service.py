import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key (ensure your .env has OPENAI_API_KEY=AIza...)
load_dotenv()
genai.configure(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the Gemini Flash model
model = genai.GenerativeModel('gemini-1.5-flash')

async def generate_questions_intro(job_title, job_description, resume_text):
    SYSTEM_PROMPT = f"""
        You are an AI interview expert who generates questions based on the candidate's job_title, job_description, and resume_text.
        Return the response strictly in JSON format with keys: "questions" (array), "introText" (string), "candidate_name" (string).
        ... (Insert your previous detailed Rules here) ...
    """
    
    # Using the native SDK for generation
    response = await model.generate_content_async(SYSTEM_PROMPT)
    
    # Cleaning JSON response (Gemini sometimes adds markdown backticks)
    text = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(text)

async def generate_report(answers=[]):
    SYSTEM_PROMPT = f"""
        You are an expert AI interviewer. Analyze these answers and return JSON with keys: "score" (string), "correct_answer" (number), "improvement_area" (array of strings).
        ... (Insert your previous detailed Rules here) ...
        Input: {answers}
    """
    
    response = await model.generate_content_async(SYSTEM_PROMPT)
    
    text = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(text)