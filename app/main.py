import json

from fastapi import FastAPI, APIRouter
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder
from app.chat import SQLChat, StreamingSQLChat
from declarai.memory import FileMessageHistory

app = FastAPI(title="Hey")
router = APIRouter()


@router.post("/chat/submit/{chat_id}")
def submit_chat(chat_id: str, request: str):
    chat = SQLChat(chat_history=FileMessageHistory(file_path=chat_id))
    response = chat.send(request)
    return response


@router.post("/chat/submit/{chat_id}/streaming")
def submit_chat_streaming(chat_id: str, request: str):
    chat = StreamingSQLChat(chat_history=FileMessageHistory(file_path=chat_id))
    response = chat.send(request)

    def stream():
        for llm_response in response:
            # Convert the LLMResponse to a JSON string
            data = json.dumps(jsonable_encoder(llm_response))
            yield data + "\n"  # Yielding as newline-separated JSON strings

    return StreamingResponse(stream(), media_type="text/event-stream")


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

