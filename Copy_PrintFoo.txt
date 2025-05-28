def foo():
    return "Original"

foo = lambda: "Reassigned"

print(foo())