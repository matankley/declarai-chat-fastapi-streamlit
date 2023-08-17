import sys

from fastapi import FastAPI, APIRouter

from chat import SQLChat
from declarai.memory import FileMessageHistory

app = FastAPI(title="Hey")
router = APIRouter()



@router.post("/chat/submit/{chat_id}")
def submit_chat(chat_id: str, request: str):
    chat = SQLChat(chat_history=FileMessageHistory(file_path=chat_id))
    response = chat.send(request)
    return response


@router.get("/chat/history/{chat_id}")
def get_chat_history(chat_id: str):
    chat = SQLChat(chat_history=FileMessageHistory(file_path=chat_id))
    response = chat.conversation
    return response


app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn  # pylint: disable=import-outside-toplevel
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=1,
        use_colors=True,
    )

