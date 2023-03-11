from flask import Flask
import redis
import os
from dotenv import dotenv_values
config = dotenv_values(".env")

global redisConnection

# Create a Flask app
app = Flask(__name__)

# Redis connection
redisConnection = redis.Redis(host='redis', port=config['REDIS_PORT'], db=0)

# Import the routes
import routes

# Start the Flask app
if __name__ == '__main__':
    port = os.getenv("PORT",5000)
    app.run(debug=True,port=port,host='0.0.0.0')