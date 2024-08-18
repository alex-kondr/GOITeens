# D(X)= E(X^2) − μ^2

def avg(data: list) -> float:
    avg = sum(data) / len(data)
    return avg


def median(data: list) -> float:
    if len(data) % 2 != 0:
        index = len(data) // 2
        number = data[index-1]
    else:
        index = len(data) // 2
        number = (data[index] + data[index-1]) / 2
    return number