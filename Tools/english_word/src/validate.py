def words_validate(data):
    errors = []
    success = []
    data = data.splitlines()
    for word in data:
        if word:
            x = word.split(" ", 1)
            if len(x) != 2:
                errors.append(word)
            else:
                success.append([x[0], x[1]])
    return success, errors