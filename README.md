# Markdown to HTML Converter

Welcome to the Markdown to HTML Converter! This script helps you convert your Markdown files to HTML format easily and efficiently.

## Features

- Convert Markdown files to HTML.
- Interactive mode for user-friendly input prompts.
- Command-line interface (CLI) for advanced users.
- Options to use the same name and/or location for the output file.

## Requirements

- Python 3.x
- `markdown` library

You can install the `markdown` library using pip:

```sh
pip install markdown
```

## Usage
### Interactive Mode
If you run the script without any arguments, it will prompt you for the necessary inputs interactively.

```bash
python md_to_html_CLI.py
```

### Command-Line Interface (CLI)
You can also provide arguments directly from the command line for a more streamlined experience.

#### Basic Usage
```bash
python md_to_html_CLI.py path/to/input.md
```

#### Specify Output File Name
```bash
python md_to_html_CLI.py path/to/input.md --output_file output.html
```

#### Use Same Name for Output File
```bash
python md_to_html_CLI.py path/to/input.md --same_name
```

#### Specify Output Directory
```bash
python md_to_html_CLI.py path/to/input.md --output_dir path/to/output/dir
```

#### Use Same Location for Output File
```bash
python md_to_html_CLI.py path/to/input.md --same_location
```

## Example
### Interactive Mode Example
```bash
python md_to_html_CLI.py
```

You will be prompted to enter:

1. The path to the input Markdown file.
2. Whether you want the output file to have the same name.
3. The desired output HTML file name (if you chose not to use the same name).
4. Whether you want the output file to be in the same location as the input file.
5. The desired output directory (if you chose not to use the same location).

### CLI Example
```bash
python md_to_html_CLI.py path/to/input.md --output_file output.html --output_dir path/to/output/dir
```

This command will convert the specified Markdown file to HTML and save it with the given name in the specified directory.

## License
This project is licensed under the MIT License. See the [LICENSE.txt](https://unloosed.github.io/MarkdownToHTMLConverter/LICENSE.txt) file for details.