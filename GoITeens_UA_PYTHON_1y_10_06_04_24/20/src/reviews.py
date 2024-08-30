def add_review(reviews: list) -> list:
    review = input("Введіть свій відгук: ")
    reviews.append(review)
    print("\nВаш відгук додано до системи.")
    return reviews


def find_repeated_groups(reviews: list) -> None:
    reviews = " ".join(reviews).lower()

    repeated_chars = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            if reviews.count(reviews[i:j]) >= 2:
                repeated_chars.add(reviews[i:j])

    print(f"\nГрупи символів, які повторююьюся не менше 2-х разів:\n{repeated_chars}")


def show_reviews(reviews: list) -> None:
    for review in reviews:
        print(review)
