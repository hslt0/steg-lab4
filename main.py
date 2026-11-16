from encode import embed_message_prng
from decode import extract_message_prng
from prng_utils import generate_key
from view_wavs import plot_waveforms


def get_embedding_key() -> str:
    while True:
        print("1. Ввести наявний ключ")
        print("2. Згенерувати новий ключ")
        choice = input("Оберіть спосіб отримання ключа: ")

        if choice == "1":
            key = input("Секретний ключ: ")
            if key:
                return key
            print("Ключ не може бути порожнім.")
        elif choice == "2":
            return generate_key()
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def show_menu():
    print("=" * 20 + " Стеганографія у WAV (LSB + PRNG) " + "=" * 20)
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
            key = get_embedding_key()
            embed_message_prng(cover_wav, stego_wav, message, key)
            print(f"Ваш секретний ключ: {key}")
            print("Збережіть ключ — він потрібен для вилучення повідомлення.")

        elif choice == "2":
            stego_wav = input("Шлях до стего-файлу (WAV): ")
            key = input("Секретний ключ: ")
            print("\nВилучене повідомлення:")
            print(extract_message_prng(stego_wav, key))

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
