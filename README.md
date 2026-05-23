# poetry‑cli

A **tiny** command‑line tool that prints a random poem fetched from the free
[PoetryDB](https://poetrydb.org) API.

```bash
pip install poetry‑cli   # after publishing, or `pip install -e .` locally
poetry-cli              # or `python -m poetry_cli`
```

## Features
- One‑command fetch of a random poem (title, author, lines).
- No heavy dependencies – uses the Python standard library.
- Packaged with a modern `src/` layout and a minimal `pyproject.toml`.

## Project layout
```
poetry-cli/
├─ src/
│  └─ poetry_cli/
│     ├─ __init__.py
│     ├─ __main__.py
│     └─ main.py
├─ pyproject.toml
├─ .gitignore
└─ README.md
```

## Development
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
# run the tool
python -m poetry_cli
```

## License
MIT – see `LICENSE` (not included in this tiny scaffold).