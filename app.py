from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

WHITESPACE_PATTERN = r"[\s\u200B\u200C\u200D\uFEFF]+"

def count_chars_excluding_spaces(text: str, strip_zero_width: bool = True) -> int:
    if strip_zero_width:
        cleaned = re.sub(WHITESPACE_PATTERN, "", text, flags=re.UNICODE)
    else:
        cleaned = re.sub(r"\s+", "", text, flags=re.UNICODE)
    return len(cleaned)

@app.route("/")
def root():
    return "flask-charcount alive", 200

@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/charcount", methods=["GET", "POST"])
def charcount():
    if request.method == "GET":
        text = request.args.get("text", "")
        strip_zw = request.args.get("strip_zero_width", "true").lower() != "false"
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
        strip_zw = bool(data.get("strip_zero_width", True))

    count = count_chars_excluding_spaces(text, strip_zero_width=strip_zw)
    return jsonify({
        "char_count": count,
        "excluded": "whitespace" + ("+zero_width" if strip_zw else ""),
        "input_length": len(text),
    })
