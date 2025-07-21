from flask import Flask, jsonify, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route("/")
def home():
    return "국토부 API 연결 테스트"

@app.route("/api/trade", methods=["GET"])
def get_trade_data():
    service_key = urllib.parse.quote("CJMjU5znj4WL0Pfrb5Dqw0SpTnr1EfPL4IRwEhDGAsiPK1SsBV+ZOUUmp4fTT5N6UuagpqgehO35vGmpgTQ+EA==")  # 반드시 운영용 키
    lawd_cd = request.args.get("lawd_cd", "11110")
    deal_ymd = request.args.get("deal_ymd", "201512")
    
    url = f"https://apis.data.go.kr/1613000/RTMSDataSvcAptTradeDev/getRTMSDataSvcAptTradeDev"
    params = {
        "serviceKey": service_key,
        "LAWD_CD": lawd_cd,
        "DEAL_YMD": deal_ymd,
        "pageNo": "1",
        "numOfRows": "10"
    }

    res = requests.get(url, params=params)
    return res.text, res.status_code

if __name__ == "__main__":
    app.run(debug=True)
