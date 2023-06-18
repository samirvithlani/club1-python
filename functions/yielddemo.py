def show():
    return 100
    return 200


def movie():
    yield "The Godfather"
    yield "The Shawshank Redemption"
    yield "The Dark Knight"
    yield "Star Wars"

print(show())

for i in movie():
    print(i)
