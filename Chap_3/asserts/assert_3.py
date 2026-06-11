# ------------------------------ FUNCTION -------------------------------------
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    

# -------------------------------TEST ----------------------------------------------
print("Testing fact()...")
assert fact(1) == 1
assert fact(5) == 120
assert fact(10) == 3628800
print("✅ All tests passed!")