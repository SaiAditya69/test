# Part 3 — File I/O, APIs & Exception Handling

This project is part of my Python assignment (Part 3).
The goal was to build a small program that works with files, fetches data from an API, and handles errors properly.

---

## What I implemented

### 1. File Handling

* Created a file `python_notes.txt` and wrote 5 basic Python topics into it
* Appended 2 additional topics
* Read the file and printed each line with numbering
* Counted total lines in the file
* Added a keyword search feature (case-insensitive)

---

### 2. API Integration (DummyJSON)

* Fetched 20 products using a GET request
* Displayed product details in a formatted table
* Filtered products with rating ≥ 4.5
* Sorted them by price (descending)
* Fetched products from the **laptops** category
* Sent a POST request to simulate adding a product

---

### 3. Exception Handling

* Created a safe division function to handle divide-by-zero and type errors
* Built a safe file reader that handles missing files
* Wrapped all API calls in try-except blocks to handle:

  * Connection errors
  * Timeout errors
  * Unexpected errors
* Added input validation for product ID lookup

---

### 4. Logging System

* Implemented a simple error logger (`error_log.txt`)
* Logged errors with timestamps using `datetime`
* Logged both:

  * Connection errors (invalid URL)
  * HTTP errors (404 response)
* Printed log file contents at the end

---

## Files Included

* `part3_api_files.py` → main Python script
* `python_notes.txt` → generated file with notes
* `error_log.txt` → log file with error records

---

## How to Run

1. Install required library:

   ```
   pip install requests
   ```

2. Run the script:

   ```
   python part3_api_files.py
   ```

3. Provide inputs when prompted:

   * Enter a keyword for search
   * Type `quit` to exit the product lookup loop

---

## Notes

* All exceptions are handled to prevent crashes
* The API used is DummyJSON (free test API)
* Logging is implemented to simulate real-world error tracking

---

