
import cipher_decipher

#--------------------------------------------------------------------------------
def menu():
    message = input("Enter your message: ")
    key = input("Enter your key: ")

    return message.upper(), key.upper()
#--------------------------------------------------------------------------------


message, key = menu()

print("\n-------------- CIPHER --------------\n")
cipher_message = cipher_decipher.cipherShift(message, key)
print("MENSAGEM CIFRADA: ", cipher_message)


print("\n------------ DECRYPTOR -------------\n")
decrypted_message = cipher_decipher.decipherShift(cipher_message, key)
print("MENSAGEM DECIFRADA: ", decrypted_message)
