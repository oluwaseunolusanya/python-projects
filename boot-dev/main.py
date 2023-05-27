with open("/root/workspace/github.com/oluwaseunolusanya/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)

count = 0

for word in file_contents.split():
    count += 1

print(count)

#Function below takes a string and returns number of times each character appears in the string.
def character_counter(text):
    return_value = {}
    text_processed = text.lower()
    for character in text_processed:
        if character not in return_value.keys():
            return_value[f"{character}"] = 1
        else:
            return_value[f"{character}"] += 1
    return return_value

print(character_counter(file_contents))

character_count = character_counter(file_contents)
for k,v in character_count.items():
    if k.isalpha():
        print(f"The '{k}' character was found {v} times.")
