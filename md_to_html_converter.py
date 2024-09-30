import argparse
import markdown
import os


def display_welcome_message():
    print("Welcome to the Markdown to HTML Converter!")
    print("This script will help you convert your Markdown files to HTML format.")
    print("You can specify the input file, output file name, and output directory via command-line arguments.")
    print("If no arguments are provided, you will be prompted for input interactively.")
    print("Let's get started!\n")


def get_file_paths(args):
    if args.input_file:
        input_file = args.input_file.strip('"')
    else:
        input_file = input("Enter the path to the input Markdown file: ").strip('"')

    # Get the base name of the input file without extension
    base_name = os.path.basename(input_file)
    base_name_without_ext = os.path.splitext(base_name)[0]

    if args.same_name or (not args.output_file and input(
            "Do you want the output file to have the same name? (y/n): ").strip().lower() == 'y'):
        output_file_name = base_name_without_ext + '.html'
    else:
        output_file_name = args.output_file.strip('"') if args.output_file else input(
            "Enter the desired output HTML file name: ").strip('"')
        # Ensure the output file name ends with ".html"
        if not output_file_name.lower().endswith('.html'):
            output_file_name += '.html'

    if args.same_location or (not args.output_dir and input(
            "Do you want the output file to be in the same location as the input file? (y/n): ").strip().lower() == 'y'):
        output_dir = os.path.dirname(input_file)
    else:
        output_dir = args.output_dir.strip('"') if args.output_dir else input(
            "Enter the desired output directory: ").strip('"')

    # Create the full path for the output file
    output_file = os.path.join(output_dir, output_file_name)

    return input_file, output_file


def convert_md_to_html(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


def main():
    display_welcome_message()

    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML.')
    parser.add_argument('input_file', nargs='?', help='Path to the input Markdown file')
    parser.add_argument('--output_file', help='Desired output HTML file name', default='')
    parser.add_argument('--same_name', action='store_true',
                        help='Use the same name for the output file with .html extension')
    parser.add_argument('--same_location', action='store_true',
                        help='Save the output file in the same location as the input file')
    parser.add_argument('--output_dir', help='Directory to save the output HTML file')

    args = parser.parse_args()

    input_file, output_file = get_file_paths(args)
    convert_md_to_html(input_file, output_file)
    print(f"\nConversion complete! The HTML file has been saved as: {output_file}")


if __name__ == "__main__":
    main()
