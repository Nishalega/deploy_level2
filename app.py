from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            submitted_json = request.form.get("json_data")
            return jsonify(submitted_json)
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
