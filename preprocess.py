raw_text = "   User1: Hello!   \n\n\nUser2: Hi there!   \n   "

        # Step 2: Essential cleaning
cleaned_text = raw_text.strip()  # Remove leading/trailing whitespace
cleaned_text = '\n'.join(
    line.strip() for line in cleaned_text.split('\n') if line.strip()
)  # Remove empty lines and trim each line
print(cleaned_text)