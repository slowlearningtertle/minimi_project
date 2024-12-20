from flask import Flask, jsonify, request, render_template
from data_fetcher import fetch_stock_data
from data_processor import calculate_moving_average
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/load_data", methods=["GET"])
def load_data():
    # 요청 파라미터 받기
    ticker = request.args.get("ticker", "AAPL")
    start_date = request.args.get("start_date", "2023-01-01")
    end_date = request.args.get("end_date", "2023-12-01")
    
    # 데이터 처리
    data = fetch_stock_data(ticker, start_date, end_date)
    data = calculate_moving_average(data)
    
    # JSON 형태로 반환
    result = data.reset_index().to_dict(orient="records")
    return jsonify(result)








if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
