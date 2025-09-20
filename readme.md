
# Why did you ask to follow module system?
Because the editor becomes visually clumsy when imported files from nested folders. However, running Python as a script also worked fine.

# How does running Python as a module work?
Basically, to make sure that we run as a module having your terminal positioned in  "./" where "./agent" is so all imports that start whit "agent" work.


# Running the CLI

Run as CLI (src/main.py) with:
```
    python -m src.cli
```

# Running the FastAPI server
### 2 options:

Run "run_server.py":
```
    python -m agent.run_server
```

Run directly with Uvicorn:
```
    uvicorn agent.server.app:cheese_cake_server --port 3001 --reload
```










# For PyInstaller    -
```
    pyinstaller src/main.py --onefile --noconsole --name "cheese_cake"
```