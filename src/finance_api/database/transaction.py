from data_model_orm import DataModel, Field
from typing import Optional
from datetime import date

from .base import ENGINE


class Transaction(DataModel, table=True):
    """
    Transaction model representing a transaction entity in the system.

    Attributes:
        transaction_id (Optional[int]): The unique identifier for the transaction.
        account_id (int): The unique identifier for the account associated with the transaction.
        amount (float): The amount of the transaction.
        description (str): The description of the transaction.
    """
    __engine__ = ENGINE
    
    transaction_id: Optional[int] = Field(
        primary_key=True, description="The unique identifier for the transaction"
    )
    account_id: int = Field(description="The unique identifier for the account associated with the transaction", foreign_key="account.account_id")
    amount: float = Field(description="The amount of the transaction")
    booking_date: date = Field(description="The booking date of the transaction")
    description: Optional[str] = Field(description="The description of the transaction")
    note: Optional[str] = Field(description="A note for the transaction")
    category_id: Optional[int] = Field(description="The category id of the transaction", foreign_key="category.category_id")