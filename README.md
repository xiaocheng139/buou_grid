# Cryptocurrency Grid Trading Bot

This project contains a collection of Python scripts for implementing grid trading strategies on various cryptocurrency exchanges.

## Description

Grid trading is a trading strategy that seeks to profit from market volatility by placing a series of buy and sell orders at predefined intervals around a set price. This bot automates this process.

The project currently includes scripts for the following exchanges:

*   **188**
*   **Binance**
*   **OKX**

The primary trading pair configured in the existing scripts is XRP, but they can be adapted for other trading pairs. The bot also uses Telegram to send notifications about its status and trades.

## Prerequisites

Before you begin, ensure you have Python 3 installed on your system.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each script is designed to be run as a standalone bot for a specific exchange.

1.  **Configuration:**
    *   Open the script you want to use (e.g., `grid_BN_XRP.py` for Binance).
    *   Inside the script, you will need to configure your API keys for the respective exchange.
    *   You will also need to provide your Telegram bot token and chat ID for notifications.

2.  **Running the bot:**
    ```bash
    python <script_name>.py
    ```
    For example, to run the Binance XRP grid bot:
    ```bash
    python grid_BN_XRP.py
    ```

## Disclaimer

Trading cryptocurrencies involves significant risk. This bot is provided as-is, and the user assumes all responsibility for any financial losses. It is highly recommended to test the bot with small amounts or in a paper trading environment before deploying it with significant capital.