from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio
import time
from ui_config import UI_LITERALS

app = FastAPI(title="KHU AI Chat UI Framework")

# HTML Template & Static Files Mount
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str
    model: str = "qwen"

@app.get("/")
async def read_chat_ui(request: Request, lang: str = "ko"):
    # 지원하지 않는 언어일 경우 기본값 'ko'로 폴백
    if lang not in UI_LITERALS:
        lang = "ko"
        
    return templates.TemplateResponse("index.html", {
        "request": request,
        "literals": UI_LITERALS[lang],
        "current_lang": lang
    })

@app.post("/api/chat")
async def chat_interaction(req: ChatRequest):
    # TODO: 추후 Qwen, Gemini, OpenAI 실제 모델 연동
    # 현재는 더미 스트리밍/응답 처리 대체를 위해 Sleep 적용
    await asyncio.sleep(1.5)
    
    reply = f"[{req.model.upper()}] 교수님, 말씀하신 내용에 대한 답변입니다:\n\n\"{req.message}\"\n\n이 텍스트는 백엔드에서 반환된 테스트용 더미 응답입니다. 추후 실제 LLM API를 여기에 연결하시면 됩니다. UI 프레임워크가 정상 구동 중입니다."
    
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    # uvicorn main:app --reload 으로 실행
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
