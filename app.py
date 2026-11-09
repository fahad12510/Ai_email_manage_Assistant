
from flask import Flask, render_template, request
from prompts import MESSAGE_TYPES, TONES
from groq_service import generate_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    generated_message = ""
    error_message = ""
    selected_type = ""
    selected_tone = ""
    rough_message = ""

    if request.method == "POST":
        selected_type = request.form.get("message_type", "").strip()
        selected_tone = request.form.get("tone", "").strip()
        rough_message = request.form.get("rough_message", "").strip()

        if selected_type not in MESSAGE_TYPES.values():
            error_message = "Please select a valid message type."

        elif selected_tone not in TONES.values():
            error_message = "Please select a valid writing tone."

        elif not rough_message:
            error_message = "Please enter a rough message."

        else:
            try:
                generated_message = generate_message(
                    selected_type,
                    selected_tone,
                    rough_message
                )

            except ValueError as error:
                error_message = str(error)

            except Exception as error:
                app.logger.exception("GROQ API ERROR")
                error_message = (
                    "Unable to generate a message. "
                    "Please check the terminal for details."
                )

    return render_template(
        "index.html",
        message_types=list(MESSAGE_TYPES.values()),
        tones=list(TONES.values()),
        generated_message=generated_message,
        error_message=error_message,
        selected_type=selected_type,
        selected_tone=selected_tone,
        rough_message=rough_message,
    )


if __name__ == "__main__":
    app.run(debug=True)
