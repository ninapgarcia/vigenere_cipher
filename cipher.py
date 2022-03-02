
import utils



print("\n-------------- CIPHER --------------\n")

message, key = utils.menu()

cipher_message = utils.cipherShift(message, key)
print("MENSAGEM CIFRADA: ", cipher_message)

decrypted_message = utils.decryptorShift(cipher_message, key)
print("MENSAGEM DECIFRADA: ", decrypted_message)
