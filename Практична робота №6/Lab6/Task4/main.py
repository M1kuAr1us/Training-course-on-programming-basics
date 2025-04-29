from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import os
from datetime import datetime

app = FastAPI()

# Підключення папки зі статичними файлами
app.mount("/static", StaticFiles(directory="static"), name="static")

# Список активних підключень
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

CHAT_HISTORY_FILE = "chat_history.json"

# Завантаження історії чату
def load_chat_history():
    if not os.path.exists(CHAT_HISTORY_FILE):
        return []
    with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Збереження історії чату
def save_chat_message(message: dict):
    history = load_chat_history()
    history.append(message)
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# WebSocket для чату
@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            username = data.get("username", "Анонім")
            message_text = data.get("message", "")
            timestamp = datetime.now().isoformat(timespec='seconds')
            message = {
                "username": username,
                "message": message_text,
                "timestamp": timestamp
            }
            save_chat_message(message)
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Ендпоінт для історії
@app.get("/history")
async def get_history():
    history = load_chat_history()
    return history

# Головна сторінка
@app.get("/")
async def get():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
