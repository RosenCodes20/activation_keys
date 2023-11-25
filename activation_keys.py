key = input()
command = input()
while command != "Generate":
    current_command = command.split(">>>")
    if current_command[0] == "Contains":
        substring = current_command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:

            print("Substring not found!")

    elif current_command[0] == "Flip":
        upper_or_lower = current_command[1]
        start_index = current_command[2]
        end_index = current_command[3]
        start_index, end_index = int(start_index), int(end_index)
        if upper_or_lower == "Upper":
            key = f"{key[:start_index]}{key[start_index:end_index].upper()}{key[end_index:]}"
        elif upper_or_lower == "Lower":
            key = f"{key[:start_index]}{key[start_index:end_index].lower()}{key[end_index:]}"

    elif current_command[0] == "Slice":
        start_index = current_command[1]
        end_index = current_command[2]
        start_index, end_index = int(start_index), int(end_index)
        key = f"{key[:start_index]}{key[end_index:]}"

    if current_command[0] != "Contains":
        print(key)
    command = input()

print(f"Your activation key is: {key}")
