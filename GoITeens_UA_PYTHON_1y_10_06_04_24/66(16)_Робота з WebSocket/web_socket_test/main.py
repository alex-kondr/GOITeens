from typing import Dict

from fastapi import FastAPI, WebSocket, WebSocketException, Path
import uvicorn


app = FastAPI()
connections: Dict[str, WebSocket] = {}



@app.websocket("/ws/{username}/")
async def test_ws_server(websocket: WebSocket, username: str = Path(...)):
    await websocket.accept()
    connections.update({username: websocket})

    try:
        while True:
            data = await websocket.receive_text()
            print(f"{data = }")
            username_client, text = data.split(": ")

            websocket_client = connections.get(username_client)
            if username_client == "all":
                for ws in connections.values():
                    await ws.send_text(f"Повідомлення від {username}: {text}")

            elif not websocket_client:
                await websocket.send_text(f"Клієнт з username={username_client} не зареєстрований.")

            else:
                await websocket_client.send_text(f"Повідомлення від {username}: {text}")

    except WebSocketException:
        websocket.close()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
