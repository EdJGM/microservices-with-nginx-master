from flask import Flask
from flask_cors import CORS
from config import config

# Import Routes
from routes import Movie

app = Flask(__name__)

# Enable CORS

CORS(app, resources={"*": {"origins": "*"}})


def page_not_found(e):
    return "<h1> Not Found </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    # Register the error handler
    app.register_error_handler(404, page_not_found)
    
    # Run the app on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)