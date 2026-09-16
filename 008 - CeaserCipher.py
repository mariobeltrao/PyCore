import string

ALPHABET = string.ascii_lowercase
# O prefixo r faz o Python tratar barras invertidas como caracteres comuns.
LOGO = r"""
   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
  ██║     ███████║█████╗  ███████╗███████║██████╔╝
  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

             🔐  C I P H E R  🔐
       Encode • Shift • Decode • Discover

====================================================
        "Every letter hides a secret..."
====================================================
"""


def caesar(original_text, shift_amount, encode_or_decode):
    """Desloca letras de A a Z, preservando os demais caracteres."""
    if encode_or_decode not in ("encode", "decode"):
        raise ValueError("Choose 'encode' or 'decode'.")

    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Espaços, números, pontuação e letras acentuadas permanecem iguais.
        if letter not in string.ascii_letters:
            output_text += letter
            continue

        # O módulo (%) faz o índice voltar ao início após a letra Z.
        shifted_position = (ALPHABET.index(letter.lower()) + shift_amount) % len(ALPHABET)
        shifted_letter = ALPHABET[shifted_position]
        if letter.isupper():
            shifted_letter = shifted_letter.upper()
        output_text += shifted_letter

    return output_text


def read_choice(prompt, valid_choices):
    """Repete a pergunta até receber uma das opções permitidas."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid option! Please choose: {', '.join(valid_choices)}.")


def read_shift():
    """Solicita um número inteiro sem encerrar o programa em caso de erro."""
    while True:
        try:
            return int(input("Type the shift number:\n"))
        except ValueError:
            print("Invalid number! Please enter an integer.")


def main():
    print(LOGO)

    while True:
        direction = read_choice(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n",
            ("encode", "decode"),
        )
        text = input("Type your message:\n")
        shift = read_shift()

        result = caesar(text, shift, direction)
        print(f"Here is the {direction}d result: {result}")

        restart = read_choice(
            "Type 'yes' to go again. Otherwise, type 'no':\n",
            ("yes", "no"),
        )
        if restart == "no":
            print("Goodbye!")
            break


# Executa a interface somente quando este arquivo é iniciado diretamente.
if __name__ == "__main__":
    main()
