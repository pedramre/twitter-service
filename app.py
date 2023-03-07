from flask import Flask
import redis
global redisConnection

# Create a Flask app
app = Flask(__name__)

# Redis connection
redisConnection = redis.Redis(host='localhost', port=6379, db=0)

# Import the routes
import routes

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)