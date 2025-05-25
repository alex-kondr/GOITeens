from typing import List, Dict

from fastapi import FastAPI, Query, Path, HTTPException, status
import uvicorn

from models import SpellModel, SpellModelResponse
import data


app = FastAPI()


@app.get("/spells/", status_code=status.HTTP_202_ACCEPTED, response_model=List[SpellModelResponse])
async def get_spells():
    return data.get_spells()


@app.post("/spells/", status_code=status.HTTP_201_CREATED)
async def add_spell(spell_model: SpellModel):
    spells = data.get_spells()
    spells.append(spell_model.model_dump())
    data.save_spells(spells)


@app.delete("/spells/{spell_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_spell(spell_id: int = Path(...)):
    spells = data.get_spells()
    spell = next((spell for spell in spells if spell.get("index") == spell_id), None)
    if not spell:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Таке заклинання відсутнє у базі даних")
    spells.remove(spell)
    data.save_spells(spells)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
