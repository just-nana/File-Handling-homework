def modify_file():
    import os

    # Prompt user for input filename
    input_filename = input("Enter the name of the input file: ").strip()

    # Check if file exists and is readable
    if not os.path.isfile(input_filename):
        print(f"❌ Error: File '{input_filename}' does not exist or cannot be read.")
        return

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
    except Exception as e:
        print(f"❌ Error reading the file: {e}")
        return

    # Modify content - you can change this logic as needed
    modified_content = content.upper()

    # Prompt for output filename
    output_filename = input("Enter the name of the output file: ").strip()

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        print(f"✅ Modified content has been saved to '{output_filename}'.")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")


if __name__ == "__main__":
    modify_file()
