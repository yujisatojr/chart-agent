from flask import Flask, request, jsonify, send_from_directory, redirect
from flask_cors import CORS
from helper_functions import generate_chart

app = Flask(__name__, static_folder='../client/build', static_url_path='')
CORS(app, supports_credentials=True)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return redirect('/')
    
@app.route('/generate_chart', methods=['GET'])
def get_chart():
    query = request.args.get('query')
    if query is None:
        return jsonify({"error": "Please provide a query."}), 404

    result = generate_chart(query)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
