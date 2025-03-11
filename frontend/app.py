import streamlit as st
import requests

# Streamlit app title
st.title("Resume Scoring System")

# File upload for resume
uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type=["pdf", "txt"])

# Input for job description
job_description = st.text_area("Enter the job description")

# Submit button
if st.button("Submit"):
    if uploaded_file and job_description:
        # Prepare the data for the request
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {"job_description": job_description}

        # Call the FastAPI endpoint
        try:
            response = requests.post("http://localhost:8000/upload_resume/", files=files, data=data)
            response.raise_for_status()  # Raise an error for bad responses
            result = response.json()

            # Display the result
            st.success(f"Resume file: {result['file_name']}")
            st.success(f"Score: {result['score']}")
        except requests.exceptions.HTTPError as err:
            st.error(f"Error: {err}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a resume and enter a job description.")
