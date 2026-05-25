def main():
    print("=== Pomocnik haseł bankowych ===")
    print("Cześć! Podaj swoje hasło, a ja powiem Ci który numer jest przypisany do danej litery.\n")

    haslo = input("Wpisz swoje hasło: ")

    if len(haslo) < 4:
        print("Błąd: hasło musi mieć co najmniej 4 znaki!")
        return

    if len(haslo) > 32:
        print("Błąd: hasło nie może mieć więcej niż 32 znaki!")
        return

    print("\nNumery Twoich liter")
    print("=" * 30)
    for i, litera in enumerate(haslo, start=1):
        print(f"Litera {i} = {litera}")
    print("=" * 30)

if __name__ == "__main__":
    main()