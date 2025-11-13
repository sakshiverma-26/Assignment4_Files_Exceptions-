user_data = input("Enter some data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_data + "\n")

print("Data written to output.txt successfully!")
more_data = input("Enter more data to append: ")

with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("Additional data appended successfully!")

print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
