from sqlalchemy import Table, Column, ForeignKey

from app.models.base import Base


employee_position_assoc_table = Table(
    "employee_posititon_assoc_table",
    Base.metadata,
    Column(
        "position_id",
        ForeignKey("positions.id"),
        primary_key=True
    ),
    Column(
        "employee_id",
        ForeignKey("employee.id"),
        primary_key=True
    )
)

cabinet_position_assoc_table = Table(
    "cabinet_position_assoc_table",
    Base.metadata,
    Column(
        "cabinet_id",
        ForeignKey("cabinets.id"),
        primary_key=True
    ),
    Column(
        "position_id",
        ForeignKey("positions.id"),
        primary_key=True
    )
)
