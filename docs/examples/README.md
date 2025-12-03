# Python API Examples

This directory, contains three different approaches to building simple, single-file "Hello World" style API applications in Python: using **FastAPI**, Async **Flask**, and a **µ-Django** approach.

## The Concept: µ-Django (Lightweight Django)

The term µ-Django or "lightweight Django" refers to utilizing Django's core components—specifically its URL routing, request/response handling, and ORM capabilities—to build a functional web application within a single, minimal file structure, often without the full complexity of a traditional multi-app Django project setup.

This pattern is used for small service APIs, or educational purposes to demonstrate Django's power without boilerplate. For more details refer to the talks and materials presented by Maxim Danilov.

# Examples Overview

Each example file in this directory is a complete, runnable API service designed to run quickly and easily.

1. fastapi_main.py (FastAPI)

This file demonstrates the FastAPI framework.

Key Features: Uses standard Python type hints for data validation, automatic OpenAPI (Swagger/ReDoc) documentation generation, and runs on asynchronous Python (async/await).

How to Run (Requires uvicorn and fastapi):

uvicorn fastapi_main:app

Access at: http://127.0.0.1:8000/

2. flask_main.py (Async Flask)

This example utilizes Flask with asynchronous request handling.

How to Run (Requires flask):

flask --app flask_main run

Access at: http://127.0.0.1:5000/

3. uDjango.py (µ-Django)

This is a single-file implementation of a Lightweight Django project.

How to Run (Requires django and uvicorn):

uvicorn uDajngo:app

Access at: http://127.0.0.1:8000/