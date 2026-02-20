# Study-Bot---AI-Powered-Study-Assistant
**Study Bot** is a simple AI-powered chatbot designed to help students with academic topics. It accepts questions, remembers previous conversations, and responds with helpful, context-aware answers. This project demonstrates how AI assistants maintain context, interact with a database, and provide dynamic responses.
This version is a **minimal version** that echoes user messages, suitable for testing deployment on platforms like Render. Full functionality with MongoDB memory and AI-powered responses can be added later.

---

## Features

- FastAPI-based backend for handling requests.
- `/chat` endpoint to accept user messages and return responses.
- `/` root endpoint to verify the API is running.
- Simple, modular Python code suitable for deployment.
- Easily extendable to integrate MongoDB and AI models.

---

## Technologies Used

- **Python** – Programming language  
- **FastAPI** – Web framework for API creation  
- **Uvicorn** – ASGI server to run FastAPI  
- **Pydantic** – Data validation for request payloads  
- *(Optional for future upgrades)*: MongoDB, LangChain, Groq LLM

---
