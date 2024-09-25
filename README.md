# resume_scoring_system

A machine learning application designed to analyze candidates' resumes against job descriptions using the LLaMA model. This project allows recruiters to score and shortlist candidates based on keyword matches, making the hiring process more efficient and effective.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Created By](#created-by)

## Features
- **Resume Parsing**: Automatically extracts relevant information from resumes.
- **Keyword Matching**: Compares resumes to job descriptions and scores candidates based on keyword matches.
- **Scoring System**: Ranks candidates on a scale from 1 to 10 based on their suitability for the job.
- **User Interface**: A simple web interface for recruiters to upload resumes and view results.

## Technologies Used
- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB
- **Frontend**: Streamlit
- **Model**: LLaMA (Meta AI)

## System Requirements
- Python 3.8 or higher
- FastAPI
- MongoDB
- Streamlit
- Transformers library (for LLaMA)
- A cloud service (optional) for deploying LLaMA if not running locally

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/candidate-resume-analyzer.git
   cd candidate-resume-analyzer
