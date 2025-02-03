from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)


# Serve the HTML form on the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data received"}), 400

            key = data.get('key')  # Extract variable 1
            path = data.get('path')
            window_seconds = data.get('window_seconds')  # Extract variable 2

            # Debugging: Print received values
            print(f"Received key: {key}, path: {path}, window_seconds: {window_seconds}")

            result = subprocess.run(
                ['python', 'cms_edgeauth.py', "-k", key, "-u", path, "-w", '500'],  # Pass variables as arguments
                capture_output=True,
                text=True
            )
            print(result)
            return jsonify({"output": result.stdout, "error": result.stderr})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return render_template('index.html')  # This renders the HTML form

if __name__ == '__main__':
    app.run(debug=True)


#Received key: 4A2E8C0E6A4C2E8A0E4C2A8E0C4A2E8C, path: /api, window_seconds: 500