from flask import Flask, request, jsonify
from flask_cors import CORS
import re, unicodedata

app = Flask(__name__)
CORS(app)ㅁfrom flask import Flask, request, jsonify
from flask_cors import CORS
import re, unicodedata

app = Flask(__name__)
CORS(app)

# 지시문과 동일한 공백 클래스
WS = r"[\t\n\v\f\r\u0020\u00A0\u1680\u2000-\u200A\u2028\u2029\u202F\u205F\u3000\uFEFF\u200B\u200C\u200D]+"

def normalize_and_count(text: str, strip_zero_width: bool = True) -> int:
    # 1) NFC 정규화
    s = unicodedata.normalize("NFC", text or "")
    # 2) 공백류 제거(옵션 무시: 프로젝트 규칙대로 항상 제거)
    s_no_ws = re.sub(WS, "", s, flags=re.UNICODE)
    # 3) 코드포인트 수(=파이썬 len)
    return len(s_no_ws)

@app.route("/")
def root():
    return jsonify({"status": "ok", "service": "charcount-api"}), 200

@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/charcount", methods=["GET", "POST"])
def charcount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")

    count = normalize_and_count(text)
    return jsonify({
        "char_count": count,
        "policy": "NFC + WS-set removal (project-spec)",
        "input_length": len(text)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# 지시문과 동일한 공백 클래스
WS = r"[\t\n\v\f\r\u0020\u00A0\u1680\u2000-\u200A\u2028\u2029\u202F\u205F\u3000\uFEFF\u200B\u200C\u200D]+"

def normalize_and_count(text: str, strip_zero_width: bool = True) -> int:
    # 1) NFC 정규화
    s = unicodedata.normalize("NFC", text or "")
    # 2) 공백류 제거(옵션 무시: 프로젝트 규칙대로 항상 제거)
    s_no_ws = re.sub(WS, "", s, flags=re.UNICODE)
    # 3) 코드포인트 수(=파이썬 len)
    return len(s_no_ws)

@app.route("/")
def root():
    return jsonify({"status": "ok", "service": "charcount-api"}), 200

@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/charcount", methods=["GET", "POST"])
def charcount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")

    count = normalize_and_count(text)
    return jsonify({
        "char_count": count,
        "policy": "NFC + WS-set removal (project-spec)",
        "input_length": len(text)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
