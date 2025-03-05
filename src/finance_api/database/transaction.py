from data_model_orm import DataModel, Field
from typing import Optional, Self
from pydantic import model_validator
import datetime

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
    account_id: int = Field(
        description="The unique identifier for the account associated with the transaction",
        foreign_key="account.id",
    )
    date: datetime.date = Field(description="The date of the transaction")
    payee: Optional[str] = Field(description="The payee of the transaction")
    category_id: Optional[int] = Field(
        description="The category id associated with the transaction",
        foreign_key="category.category_id",
    )
    memo: Optional[str] = Field(description="The memo of the transaction")
    outflow: Optional[float] = Field(
        description="The outflow of the transaction", default=None
    )
    inflow: Optional[float] = Field(
        description="The inflow of the transaction", default=None
    )

    @model_validator(mode="after")
    def validate_amount(self) -> Self:
        """Validates whether an amount is either an inflow or outflow."""

        if self.inflow is None and self.outflow is None:
            raise ValueError("An amount must be either an inflow or outflow")
        return self
