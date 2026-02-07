#!/bin/python

import os
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient


def create_client(
    envAccKey: str = "ALPACA_KEY", envAccSecret="ALPACA_SECRET", paperBool: bool = True
):
    """
    Factory for creating an active session of the alpaca-py sdk.

    Args:
    paperBool - boolean: Is the account a paper trading, or real trading account?
    """
    apiKey = os.getenv(envAccKey)
    apiSecret = os.getenv(envAccSecret)
    acc = TradingClient(apiKey, apiSecret, paper=paperBool)
    dataClient = StockHistoricalDataClient(apiKey, apiSecret)

    return acc, dataClient


if __name__ == "__main__":
    acc, dataClient = create_client()
    print(acc.get_account())
