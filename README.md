# declarai-chat-fastapi-streamlit


## View the app
Visit http://localhost:8501/ to view the app

![img.png](img.png)


## Run with Docker

You can also run the app with docker-compose

```bash
docker-compose up -d
```

## Installation

```bash
poetry install
```
or 

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


