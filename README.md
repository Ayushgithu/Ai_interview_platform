# 🤖 AI Interview Platform

An AI-powered interview preparation platform that helps users practice and improve their interview skills through intelligent question generation, real-time interactions, and automated evaluation.

---

## 🚀 Tech Stack

This project is built using the following technologies:

- **Backend:** FastAPI (Python)
- **Frontend:** ReactJS
- **AI Engine:** OpenAI
- **Containerization:** Docker & Docker Compose

---

## 🧠 Features

- The user shall be able to enter a job title, job description, and upload a resume.
- The user shall be able to start the interview after providing the required information.
- The system shall analyze the resume, job title, and job description to generate personalized interview questions based on:
  - Relevant skills
  - Years of experience
  - Job role requirements
- The AI bot shall ask interview questions one at a time.
- The user shall be able to answer a question or skip a question.
- Once all questions have been asked or the user ends the interview manually, the system shall generate a detailed interview feedback report, including:
  - Performance evaluation
  - Strengths and improvement areas
  - Overall interview summary

---

## 🐳 Prerequisites

Before running the application, make sure you have the following installed:

- Python 3+
- NodeJS
- Docker (Optional)

---

## Set Environment Variables

```bash
OPENAI_API_KEY=your_api_key_here
```

## ▶️ Run the Application

To start the application using docker, run the following command from the project root directory:

```bash
docker compose up -d
```

**OR** To start the application manually

- Start Backend

```bash
cd ai_interview_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

- Start Frontend

```bash
cd ai_interview_frontend
npm install
npm start
```

## 🌐 Access the Application

FastAPI Swagger Docs:

```bash
👉 http://localhost:8000/docs
```

Frontend (React UI):

```bash
👉 http://localhost:3000/
```

## 🤙 Connect Community

💬 Join the LoopKaka Discord Community!
Got questions, doubts, or want to discuss topics from my videos?
Join our friendly Discord server to connect, learn, and grow together 👉 [https://discord.gg/BZwkqTsbND](https://discord.gg/BZwkqTsbND)
