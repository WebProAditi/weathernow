from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'WeatherNow API is running!'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    data = {
        "city": city,
        "temperature": "26°C",
        "description": "Partly cloudy"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
