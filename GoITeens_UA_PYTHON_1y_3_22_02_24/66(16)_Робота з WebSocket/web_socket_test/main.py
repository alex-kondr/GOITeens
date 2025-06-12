from typing import List, Dict

from fastapi import FastAPI, WebSocket, Path, Query, HTTPException, status, WebSocketDisconnect
import uvicorn


app = FastAPI()
connections: Dict[str, WebSocket] = {}


@app.websocket("/web-socket-test/{user_name}/")
async def web_socket_server(websocket: WebSocket, user_name: str = Path(...), token: str = Query(...)):
    if token != "super_secret":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    await websocket.accept()
    connections.update(
        {user_name: websocket}
    )

    try:
        while True:
            data = await websocket.receive_text()
            user_name_new, text = data.split(": ", 1)

            if user_name_new == "Всі":
                for conn in connections.values():
                    if conn != websocket:
                        await conn.send_text(f"{user_name}: {text}")
            else:
                websocket_new = connections.get(user_name_new)
                if not websocket_new:
                    await websocket.send_text(f"Користувач '{user_name_new}' OFFLINE")
                await websocket_new.send_text(f"{user_name}: {text}")

    except Exception:
        del connections[websocket]
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
