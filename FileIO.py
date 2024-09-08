s = "Something is written"
append_text = " More text appended."

# Write to the file
try:
    with open("text.txt", "w") as f:  # Open the file in write mode
        f.write(s)
except Exception as e:
    print("Error writing to file:", e)

# Append to the file
try:
    with open("text.txt", "a") as f:  # Open the file in append mode
        f.write(append_text)
except Exception as e:
    print("Error appending to file:", e)

# Read and print the file content
try:
    with open("text.txt", "r") as f:  # Open the file in read mode
        content = f.read()
        print("File content:", content)
except Exception as e:
    print("Error reading from file:", e)
