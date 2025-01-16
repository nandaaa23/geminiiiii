from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyAd1kp_jQKJj3hreNozSjft3wET1a-AoPs"


@app.route('/generate_horoscope', methods=['POST'])
def generate_horoscope():
    zodiac = request.json.get('zodiac')
    if not zodiac:
        return jsonify({"error": "Zodiac sign is required!"}), 400

    prompt = f"Generate a horoscope for the zodiac sign {zodiac} for today."
    
    # API call to Gemini
    response = requests.post(
        
        headers={"Authorization": f"Bearer {AIzaSyAd1kp_jQKJj3hreNozSjft3wET1a-AoPs}"},
        json={"prompt": prompt, "max_tokens": 100}
    )

    if response.status_code == 200:
        horoscope = response.json().get("choices")[0].get("text").strip()
        return jsonify({"horoscope": horoscope})
    else:
        return jsonify({"error": "Failed to generate horoscope"}), 500

if __name__ == "__main__":
    app.run(debug=True)
