from uvicorn import run

from .base import FinanceAPI


if __name__ == "__main__":
    run(FinanceAPI())
