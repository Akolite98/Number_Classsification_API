# Number Classification API

## Overview
This project is a Flask-based REST API that classifies numbers based on their mathematical properties and provides a fun fact about them using the Numbers API.

## Features
- Determines if a number is **prime**, **perfect**, or **Armstrong**.
- Classifies numbers as **odd** or **even**.
- Computes the **sum of digits** of a number.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns responses in **JSON format**.
- Implements **error handling** for invalid inputs.
- Supports **CORS** for cross-origin requests.

## Technology Stack
- Python
- Flask
- Requests

## API Specification

### **Endpoint:**
```
GET /api/classify-number?number={number}
```

### **Request Parameters:**
- `number` (integer): The number to be classified.

### **Successful Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request):**
```json
{
    "number": "invalid_input",
    "error": true
}
```

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Akolite98/Number_Classsification_API
   
2. Navigate to the project directory:
   ```sh
   cd number-classification-api
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the API locally:
   ```sh
   python app.py
   ```
6. The API will be available at:
   ```
   http://127.0.0.1:5000/api/classify-number?number=371
   ```

## Deploymen
## License
This project is open-source and available under the **MIT License**.

---
