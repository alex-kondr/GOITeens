def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук:\n")
    reviews.append(review)
    return reviews


def find_repeated_chars(reviews: list) -> None:
    revs = " ".join(reviews)

    repeated_groups = set()
    for i in range(len(revs)):
        for j in range(i+1, len(revs)):
            slice = revs[i:j]
            if revs.count(slice) >= 2:
                repeated_groups.add(slice)

    print(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")
