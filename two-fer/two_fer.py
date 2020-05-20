def two_fer(*args):

    if len(args) == 1:
        name = str(args[0])
    else:
        name = ""

    if name:
        return f"One for {name}, one for me."
    else:
        return "One for you, one for me."

if __name__ == '__main__':
    two_fer('Xenu')
