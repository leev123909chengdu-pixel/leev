from flask import Flask, request
import time
import os

app = Flask(__name__)

@app.route("/compute", methods=["POST"])
def compute():
    data = request.json
    result = sum(range(data.get("n", 1000000)))
    time.sleep(2)
    return {"result": result, "message": "success"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
