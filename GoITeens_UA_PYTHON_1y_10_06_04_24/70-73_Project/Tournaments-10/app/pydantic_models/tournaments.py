from typing import Optional, List
from datetime import date

from pydantic import BaseModel, Field
from app.pydantic_models.teams import TeamModelResponse


class TournamentModel(BaseModel):
    name: str = Field(..., description="Назва турніру")
    description: Optional[str] = Field(None, description="Опис турніру")
    reg_days: int = Field(7, description="Кількість днів для реєстрації на турнір")


class TournamentModelResponse(BaseModel):
    id: str = Field(..., description="ID турніру")
    name: str = Field(..., description="Назва турніру")
    description: Optional[str] = Field(None, description="Опис турніру")
    start_day: date
    teams: List[TeamModelResponse] = Field([], description="Список команд учасників у турнірі")


class TeamTournamentModel(BaseModel):
    team_id: str = Field(..., description="ID команди")
    tournament_id: str = Field(..., description="ID турніру")


class ResultModel(TeamTournamentModel):
    result: float = Field(..., description="Результат команди у турнірі")


class ResultModelResponse(BaseModel):
    id: str
    team: TeamModelResponse
    tournament: TournamentModelResponse
    result: float
