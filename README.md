# declarai-chat-fastapi-streamlit


## View the app
Visit http://localhost:8501/ to view the app

![img.png](img.png)


## Run with Docker

You can run the app with docker-compose.

This demo is using openai gpt-3.5 mode so make sure to add your openai token to **.env** file.

Go to .env file and add your openai token
```bash
DECLARAI_OPENAI_API_KEY = <your openai key> ###ENTER YOUR OPENAI KEY HERE
```

Then run the following command

```bash
docker-compose up -d
```

## Installation

If you prefer to run the app locally, you can install the dependencies with poetry

```bash
poetry install
```
or with pip

```bash
pip install -r requirements.txt
```

## Run

First run the fastapi server

```bash
export DECLARAI_OPENAI_API_KEY = <your openai token>
cd app
poetry run uvicorn main:app --reload
```
(replace poetry with python if you didn't use poetry)

Afterwards, run the streamlit app

```bash
poetry run streamlit run streamlit_app.py
```


