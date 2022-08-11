def most_recently_watched(movies):
    stack = []
    num = 1
    for movie in movies.split(","):
        stack.append(movie)
    result = ""
    while len(stack) > 0 and num < 6:
        result += (f"   {num}. {stack.pop()}\n" )
        num += 1
    return result

print("Your 5 Most Recently Watched Programs: ")
print(most_recently_watched("Beauty and the Beast, Sleeping Beauty, Cinderella, The Little Mermaid, Frozen, Moana"))