import uvicorn
import agent.server.api  # forces PyInstaller to see the package




if __name__ == "__main__":
    #$ Need to pass application as import string
    uvicorn.run("agent.server.api:cheese_cake_server",  host="0.0.0.0", port=3001, reload=False) 
    
    #$ using "reload=False" Because bundled Pyinstaller app infinitely reloads due to detected changes:
        #/ "With PyInstaller’s --onefile executables, the code is bundled into a temporary directory at runtime. That temp folder changes each time you run it, so the reloader thinks files are changing continuously → endless restarts."