# nested loops = The "inner loop" wil finish all of it's iterations before
#               finishing one iteration of the "outer loop"

rows = int(input("How many rows ?: "))
columns = int(input("How many columns ?: "))
symbols = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()
