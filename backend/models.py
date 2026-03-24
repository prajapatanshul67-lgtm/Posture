from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: str = Field(index=True)
    type: str = Field(index=True)
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = Field(default=None, index=True)


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: str = Field(index=True)
    session_id: Optional[int] = Field(default=None, foreign_key="session.id")
    event_type: str = Field(index=True)
    payload_json: str
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)


class EventCreate(SQLModel):
    session_id: Optional[int] = None
    event_type: str
    payload: dict


class SessionCreate(SQLModel):
    type: str


class SessionRead(SQLModel):
    id: int
    client_id: str
    type: str
    started_at: datetime
    ended_at: Optional[datetime]


class SummaryStats(SQLModel):
    total_focus_minutes: float
    focus_sessions: int
    posture_events: int
    good_posture_ratio: float
    distance_events: int
    safe_distance_ratio: float

