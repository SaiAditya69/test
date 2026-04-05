# part3_api_files.py

import requests
from datetime import datetime

# ==========================================================
# Task 1 — File Read & Write
# ==========================================================

print("\n--- TASK 1: FILE OPERATIONS ---")

# Part A — Write
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# write file
with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")

print("File written successfully.")

# append extra lines
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help reuse code.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")

print("Lines appended.")

# Part B — Read
print("\nReading file:")

with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")

print("Total lines:", len(lines))

# keyword search
keyword = input("Enter keyword to search: ").lower()
found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")


# ==========================================================
# Helper — Logger
# ==========================================================

def log_error(context, error_type, message):
    with open("error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR in {context}: {error_type} — {message}\n")


# ==========================================================
# Task 2 — API Integration
# ==========================================================

print("\n--- TASK 2: API ---")

# Step 1 — Fetch products
try:
    url = "https://dummyjson.com/products?limit=20"
    response = requests.get(url, timeout=5)
    data = response.json()

    products = data["products"]

    print("\nID | Title | Category | Price | Rating")
    print("-" * 60)

    for p in products:
        print(f"{p['id']:<3}| {p['title'][:25]:<25}| {p['category']:<12}| ${p['price']:<8}| {p['rating']}")

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("fetch_products", "ConnectionError", "No connection")
except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("fetch_products", "Timeout", "Server too slow")
except Exception as e:
    print("Something went wrong:", e)
    log_error("fetch_products", "Exception", str(e))


# Step 2 — Filter & Sort
filtered = [p for p in products if p["rating"] >= 4.5]
filtered.sort(key=lambda x: x["price"], reverse=True)

print("\nFiltered Products (rating >= 4.5):")
for p in filtered:
    print(p["title"], "-", p["price"], "-", p["rating"])


# Step 3 — Category search
try:
    url = "https://dummyjson.com/products/category/laptops"
    res = requests.get(url, timeout=5)
    data = res.json()

    print("\nLaptops:")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except Exception as e:
    print("Error fetching laptops")
    log_error("fetch_laptops", "Exception", str(e))


# Step 4 — POST request
try:
    url = "https://dummyjson.com/products/add"
    payload = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    res = requests.post(url, json=payload, timeout=5)
    print("\nPOST Response:", res.json())

except Exception as e:
    print("POST failed")
    log_error("post_product", "Exception", str(e))


# ==========================================================
# Task 3 — Exception Handling
# ==========================================================

print("\n--- TASK 3: EXCEPTIONS ---")

# Part A
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Part B
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


# Part C — Robust API already handled above


# Part D — Input loop
while True:
    user_input = input("\nEnter product ID (1-100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue

    pid = int(user_input)

    if pid < 1 or pid > 100:
        print("Enter value between 1 and 100.")
        continue

    try:
        url = f"https://dummyjson.com/products/{pid}"
        res = requests.get(url, timeout=5)

        if res.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", "HTTPError", f"404 for ID {pid}")
        else:
            data = res.json()
            print(data["title"], "-", data["price"])

    except Exception as e:
        print("Error occurred")
        log_error("lookup_product", "Exception", str(e))


# ==========================================================
# Task 4 — Logging
# ==========================================================

print("\n--- TASK 4: LOGGING ---")

# Trigger connection error
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    log_error("test_connection", "ConnectionError", str(e))

# Trigger HTTP error manually
try:
    res = requests.get("https://dummyjson.com/products/999", timeout=5)
    if res.status_code != 200:
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")
except Exception as e:
    log_error("lookup_product", "Exception", str(e))

# print log file
print("\nError Log Contents:\n")

with open("error_log.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\nDone.")