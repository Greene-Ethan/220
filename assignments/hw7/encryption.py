def encode(message,key):
    final_secret_message = ""
    for words in message:
        secret_message = ""
        for letters in words:
            converter = ord(letters)
            mes_add_three = converter + key
            back_to_words = chr(mes_add_three)
            secret_message = secret_message + back_to_words
        final_secret_message = final_secret_message + secret_message + "\n"
    return final_secret_message

def encode_better(message, key):
    loop_val = len(message) - len(key)
    new_key = key
    mod_num = 0
    for i in range(loop_val):
        new_key = new_key + key[mod_num % len(key)]
        mod_num = mod_num + 1
    seperated_letters = ""
    for letters in new_key:
        num_letts = str(ord(letters))
        seperated_letters = seperated_letters + " " + num_letts
    seperated_letters = seperated_letters[1:]
    seperated_letters = seperated_letters.split(" ")
    num = 0
    final_message = ""
    for letters in message:
        key_letts = eval(seperated_letters[num]) - 65
        message_letts = ord(letters) - 65
        add_letts = key_letts + message_letts
        mod_letts = add_letts % 58
        mod_letts = mod_letts + 65
        into_letts = chr(mod_letts)
        final_message = final_message + into_letts
        num = num + 1
    return final_message