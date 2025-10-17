from fastapi import FastAPI, Query, HTTPException, status, Path
import uvicorn


app = FastAPI()

subjects = []


@app.get("/")
async def index():
    return dict(message="Hello world!")


@app.get("/name/")
async def get_name(
    name: str = Query(None, description="Введіть ім'я для відображення"),
    age: int = Query(..., description="Ваш вік")
):
    age = age / 10
    return dict(msg=f"Привіт, {name}, Ваш вік: {age}!")


@app.get("/calculate/")
async def calculate(
    op: str = Query(..., description="Введіть дію", examples=["+", "-"]),
    number1: float = Query(..., description="Введіть перше число"),
    number2: float = Query(..., description="Введіть друге число")
):
    if op == "+":
        result = number1 + number2
    elif op == "-":
        result = number1 - number2
    else:
        result = "Невідома дія"

    return {
        "message": f"Ви передали такі параметри: \n{op = }\n{number1 = }\n{number2 = }. Результат: {result}",
        "result": f"Результат: {number1} {op} {number2} = {result}",
    }


@app.post("/add_subject/")
async def add_subject(name: str = Query(..., description="Додати новий предмет")):
    if name not in subjects:
        subjects.append(name)
        return dict(message=f"Предмет '{name}' успішно додано")
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Предмет '{name}' вже є у списку")


@app.get("/subjects/")
async def get_subjects():
    return dict(subjects=subjects)


@app.get("/subjects/{index}/")
async def get_subject(index: int = Path(..., description="Індекс шкільного предмета")):
    if index >= len(subjects):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Предмета з індексом '{index}' не існує")

    return dict(subject=subjects[index])


@app.put("/subjects/{index}/")
async def update_subject(
    index: int = Path(..., description="Індекс предмета"),
    name: str = Query(..., description="Нова назва предмета")
):
    if index < 0 or index >= len(subjects):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Предмета з індексом '{index}' не існує")

    subjects[index] = name
    return dict(message=f"Предмет під індексом '{index}' успішно оновлено")


@app.delete("/subjects/{index}/")
async def remove_subject(index: int = Path(..., description="Індекс предмета для видалення")):
    if 0 <= index < len(subjects):
        subject = subjects.pop(index)
        return dict(message=f"Предмет '{subject}', який був під індексом '{index}' успішно видалено")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Предмета з індексом '{index}' не існує")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
