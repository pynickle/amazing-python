def words_validate(data):
    errors = []
    success = []
    data = data.splitlines()
    for word in data:
        if word:
            x = word.split()
            if len(x) != 3:
                errors.append(word)
            else:
                success.append([x[0], x[1], x[2]])
    return success, errors