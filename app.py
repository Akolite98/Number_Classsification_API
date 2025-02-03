from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS handling

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

# Function to check if a number is perfect
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to get a fun fact about a number
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        return response.json().get("text", "No fun fact found")
    except:
        return "Could not retrieve a fun fact"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    if number is None or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    number = int(number)
    
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")
    
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()
