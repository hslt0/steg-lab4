from encode import embed_message
from decode import extract_message
from view_wavs import plot_waveforms


def show_menu():
    print("=" * 20 + " Стеганографія у WAV (LSB) " + "=" * 20)
    print("1. Приховати повідомлення")
    print("2. Вилучити повідомлення")
    print("3. Порівняти графіки хвиль")
    print("4. Вихід")


def main():
    while True:
        show_menu()
        choice = input("\nОберіть опцію: ")

        if choice == "1":
            cover_wav = input("Шлях до оригіналу (WAV): ")
            stego_wav = input("Шлях для збереження стего (WAV): ")
            message = input("Повідомлення для вбудування: ")
            embed_message(cover_wav, stego_wav, message)

        elif choice == "2":
            stego_wav = input("Шлях до стего-файлу (WAV): ")
            print("\nВилучене повідомлення:")
            print(extract_message(stego_wav))

        elif choice == "3":
            original_wav = input("Шлях до оригіналу (WAV): ")
            stego_wav = input("Шлях до стего-файлу (WAV): ")
            plot_waveforms(original_wav, stego_wav)

        elif choice == "4":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

        print()


if __name__ == "__main__":
    main()
