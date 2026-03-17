from flask import Flask, request
import time
app = Flask(__name__)
@app.route("/compute", methods=["POST"])
def compute():
 data = request.json
  result = sum(range(data.get("n", 1000000)))
 time.sleep(2)
 return {"result": result, "message": "success"}
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=10000)
