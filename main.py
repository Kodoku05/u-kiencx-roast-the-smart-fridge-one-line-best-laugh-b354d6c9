from pathlib import Path

line = "My smart fridge sends me photos of my groceries like a kidnapper who's already killed the lettuce."
output = Path("/output")
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_text(line + "\n", encoding="utf-8")
