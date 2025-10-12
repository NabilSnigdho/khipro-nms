# Khipro NMS

[NMS Kontho](https://nabil-bot.github.io/Kontho/) layout for [Khipro](https://github.com/rank-coder/khipro-m17n/).

## ⚠️ Repository Archived: Moving to the Official Khipro Organization

I have **archived this repository** and will **no longer be actively maintaining** the Python script or the generated keyboard layout file.

This decision was made because I unfortunately no longer have the time to dedicate to its proper maintenance.

### Where to Find the Maintained Layout

I am happy to report that the official [Khipro organization](https://github.com/KhiproKeyboard) has taken over maintenance of the layout file of Khipro for [Nms Kontho](https://nabil-bot.github.io/Kontho/)!

You can find the up-to-date layout file, future improvements, and any necessary support at their official repository:

[https://github.com/KhiproKeyboard/khipro-nms](https://github.com/KhiproKeyboard/khipro-nms)

Please direct all future issues, pull requests, and usage questions to the repository linked above.

Thank you to everyone who showed interest in this script and its generated layout. I am glad the work has found a dedicated, long-term home.

---

## Usage

1. Install [NMS Kontho](https://nabil-bot.github.io/Kontho/).
2. Download [Khipro NMS layout](https://github.com/NabilSnigdho/khipro-nms/raw/refs/heads/main/Khipro.nmsLayout).
3. Import the layout
4. Restart NMS Kontho
5. Select Khipro layout

## Development

### Running the Main Script

The main file for this project is `generate_nms_layout.py`. This script generates the Khipro.nmsLayout file and runs the associated test cases to verify the output. To run it:

```bash
git clone https://github.com/NabilSnigdho/khipro-nms.git
cd khipro-nms
pip install black
python generate_nms_layout.py
```

This command will execute the layout generation process and run the test cases included within the script.

### Pre-commit Hook

To ensure code quality and consistency, set up a Git pre-commit hook to automatically format code using Black and run `generate_nms_layout.py` before each commit.

#### Setting up the Pre-commit Hook

1. Create a `pre-commit` file in `.git/hooks/`:
    ```bash
    touch .git/hooks/pre-commit
    ```

2. Add the following lines to `.git/hooks/pre-commit`:

    ```bash
    #!/bin/sh
    # Format code with Black
    black .

    # Run the main script to ensure tests pass before committing
    python generate_nms_layout.py

    # Re-stage any files modified
    git add .
    ```

3. Make the hook executable:

    ```bash
    chmod +x .git/hooks/pre-commit
    ```

Now, each time you attempt to commit changes, the pre-commit hook will:
1. Format the code using Black to ensure code style consistency.
2. Run the `generate_nms_layout.py` script to verify that everything is functioning as expected.

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
