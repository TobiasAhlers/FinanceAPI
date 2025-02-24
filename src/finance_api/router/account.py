from data_model_router import DataModelRouter

from ..database import Account, Transaction


class AccountRouter(DataModelRouter):
    def __init__(self) -> None:
        super().__init__(data_model=Account)

        @self.get("/balance", response_model=float, tags=["Account"])
        def get_balance(account_id: int) -> float:
            """
            Retrieve the balance of the account.

            account_id (int): The unique identifier for the account.
            """
            transactions = Transaction.get_all(account_id=account_id)
            balance = sum(transaction.amount for transaction in transactions)
            return balance
