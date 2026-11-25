from flask import Flask, render_template, request, jsonify
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from security_engine import (
    Traffic,
    inspect_firewall,
    detect_intrusion,
    scan_file_content,
    check_email_authentication
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/firewall", methods=["POST"])
def firewall_check():
    data = request.get_json()

    traffic = Traffic(
        source_zone=data.get("source", "INTERNET"),
        destination_zone=data.get("destination", "INTERNAL"),
        protocol=data.get("protocol", "TCP"),
        destination_port=int(data.get("port", 22)),
        application_data=data.get("payload", "")
    )

    return jsonify(inspect_firewall(traffic))


@app.route("/api/intrusion", methods=["POST"])
def intrusion_check():
    data = request.get_json()
    return jsonify({"alerts": detect_intrusion(data.get("ports", []))})


@app.route("/api/malware", methods=["POST"])
def malware_check():
    data = request.get_json()
    return jsonify(scan_file_content(data.get("content", "")))


@app.route("/api/email", methods=["POST"])
def email_check():
    data = request.get_json()

    return jsonify(check_email_authentication(
        data.get("spf", "FAIL"),
        data.get("dkim", "FAIL"),
        data.get("dmarc", "FAIL")
    ))


if __name__ == "__main__":
    app.run(debug=False)
