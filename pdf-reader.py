import pyttsx3
import PyPDF2

def read_pdf_to_text(file_path):
    """
    Reads text from a PDF file and returns it as a string.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading the PDF: {e}")
        return None

def text_to_speech(text):
    """
    Converts text to speech using pyttsx3.
    """
    if not text:
        print("No text to read!")
        return

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 for male voice, 1 for female voice

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Get PDF file path from user
    # file_path = input("Enter the path to the PDF file: ").strip()
    file_path = "/Users/steven/Desktop/Extraordinary-Popular-Delusions-Mackay.pdf"

    # Read the text from the PDF
    pdf_text = read_pdf_to_text(file_path)

    if pdf_text:
        print("Starting to read the PDF aloud...")
        text_to_speech(pdf_text)
    else:
        print("No text found in the PDF or an error occurred.")
