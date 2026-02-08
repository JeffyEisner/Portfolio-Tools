#!/binbin/python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import pandas as pd


class TradingStrategy(ABC):
    """Base class for all trading strategies"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def analyze(self, symbol: str, df: pd.DataFrame) -> Optional[Dict[str, Any]]:
        """
        Analyze the given stock data and return a trading signal.

        Args:
            symbol: The stock symbol being analyzed
            df: A DataFrame containing historical stock data with columns like 'open', 'high', 'low', 'close', 'volume'

        Returns:
            Dictionaryu with analysis results or None
        """
        pass

    @abstractmethod
    def should_buy(self, analysis: Dict[str, Any]) -> bool:
        """
        Determine if we should buy based off a given strategies buy signals

        Args:
            Analys: Results from Analyze()

        Returns:
            True if buy signal, False otherwise
        """
        pass
