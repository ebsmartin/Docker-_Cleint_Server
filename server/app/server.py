#!/usr/bin/env python3

# Basic python server that returns the square root of an int n.
# Listens on port 5000
# Returns “The square root of n is: [value of n^0.5]” when a request is received"

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
from flask import Flask
import sys

server = Flask(__name__)

# Create a route for the app.
# The route will return the square root of the value of n.
@server.route('/')
def squareroot():
    # Get the value of n from command line argument
    n = int(server.config.get("n"))
    if n >= 0:
        # Return the square root of n.
        square = (n**0.5)
        return f"The square root of {n} is: {square}"
    else: # add the imaginary part of the square root
        square = (n * -1)**0.5
        imaginary_square = str(square) + "j"
        return f"The square root of {n} is: {square}"

if __name__ == '__main__':
    # Get the value of n from command line argument
    server.config["n"] = sys.argv[1]

    # Create a server.
    # The server will listen on port 5000.
    print(f'Reading value {server.config["n"]}')
    server.run(host='0.0.0.0', port=5000)