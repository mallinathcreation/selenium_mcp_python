from agent import process_command

while True:
    command = input("🤖 Enter command: ")

    if command.lower() in ["exit", "quit"]:
        break

    result = process_command(command)
    print(result)