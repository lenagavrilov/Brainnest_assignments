'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

def ceasar_cipher():
    global abc

    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    command = get_command()

    encrypt_key = get_key()

    message = input('Enter the message to ' + command + '\n')

    output = do_encryption(command, encrypt_key, message)

    print(output)

def do_encryption(command, encrypt_key, message):
    new_message = ''

    for symbol in message:
        if symbol.upper() in abc:
            symbol_index = abc.find(symbol.upper())
            if command == 'encrypt':
                shifted_index = symbol_index + encrypt_key
            else:
                shifted_index = symbol_index - encrypt_key

            if shifted_index >= len(abc):
                shifted_index = shifted_index - len(abc)

            new_message += abc[shifted_index]
        else:
            new_message += symbol
    return  new_message




def get_command():
    command = ''
    while True:
        if command.lower() in ['encrypt', 'decrypt']:
            break;
        get_command = input('Do you want to (e)ncrypt or (d)ecrypt?')
        if get_command.lower() == 'e':
            command = 'encrypt'
        elif get_command.lower() == 'd':
            command = 'decrypt'
        else:
            print('No Valid Command')
    return command

def get_key():
    try:
        encrypt_key = int(input('Please enter the key (0 to 26) to use'))
        encrypt_key = encrypt_key % len(abc)

    except ValueError:
        print('You should enter numbers only')
    return encrypt_key


if __name__ == '__main__':
    ceasar_cipher()