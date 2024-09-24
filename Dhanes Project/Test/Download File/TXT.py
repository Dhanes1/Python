def create_and_download_text_file(file_content, file_name):
    try:
        with open(file_name, 'w') as file:
            file.write(file_content)
        print("File created and downloaded successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
text_content = """This is a sample text file.
You can write whatever content you want here.
This content will be saved to a text file."""
file_name = "sample_text_file.txt"

create_and_download_text_file(text_content, file_name)
