
# Running the CLI

Run as CLI (src/main.py) with:
```
    python3 src/cli.py
```

Run as server (src/main.py) with:
```
    uvicorn src.server:cheese_cake_server --port 3001 --reload
```

All imports will start from where the `main.py` file is located (look at the imports in `main.py`)








# For PyInstaller    -
```
    pyinstaller src/main.py --onefile --noconsole --name "cheese_cake"
```