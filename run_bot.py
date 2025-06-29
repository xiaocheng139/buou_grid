#!/usr/bin/env python
"""
This is the main entry point for running a specific grid trading bot.

This script imports the necessary configuration and the bot class from the `src`
directory, instantiates the bot, and starts its execution.
"""

import asyncio
import sys
import os

# Add the src directory to the Python path to allow for absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.bot_okx import GridTradingBot
from config import (
    COIN_NAME,
    CONTRACT_TYPE,
    GRID_SPACING,
    INITIAL_QUANTITY,
    LEVERAGE,
    POSITION_THRESHOLD,
    POSITION_LIMIT,
    SYNC_TIME,
    ORDER_FIRST_TIME,
    OKX_CONFIG
)

async def main():
    """
    Initializes and runs the OKX grid trading bot.
    """
    print("Starting the OKX grid trading bot...")

    # Initialize the bot with settings from the config file
    bot = GridTradingBot(
        api_key=OKX_CONFIG["API_KEY"],
        api_secret=OKX_CONFIG["API_SECRET"],
        passphrase=OKX_CONFIG["PASSPHRASE"],
        coin_name=COIN_NAME,
        contract_type=CONTRACT_TYPE,
        grid_spacing=GRID_SPACING,
        initial_quantity=INITIAL_QUANTITY,
        leverage=LEVERAGE,
        position_threshold=POSITION_THRESHOLD,
        position_limit=POSITION_LIMIT,
        sync_time=SYNC_TIME,
        order_first_time=ORDER_FIRST_TIME,
        websocket_url=OKX_CONFIG["WEBSOCKET_URL"],
        websocket_private_url=OKX_CONFIG["WEBSOCKET_PRIVATE_URL"]
    )

    # Start the bot's main execution loop
    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
