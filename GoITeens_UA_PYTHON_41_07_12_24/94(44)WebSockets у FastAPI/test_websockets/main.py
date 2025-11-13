import logging
from typing import Dict, Optional
from datetime import datetime

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, Path
import uvicorn


app = FastAPI()
logging.basicConfig(level=logging.INFO)

CLIENTS: Dict[str, WebSocket] = {}


@app.websocket("/ws/{name}/")
async def test_websocket(websocket: WebSocket, name: str = Path(...), token: Optional[str] = Query(None)):
    if name not in CLIENTS and token == "Bearer 123456":
        await websocket.accept()
        CLIENTS[name] = websocket
        for ws in CLIENTS.values():
            await ws.send_text(f"{datetime.now()}: '{name}' приєднався до чату.")

    try:
        while True:
            message = await websocket.receive_text()
            if ": " in message:
                client, message = message.split(": ")
                if client in CLIENTS:
                    await CLIENTS[client].send_text(f"{name}: {message}")
                    logging.info(f"Отримали повідомлення: '{message}'")
                elif client == "all":
                    for ws in CLIENTS.values():
                        await ws.send_text(f"{name}: {message}")
                else:
                    await websocket.send_text(f"Клієнта з ім'ям '{name}' не знайдено.")
            else:
                await websocket.send_text("Повідомлення повинно бути у такому форматі: 'name: message'")

    except WebSocketDisconnect:
        logging.info("З'єднання закрито")
    except Exception as error:
        logging.warning(f"Помилка: {error}")
    finally:
        await websocket.close()
        del CLIENTS[name]
        logging.info("Сесія завершена")
        for ws in CLIENTS.values():
            await ws.send_text(f"{datetime.now()}: '{name}' від'єднався.")


if __name__ == "__main__":
    uvicorn.run("main:app")
