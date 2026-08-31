from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/twin-data')
def twin_data():
    try:
        with open('twin_state.json') as f:
            return jsonify(json.load(f))
    except:
        return jsonify({"live_queue":0})

if __name__ == '__main__':
    app.run(debug=True, port=5000)