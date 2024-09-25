# # # from fastapi import FastAPI, UploadFile, File, Form
# # # from transformers import pipeline
# # # import pymongo
# # # from pymongo import MongoClient
# # # from PyPDF2 import PdfReader
# # # import os

# # # app = FastAPI()

# # # # MongoDB setup (replace with your own MongoDB URI)
# # # MONGO_URI = "mongodb://localhost:27017"  # Update this with your MongoDB connection string
# # # client = MongoClient(MONGO_URI)
# # # db = client['resume_db']  # Create or use an existing database
# # # collection = db['resumes']  # Create a 'resumes' collection

# # # # Replace LLaMA with distilgpt2 for text generation
# # # generator = pipeline('text-generation', model="distilgpt2")

# # # # Helper function to read text from PDF files
# # # def extract_text_from_pdf(file):
# # #     reader = PdfReader(file)
# # #     text = ""
# # #     for page in reader.pages:
# # #         text += page.extract_text()
# # #     return text

# # # @app.post("/upload_resume/")
# # # async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
# # #     # Check file extension for PDF
# # #     if file.filename.endswith('.pdf'):
# # #         resume_text = extract_text_from_pdf(file.file)
# # #     else:
# # #         resume_content = await file.read()
# # #         resume_text = resume_content.decode('utf-8')

# # #     # Use distilgpt2 to analyze the resume and compare it with the job description
# # #     prompt = f"Compare this resume: {resume_text} with this job description: {job_description}. Give a score from 1 to 10."
    
# # #     # Use max_new_tokens instead of max_length to avoid input length conflicts
# # #     generated_text = generator(prompt, max_new_tokens=50)

# # #     score = extract_score_from_text(generated_text[0]['generated_text'])

# # #     # Save resume and score to MongoDB
# # #     resume_data = {
# # #         "file_name": file.filename,
# # #         "resume_content": resume_text,
# # #         "job_description": job_description,
# # #         "score": score
# # #     }
# # #     collection.insert_one(resume_data)

# # #     return {"file_name": file.filename, "score": score}

# # # # Helper function to extract score from the generated text
# # # def extract_score_from_text(generated_text):
# # #     # Extracts a score from the generated text using regex (basic implementation)
# # #     import re
# # #     match = re.search(r'\b(\d+)\b', generated_text)
# # #     if match:
# # #         return int(match.group(1))
# # #     return 0


# # from fastapi import FastAPI, UploadFile, File, Form
# # from transformers import AutoTokenizer, AutoModelForCausalLM
# # import pymongo
# # from pymongo import MongoClient
# # from PyPDF2 import PdfReader
# # import torch
# # import re

# # app = FastAPI()

# # # MongoDB setup (replace with your own MongoDB URI)
# # MONGO_URI = "mongodb://localhost:27017"  # Update this with your MongoDB connection string
# # client = MongoClient(MONGO_URI)
# # db = client['resume_db']  # Create or use an existing database
# # collection = db['resumes']  # Create a 'resumes' collection

# # # Load the LLaMA model and tokenizer
# # tokenizer = AutoTokenizer.from_pretrained("mattshumer/Reflection-Llama-3.1-70B")
# # model = AutoModelForCausalLM.from_pretrained("mattshumer/Reflection-Llama-3.1-70B")

# # # Helper function to read text from PDF files
# # def extract_text_from_pdf(file):
# #     reader = PdfReader(file)
# #     text = ""
# #     for page in reader.pages:
# #         text += page.extract_text()
# #     return text

# # @app.post("/upload_resume/")
# # async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
# #     # Check file extension for PDF
# #     if file.filename.endswith('.pdf'):
# #         resume_text = extract_text_from_pdf(file.file)
# #     else:
# #         resume_content = await file.read()
# #         resume_text = resume_content.decode('utf-8')

# #     # Prepare the prompt for the model
# #     prompt = f"Compare this resume: {resume_text} with this job description: {job_description}. Give a score from 1 to 10."
    
# #     # Tokenize input
# #     inputs = tokenizer(prompt, return_tensors="pt")

# #     # Check the length of the input sequence
# #     if inputs['input_ids'].shape[1] > 1024:
# #         # Truncate the input to the last 1024 tokens
# #         inputs['input_ids'] = inputs['input_ids'][:, -1024:]

