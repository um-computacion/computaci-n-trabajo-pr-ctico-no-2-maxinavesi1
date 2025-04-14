def to_lowercase(text: str) -> str:
    return text.lower()

def remove_non_alphanumeric(text: str) -> str:
    return ''.join(char for char in text if char.isalnum())

def clean_text(text: str) -> str:
    lower = to_lowercase(text)
    return remove_non_alphanumeric(lower)

def is_symmetric(text: str) -> bool:
    return text == text[::-1]

def is_palindrome(text: str) -> bool:
    cleaned = clean_text(text)
    return is_symmetric(cleaned)

if __name__ == "__main__":
    try:
        while True:
            frase = input("Ingrese una palabra o frase: ")
            if is_palindrome(frase):
                print(f'"{frase}" es un palíndromo\n')
            else:
                print(f'"{frase}" no es un palíndromo\n')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
    