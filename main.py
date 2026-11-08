from prompts import MESSAGE_TYPES, TONES
from groq_service import generate_message


def show_options(title, options):
    print("\n" + title)
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")


def choose_option(title, options):
    show_options(title, options)
    while True:
        choice = input("Enter your choice: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]
        print(f"Invalid choice. Enter a number from 1 to {len(options)}.")


def create_message():
    message_type = choose_option("MESSAGE TYPES", MESSAGE_TYPES)
    tone = choose_option("AVAILABLE TONES", list(TONES.keys()))

    rough_message = input("\nEnter your rough message: ").strip()
    while not rough_message:
        print("Message cannot be empty. Please try again.")
        rough_message = input("Enter your rough message: ").strip()

    while True:
        print("\nGenerating your message...")
        try:
            result = generate_message(message_type, tone, rough_message)
            print("\n" + "=" * 45)
            print("             AI GENERATED MESSAGE")
            print("=" * 45)
            print(result)
            print("=" * 45)
        except ValueError as error:
            print(f"\nConfiguration error: {error}")
            return
        except Exception as error:
            print(f"\nCould not generate the message: {error}")
            print("Check your internet connection, API key, and model setting.")
            return

        print("\n1. Regenerate Message")
        print("2. Create Another Message")
        print("3. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            create_message()
            return
        elif choice == "3":
            return
        else:
            print("Invalid choice. Returning to the main menu.")
            return


def main():
    while True:
        print("\n" + "=" * 43)
        print("       AI EMAIL & MESSAGE ASSISTANT")
        print("=" * 43)
        print("1. Generate New Message")
        print("2. View Message Types")
        print("3. View Available Tones")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_message()
        elif choice == "2":
            show_options("MESSAGE TYPES", MESSAGE_TYPES)
        elif choice == "3":
            show_options("AVAILABLE TONES", list(TONES.keys()))
        elif choice == "4":
            print("Thank you for using AI Email & Message Assistant!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
