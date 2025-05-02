from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Nifty 50 stock names dictionary
stock_names = {
    "ADANIENT": "Adani Enterprises Ltd.",
    "ADANIPORTS": "Adani Ports and Special Economic Zone Ltd.",
    "APOLLOHOSP": "Apollo Hospitals Enterprise Ltd.",
    "ASIANPAINT": "Asian Paints Ltd.",
    "AXISBANK": "Axis Bank Ltd.",
    "BAJAJ-AUTO": "Bajaj Auto Ltd.",
    "BAJFINANCE": "Bajaj Finance Ltd.",
    "BAJAJFINSV": "Bajaj Finserv Ltd.",
    "BPCL": "Bharat Petroleum Corporation Ltd.",
    "BHARTIARTL": "Bharti Airtel Ltd.",
    "BRITANNIA": "Britannia Industries Ltd.",
    "CIPLA": "Cipla Ltd.",
    "COALINDIA": "Coal India Ltd.",
    "DIVISLAB": "Divis Laboratories Ltd.",
    "DRREDDY": "Dr. Reddy's Laboratories Ltd.",
    "EICHERMOT": "Eicher Motors Ltd.",
    "GRASIM": "Grasim Industries Ltd.",
    "HDFC": "Housing Development Finance Corporation Ltd.",
    "HDFCBANK": "HDFC Bank Ltd.",
    "HDFCLIFE": "HDFC Life Insurance Company Ltd.",
    "HEROMOTOCO": "Hero MotoCorp Ltd.",
    "HINDALCO": "Hindalco Industries Ltd.",
    "HINDUNILVR": "Hindustan Unilever Ltd.",
    "ICICIBANK": "ICICI Bank Ltd.",
    "INDUSINDBK": "IndusInd Bank Ltd.",
    "INFY": "Infosys Ltd.",
    "ITC": "ITC Ltd.",
    "JSWSTEEL": "JSW Steel Ltd.",
    "KOTAKBANK": "Kotak Mahindra Bank Ltd.",
    "LT": "Larsen & Toubro Ltd.",
    "M&M": "Mahindra & Mahindra Ltd.",
    "MARUTI": "Maruti Suzuki India Ltd.",
    "NESTLEIND": "Nestlé India Ltd.",
    "NTPC": "NTPC Ltd.",
    "ONGC": "Oil and Natural Gas Corporation Ltd.",
    "POWERGRID": "Power Grid Corporation of India Ltd.",
    "RELIANCE": "Reliance Industries Ltd.",
    "SBILIFE": "SBI Life Insurance Company Ltd.",
    "SBIN": "State Bank of India",
    "SUNPHARMA": "Sun Pharmaceutical Industries Ltd.",
    "TATACONSUM": "Tata Consumer Products Ltd.",
    "TATAMOTORS": "Tata Motors Ltd.",
    "TATASTEEL": "Tata Steel Ltd.",
    "TCS": "Tata Consultancy Services Ltd.",
    "TECHM": "Tech Mahindra Ltd.",
    "TITAN": "Titan Company Ltd.",
    "ULTRACEMCO": "UltraTech Cement Ltd.",
    "UPL": "UPL Ltd.",
    "WIPRO": "Wipro Ltd."
}

# Function to simulate fetching news
def fetch_news_for_stock(stock_name):
    headlines = [
        f"{stock_name} reports positive growth",
        f"Concerns over {stock_name} management decisions",
        f"{stock_name} stock rallies on market sentiment",
        f"Investors cautious as {stock_name} stock drops",
    ]
    return headlines

# News sentiment analysis function
def analyze_news_sentiment(stock_name):
    headlines = fetch_news_for_stock(stock_name)
    positive_words = ["buy", "up", "gain", "positive", "strong", "rally", "surge"]
    negative_words = ["sell", "down", "loss", "negative", "weak", "drop", "decline"]
    positive_count, negative_count = 0, 0

    for headline in headlines:
        for word in headline.lower().split():
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1

    total_count = positive_count + negative_count
    sentiment_score = (positive_count - negative_count) / total_count if total_count > 0 else 0
    sentiment_score += random.uniform(-0.3, 0.3)
    return max(min(sentiment_score, 1), -1)

# Social media sentiment analysis (simulated)
def analyze_social_media_sentiment(stock_name):
    return random.uniform(-1, 1)

# Overall stock sentiment function
def analyze_stock_sentiment(stock_name):
    news_sentiment = analyze_news_sentiment(stock_name)
    social_media_sentiment = analyze_social_media_sentiment(stock_name)
    overall_sentiment = (news_sentiment + social_media_sentiment) / 2

    if overall_sentiment > 0.5:
        recommendation = "Buy"
    elif overall_sentiment < -0.5:
        recommendation = "Sell"
    else:
        recommendation = "Hold"
    return overall_sentiment, recommendation

# Flask route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        stock_name = stock_names.get(ticker)

        if stock_name:
            sentiment_score, recommendation = analyze_stock_sentiment(stock_name)
            result = {
                "stock_name": stock_name,
                "sentiment_score": sentiment_score,
                "recommendation": recommendation
            }
        else:
            result = {"error": "Invalid stock ticker."}
    return render_template("index.html", result=result, stock_names=stock_names)

if __name__ == "__main__":
    app.run(debug=True)
