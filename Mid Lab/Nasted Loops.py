data = {
    "user": {
        "name": "Raihan",
        "id": 123,
        "contact": {
            "email": ["rai@example.com", "abc@edu.com"],
            "phone": "555-1234"
        }
    },
    "items": [
        {"name": "Laptop", "price": 1200},
        {"name": "Keyboard", "price": 75}
    ]
}

print("User Name:", data["user"]["name"])
print("First Item Price:", data["items"][0]["price"])
print("User Email:", data["user"]["contact"]["email"][1])