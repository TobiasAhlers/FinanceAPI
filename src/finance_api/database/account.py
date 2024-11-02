from data_model_orm import DataModel, Field
from typing import Optional

from .base import ENGINE

class Account(DataModel, table=True):
    """
    Account model representing an account entity in the system.

    Attributes:
        account_id (Optional[int]): The unique identifier for the account.
        name (str): The name of the account.
    """
    __engine__ = ENGINE
    
    account_id: Optional[int] = Field(
        primary_key=True, description="The unique identifier for the account"
    )
    name: str = Field(description="The name of the account")