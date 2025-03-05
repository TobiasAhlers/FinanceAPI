from data_model_orm import DataModel, Field
from typing import Optional
from pydantic import field_validator

from .base import ENGINE


class Account(DataModel, table=True):
    """
    Account model representing an account entity in the system.
    """

    __engine__ = ENGINE

    id: Optional[int] = Field(
        primary_key=True, description="The unique identifier for the account"
    )
    nickname: str = Field(description="The name of the account")
    type: str = Field(description="The type of the account", default="checking")
    balance: Optional[float] = Field(
        description="The balance of the account", default=0.0
    )

    @field_validator("type")
    @classmethod
    def validate_type(cls, v: any) -> str:
        if v not in ["checking", "savings", "cash", "asset", "liability", "other"]:
            raise ValueError(
                f"Expected type to be one of 'checking', 'savings', 'cash', 'asset', 'liability', or 'other', got {v}"
            )
        return v

