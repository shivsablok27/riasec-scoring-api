# RIASEC Scoring API

A FastAPI-based application to calculate **Holland Code (RIASEC)** scores from user responses. This API is designed for a Final Year Project (FYP) to help users identify their vocational personality types.

## Features
- **Standard 48-Question Support**: Accepts responses for 48 standard RIASEC items.
- **Normalized Scoring**: Returns scores normalized between `0.0` and `1.0`.
- **Holland Code Calculation**: Automatically determines the top 3 personality types (e.g., "RIA").
- **Interactive Documentation**: Comes with built-in Swagger UI for easy testing.

## Project Structure
- `main.py`: The entry point of the API application.
- `schemas.py`: Pydantic models defining the input/output data structure.
- `scoring.py`: Core logic for calculating and normalizing scores.
- `test_main.py`: Unit tests to verify the API's correctness.

## How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access Documentation**
   Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Testing
Run the automated test suite to verify everything is working:
```bash
pytest test_main.py
```
