alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def do_this(original_text,shift_amount,encrypt_or_decrypt):
    over = ""
    if encrypt_or_decrypt == "decrypt":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shift_text = alphabet.index(letter) + shift_amount
            shift_text %= len(alphabet)
            over += alphabet[shift_text]
        else:
            over += letter
    print(f"The result is : {over}")
repeat = True
while repeat:
    direction = input("Type 'encrypt' to encrypt ,type decode to decrypt:\n").lower()
    text = input("Enter your message: \n").lower()
    shift = int(input("Type the shift numbers:\n"))
    do_this(original_text = text,shift_amount = shift,encrypt_or_decrypt = direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        repeat = False
        print("Goodbye") 
    
    