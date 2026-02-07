#!/bin/python

from src.utl.filters import (
    sma_crossover_filter,
    volume_filter,
    momentum_filter,
    rsi_filter,
)
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.trading.models import Asset
from datetime import datetime, timedelta
import pandas as pd
from typing import List, Dict, Any


def stock_filter_strategy(symbol, client):
    # Get historical data
    request = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame(1, TimeFrameUnit("Day")),
        start=datetime.now() - timedelta(days=365),
    )
    bars = client.get_stock_bars(request)
    df = bars.df

    # Handle MultiINdex data frames
    if isinstance(df.columns, pd.MultiIndex):
        df = df.droplevel(0, axis=1)

    # Check if the data frame is empty
    if df.empty or "close" not in df.columns:
        print(f"No data available for {symbol}")
        return None

    # Returns boolean values based off the given filters
    try:
        sma_fil = sma_crossover_filter(df)
        vol_fil = volume_filter(df)
        mom_fil = momentum_filter(df)
        rsi_fil = rsi_filter(df)
        score = sum([sma_fil, vol_fil, mom_fil, rsi_fil])
        buy = score >= 4
    except Exception as x:
        print(f"Caught Exception on symbol: {symbol}")
        print(x)
        return None

    return {
        "symbol": symbol,
        "price": df["close"].iloc[-1],
        "buy": buy,
        "score": score,
        "SMA": sma_fil,
        "VOL": vol_fil,
        "MOM": mom_fil,
        "RSI": rsi_fil,
    }


def stock_filter_strategy_batch(symbols: List[str], client) -> List[Dict[str, Any]]:
    """
    Process multiple symbols at once using batch API request

    Args:
        symbols: List of stock symbols to analyze
        client: Alpaca data client

    Returns:
        List of results for each symbol
    """
    # Single API call for ALL symbols
    request = StockBarsRequest(
        symbol_or_symbols=symbols,  # Pass list instead of single symbol
        timeframe=TimeFrame(1, TimeFrameUnit("Day")),
        start=datetime.now() - timedelta(days=365),
    )

    # Get data for all symbols at once
    bars = client.get_stock_bars(request)
    df_multi = bars.df  # This is a MultiIndex DataFrame

    results = []

    # Process each symbol from the MultiIndex DataFrame
    for symbol in symbols:
        try:
            # Extract data for this specific symbol
            if isinstance(df_multi.index, pd.MultiIndex):
                # MultiIndex format: index levels are (symbol, timestamp)
                df = df_multi.xs(symbol, level=0)
            else:
                # Fallback if single symbol
                df = df_multi

            # Check if we have data
            if df.empty or "close" not in df.columns:
                print(f"No data available for {symbol}")
                continue

            # Run filters
            sma_fil = sma_crossover_filter(df)
            vol_fil = volume_filter(df)
            mom_fil = momentum_filter(df)
            rsi_fil = rsi_filter(df)
            score = sum([sma_fil, vol_fil, mom_fil, rsi_fil])
            buy = score >= 4

            result = {
                "symbol": symbol,
                "price": float(df["close"].iloc[-1]),
                "buy": buy,
                "score": score,
                "SMA": sma_fil,
                "VOL": vol_fil,
                "MOM": mom_fil,
                "RSI": rsi_fil,
            }
            print(result)
            results.append(result)

        except KeyError:
            # Symbol not in the results (delisted, no data, etc.)
            print(f"Symbol {symbol} not found in batch results")
            continue
        except Exception as e:
            print(f"Error processing {symbol}: {e}")
            continue

    return results


def process_symbols_in_batches(all_symbols: List[str], client, batch_size: int = 100):
    """
    Process symbols in batches to avoid API limits and memory issues

    Args:
        all_symbols: Complete list of symbols to process
        client: Alpaca data client
        batch_size: Number of symbols per batch (Alpaca recommends max 100)

    Returns:
        List of all results
    """
    all_results = []

    # Split symbols into batches
    for i in range(0, len(all_symbols), batch_size):
        batch = all_symbols[i : i + batch_size]
        print(f"Processing batch {i // batch_size + 1}: {len(batch)} symbols")

        # Process this batch
        batch_results = stock_filter_strategy_batch(batch, client)
        all_results.extend(batch_results)

        print(f"Batch complete. Found {len(batch_results)} results")

    return all_results


if __name__ == "__main__":
    from src.factories.client_factory import create_client
    # from src.utl.watchlistJson import load_watchlist

    # Create Client
    acc, data_client = create_client()

    # Load Symbols
    raw_assets = acc.get_all_assets()
    if isinstance(raw_assets, list):
        assets: List[Asset] = raw_assets
        tradable_symbols = [
            asset.symbol
            for asset in assets
            if asset.tradable
            and asset.status == "active"
            and asset.asset_class == "us_equity"
        ]
    else:
        raise TypeError("Expected List[Asset] but recieved RawData or None")

    print(f"Total symbols to process: {len(tradable_symbols)}")

    all_results = process_symbols_in_batches(
        tradable_symbols, data_client, batch_size=100
    )

    # Filter for buy signals
    buy_candidates = [r for r in all_results if r["buy"]]

    print(f"\n{'=' * 60}")
    print(f"Total analyzed: {len(all_results)}")
    print(f"Buy signals: {len(buy_candidates)}")
    print(f"{'=' * 60}\n")
