from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded airport database for demonstration purposes
airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    # Add more airports as needed
}


@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport_info = airport_database.get(icao_code.upper())

    if airport_info:
        result = {
            "ICAO": icao_code.upper(),
            "Name": airport_info["Name"],
            "Location": airport_info["Location"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