# #     # Generate output
# #     with torch.no_grad():
# #         outputs = model.generate(inputs['input_ids'], max_new_tokens=50, pad_token_id=tokenizer.eos_token_id)
    
# #     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# #     score = extract_score_from_text(generated_text)

# #     # Save resume and score to MongoDB
# #     resume_data = {
# #         "file_name": file.filename,
# #         "resume_content": resume_text,
# #         "job_description": job_description,
# #         "score": score
# #     }
# #     collection.insert_one(resume_data)

# #     return {"file_name": file.filename, "score": score}

# # # Helper function to extract score from the generated text
# # def extract_score_from_text(generated_text):
# #     # Extracts a score from the generated text using regex (basic implementation)
# #     match = re.search(r'\b(\d+)\b', generated_text)
# #     if match:
# #         return int(match.group(1))
# #     return 0

# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from transformers import pipeline
# from pymongo import MongoClient
# from PyPDF2 import PdfReader
# import re

# app = FastAPI()

# # MongoDB setup (replace with your own MongoDB URI)
# MONGO_URI = "mongodb://localhost:27017"  # Update this with your MongoDB connection string
# client = MongoClient(MONGO_URI)
# db = client['resume_db']  # Create or use an existing database
# collection = db['resumes']  # Create a 'resumes' collection

# # Load the DistilGPT-2 model for text generation
# generator = pipeline('text-generation', model='distilgpt2')

# # Helper function to read text from PDF files
# def extract_text_from_pdf(file):
#     reader = PdfReader(file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""  # Handle None case
#     return text.strip()

# @app.post("/upload_resume/")
# async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
#     try:
#         # Check file extension for PDF
#         if file.filename.endswith('.pdf'):
#             resume_text = extract_text_from_pdf(file.file)
#         else:
#             resume_content = await file.read()
#             resume_text = resume_content.decode('utf-8')

#         # Prepare the prompt for the model
#         prompt = f"Compare this resume: {resume_text} with this job description: {job_description}. Give a score from 1 to 10."
        
#         # Generate output
#         generated_text = generator(prompt, max_new_tokens=50, num_return_sequences=1)[0]['generated_text']
#         score = extract_score_from_text(generated_text)

#         # Save resume and score to MongoDB
#         resume_data = {
#             "file_name": file.filename,
#             "resume_content": resume_text,
#             "job_description": job_description,
#             "score": score
#         }
#         collection.insert_one(resume_data)

#         return {"file_name": file.filename, "score": score}

#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# # Helper function to extract score from the generated text
# def extract_score_from_text(generated_text):
#     # Extracts a score from the generated text using regex
#     match = re.search(r'\b(\d+)\b', generated_text)
#     if match:
#         return int(match.group(1))
#     return 0

# # To run the app, use the command:
# # uvicorn main:app --reload

# # uvicorn main:app --reload

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import pymongo
from pymongo import MongoClient
from PyPDF2 import PdfReader
import torch
import re

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup (replace with your own MongoDB URI)
MONGO_URI = "mongodb://localhost:27017"  
client = MongoClient(MONGO_URI)
db = client['resume_db']  
collection = db['resumes']  

# Load the DistilGPT-2 model for text generation
generator = pipeline('text-generation', model='distilgpt2')

# Helper function to read text from PDF files
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    # Check file extension for PDF
    if file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(file.file)
    else:
        resume_content = await file.read()
        resume_text = resume_content.decode('utf-8')

    # Prepare the prompt for the model
    prompt = f"Compare this resume: {resume_text} with this job description: {job_description}. Give a score from 1 to 10."
    
    # Generate output using max_new_tokens instead of max_length
    generated_text = generator(prompt, max_new_tokens=50, num_return_sequences=1)[0]['generated_text']

    score = extract_score_from_text(generated_text)

    # Save resume and score to MongoDB
    resume_data = {
        "file_name": file.filename,
        "resume_content": resume_text,
        "job_description": job_description,
        "score": score
    }
    collection.insert_one(resume_data)

    return {"file_name": file.filename, "score": score}

# Helper function to extract score from the generated text
def extract_score_from_text(generated_text):
    # Extracts a score from the generated text using regex (basic implementation)
    match = re.search(r'\b(\d+)\b', generated_text)
    if match:
        return int(match.group(1))
    return 0
