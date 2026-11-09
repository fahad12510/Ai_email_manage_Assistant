from prompts import MESSAGE_TYPES, TONES
from groq_service import generate_message


def show_main_menu():
    print("\n" + "=" * 45)
    print("       AI EMAIL & MESSAGE ASSISTANT")
    print("=" * 45)
    print("1. Generate New Message")
    print("2. View Message Types")
    print("3. View Available Tones")
    print("4. Exit")


def show_options(title, options):
    print("\n" + title)
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")


def choose_option(title, options):
    while True:
        show_options(title, options)
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Invalid choice. Please select a valid number.")


def get_rough_message():
    while True:
        rough_message = input("\nEnter your rough message: ").strip()

        if rough_message:
            return rough_message

        print("Message cannot be empty. Please try again.")


def create_message():
    message_type = choose_option("SELECT MESSAGE TYPE", list(MESSAGE_TYPES.values()))
    tone = choose_option("SELECT WRITING TONE", list(TONES.values()))
    rough_message = get_rough_message()

    while True:
        print("\nConnecting to Groq AI...")
        try:
            generated_message = generate_message(
                message_type, tone, rough_message
            )

            print("\n" + "=" * 45)
            print("          AI GENERATED MESSAGE")
            print("=" * 45)
            print(generated_message)
            print("=" * 45)

        except ValueError as error:
            print(f"\nConfiguration Error: {error}")
            break
        except Exception as error:
            print(f"\nCould not generate the message: {error}")
            print("Please check your internet connection, API key, and model setting.")
            break

        print("\n1. Regenerate Message")
        print("2. Create Another Message")
        print("3. Return to Main Menu")
        next_choice = input("Enter your choice: ").strip()

        if next_choice == "1":
            # This calls Groq again and creates a fresh response.
            continue
        elif next_choice == "2":
            create_message()
            break
        elif next_choice == "3":
            break
        else:
            print("Invalid choice. Returning to the main menu.")
            break


def main():
    while True:
        show_main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_message()
        elif choice == "2":
            show_options("AVAILABLE MESSAGE TYPES", list(MESSAGE_TYPES.values()))
        elif choice == "3":
            show_options("AVAILABLE WRITING TONES", list(TONES.values()))
        elif choice == "4":
            print("\nThank you for using AI Email & Message Assistant!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
