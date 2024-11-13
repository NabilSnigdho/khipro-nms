# Khipro NMS

[NMS Kontho](https://nabil-bot.github.io/Kontho/) layout for [Khipro](https://github.com/rank-coder/khipro-m17n/).

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
