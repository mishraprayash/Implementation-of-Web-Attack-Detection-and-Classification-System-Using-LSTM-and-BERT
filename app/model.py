# app/models.py

from sqlalchemy import Column, String, Text, Enum, DateTime, Boolean, Float
from datetime import datetime, timedelta, UTC
from db import Base


class RequestLog(Base):
    __tablename__ = "Activity"

    id = Column(String(191), primary_key=True)
    method = Column(String(191), nullable=False)
    endpoint = Column(Text, nullable=False)
    ip = Column(String(191), nullable=False)
    category = Column(Enum("NORMAL", "MALICIOUS"), nullable=False, default="NORMAL")
    attackType = Column(
        Enum(
            "NULL",
            "SQLI",
            "NOSQLI",
            "XSS",
            "SSRF",
            "CMDI",
            "LFI",
            "HTMLI",
            "CSSI",
            "XXE",
        ),
        nullable=False,
        default="NULL",
    )
    attackPayload = Column(Text)
    createdAt = Column(DateTime, nullable=False, default=datetime.now(UTC) + timedelta(seconds=20700))
    misClassified = Column(Boolean, nullable=False, default=False)
    predictionProbability = Column(Float, nullable=False, default=0.0)
    severity = Column(Enum("CRITICAL", "HIGH", "MEDIUM", "LOW", "NULL"))
