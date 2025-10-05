# --- DEMO: Comprehensions ---
temp = [35, 40, 28, 32, 30]

farhen = [item*(9/5)+32 for item in temp]
print(f"First {farhen}")

farhen1 = [item*(9/5)+32 for item in temp if item % 2 == 0]
print(f"Second {farhen1}")

