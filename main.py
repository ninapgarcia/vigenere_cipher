
import cipher_decipher
import text_processing

#--------------------------------------------------------------------------------
def menu():
    message = input("Enter your message: ")
    key = input("Enter your key: ")

    return message.upper(), key.upper()
#--------------------------------------------------------------------------------


message, key = menu()
removed_chr_dict, new_message = text_processing.removingSpecialChr(message)


print("\n-------------- CIPHER --------------\n")
cipher_message = cipher_decipher.cipherShift(new_message, key)
cipher_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, cipher_message)
print("CIPHERED MESSAGE: ", cipher_message_w_chr)


print("\n------------ DECRYPTOR -------------\n")
decrypted_message = cipher_decipher.decipherShift(cipher_message, key)
decrypted_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, decrypted_message)
print("DECIPHERED MESSAGE: ", decrypted_message_w_chr)





