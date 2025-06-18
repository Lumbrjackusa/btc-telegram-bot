from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "7460766184:AAHXRMGq4wMP1elkg1AcAvNb72WtC1VGsBM"  # Pega aquí tu token válido actual
CHAT_ID = "467302456"  # Tu chat ID

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.json
    if data:
        signal_type = data.get("type", "N/A")
        price = data.get("price", "N/A")
        symbol = data.get("symbol", "BTC/USDT")
        exchange = data.get("exchange", "Binance")

        msg = f"""🚨 Señal detectada en {symbol}
✅ Exchange: {exchange}
📈 Tipo: {signal_type}
💰 Precio: {price}"""

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": msg
        }

        response = requests.post(url, json=payload)
        print("🧠 Telegram response:", response.status_code, response.text)

        return "OK", 200
    return "No data", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
