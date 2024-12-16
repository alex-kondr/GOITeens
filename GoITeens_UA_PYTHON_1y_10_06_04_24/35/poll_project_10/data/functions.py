def read_file(file: str = "data/answers.txt") -> list[str]:
    with open(file, "r", encoding="utf-8") as fh:
        file_r = fh.readlines()

    return file_r


def write_file(text: str, file: str = "data/answers.txt") -> None:
    with open(file, "a", encoding="utf-8") as fh:
        fh.write(text + "\n")
