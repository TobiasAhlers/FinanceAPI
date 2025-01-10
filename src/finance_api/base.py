from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data_model_router import DataModelRouter
from sqlmodel import SQLModel

from .database import *


class FinanceAPI(FastAPI):
    def __init__(self):
        super().__init__(
            title="Finance API",
            version="0.1.0",
            description="API for finance related operations",
        )
        SQLModel.metadata.create_all(ENGINE, checkfirst=True)

        self.include_router(DataModelRouter(Transaction))
        self.include_router(DataModelRouter(Account))
        self.include_router(DataModelRouter(Category))

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @classmethod
    def create_tables(cls) -> None:
        SQLModel.metadata.create_all(ENGINE, checkfirst=True)


API = FinanceAPI()
