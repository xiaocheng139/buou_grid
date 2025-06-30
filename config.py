"""
Central configuration file for the grid trading bots.
"""

# ==================== General Settings ====================
COIN_NAME = "XRP"  # Trading coin
CONTRACT_TYPE = "USDT"  # Margin contract type: USDT or USDC
GRID_SPACING = 0.004  # Grid spacing (e.g., 0.004 for 0.4%)
INITIAL_QUANTITY = 0.5  # Initial trade quantity in coin amount
LEVERAGE = 20  # Leverage multiplier
POSITION_THRESHOLD = 8  # Position hard limit to trigger defensive actions
POSITION_LIMIT = 2  # Position soft limit to accelerate profit-taking
SYNC_TIME = 60  # Interval in seconds to force sync account info
ORDER_FIRST_TIME = 10  # Delay in seconds before placing the first order

# ==================== Exchange Specific Settings ====================

# --- OKX Settings ---
OKX_CONFIG = {
    "API_KEY": "",  # Replace with your OKX API Key
    "API_SECRET": "",  # Replace with your OKX API Secret
    "PASSPHRASE": "",  # Replace with your OKX API Passphrase
    "WEBSOCKET_URL": "wss://ws.okx.com:8443/ws/v5/public",
    "WEBSOCKET_PRIVATE_URL": "wss://ws.okx.com:8443/ws/v5/private",
}

# --- Binance (BN) Settings ---
# Note: You will need to fill these in with your actual Binance configuration
BN_CONFIG = {
    "API_KEY": "",  # Replace with your Binance API Key
    "API_SECRET": "",  # Replace with your Binance API Secret
    # Binance doesn't require a passphrase
}

# --- 188 Settings ---
# Note: You will need to fill these in with your actual 188 configuration
GATEIO_CONFIG = {
    "API_KEY": "",  # Replace with your Gate.io API Key
    "API_SECRET": "",  # Replace with your Gate.io API Secret
}

# ==================== Telegram Notifications ====================
TELEGRAM_BOT_TOKEN = ""  # Your Telegram bot token
TELEGRAM_CHAT_ID = ""    # Your Telegram chat ID
