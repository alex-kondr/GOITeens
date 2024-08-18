def print_message(text: str) -> str:
    print(text)


def print_message_2(text: str) -> str:
    print(text + "-> print-2")


def print_message_3(text: str) -> str:
    print(text + "-> print-3")

print(f"{__name__ = }")

if __name__ == "__main__":

    print_message("Hello-1")
    print_message_2("Hello-2")
    print_message_3("Hello-3")