from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "7460766184:AAGB5LeutaJwp1a3L85L9Dtnn1mJCCpbzg"
CHAT_ID = "467302456"

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.json
    if data:
        signal_type = data.get("type", "N/A")
        price = data.get("price", "N/A")
        symbol = data.get("symbol", "BTC/USDT")
        exchange = data.get("exchange", "Binance")

        msg = f"""📉 Señal detectada en {symbol}
✅ Exchange: {exchange}
📊 Tipo: {signal_type}
💰 Precio: {price}"""

        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": msg}
        )
        print("📨 Telegram response:", response.status_code, response.text)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
