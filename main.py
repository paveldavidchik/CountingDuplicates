def duplicate_count(text):
    return len({ch for ch in text.lower() if text.lower().count(ch) > 1})


print(duplicate_count('indivisibility'))
