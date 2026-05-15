# Hash-GUI

A simple GUI application for hashing files and text.

## Requirements

- Python 3.13 or newer.
- [`uv`](https://docs.astral.sh/uv/) installed and available on your PATH.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MrSplatchy/Hash-GUI.git
   cd Hash-GUI
   ```

2. Make sure Python 3.13+ is available:
   ```bash
   python --version
   ```
   If needed, you can let `uv` manage the Python version:
   ```bash
   uv python install 3.13
   ```

3. Create the environment and install dependencies:
   ```bash
   uv sync
   ```

## Run

Start the application with:

```bash
uv run python main.py
```

## Development

To run the app after making changes, use the same command:

```bash
uv run python main.py
```

## Notes

- `uv sync` installs the project dependencies into the local virtual environment.
- `uv run` ensures the app runs inside that environment without manual activation.
