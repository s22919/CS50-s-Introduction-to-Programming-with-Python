def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

reptext = input("Type whatever: ")

print(convert(reptext))
