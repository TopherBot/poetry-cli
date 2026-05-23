import json
import sys
import urllib.request
from urllib.error import URLError, HTTPError

API_URL = "https://poetrydb.org/random"


def fetch_random_poem() -> dict:
    """Retrieve a random poem from PoetryDB.

    Returns a dictionary with at least the keys ``title``, ``author`` and ``lines``.
    Raises ``RuntimeError`` on network or decoding problems.
    """
    try:
        with urllib.request.urlopen(API_URL, timeout=10) as response:
            if response.status != 200:
                raise RuntimeError(f"Unexpected HTTP status {response.status}")
            raw = response.read().decode("utf-8")
            data = json.loads(raw)
            # API returns a list with a single poem object
            return data[0]
    except (URLError, HTTPError) as exc:
        raise RuntimeError(f"Failed to fetch poem: {exc}")
    except (json.JSONDecodeError, IndexError) as exc:
        raise RuntimeError(f"Invalid response format: {exc}")


def format_poem(poem: dict) -> str:
    title = poem.get("title", "Untitled")
    author = poem.get("author", "Unknown")
    lines = poem.get("lines", [])
    body = "\n".join(lines)
    return f"{title}\nby {author}\n\n{body}\n"


def main(argv: list | None = None) -> int:
    """Entry point for the ``poetry-cli`` command.

    Returns an exit‑code (0 for success, non‑zero for errors).
    """
    argv = argv or sys.argv[1:]
    # No arguments are needed; we just ignore anything passed.
    try:
        poem = fetch_random_poem()
        sys.stdout.write(format_poem(poem))
        return 0
    except RuntimeError as err:
        sys.stderr.write(f"Error: {err}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
