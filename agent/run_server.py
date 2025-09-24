import time
import subprocess
import sys
import uvicorn
#* This will redirect all output of the application run to cheese_cake.log

logs_dir = "cheese_cake_logs"
log_file = "run-" + time.strftime("%Y-%m-%d_%H:%M:%S")
subprocess.run(f"mkdir -p {logs_dir}", shell=True)
logfile = open(f"{logs_dir}/{log_file}" , "w")
sys.stdout = logfile
sys.stderr = logfile


if __name__ == "__main__":
    #$ Need to pass application as import string
    uvicorn.run("agent.server.api:cheese_cake_server",  host="0.0.0.0", port=8000, reload=True) 


    #¡ Forget this:
    #$ using "reload=False" Because bundled Pyinstaller app infinitely reloads due to detected changes:
        #/ "With PyInstaller’s --onefile executables, the code is bundled into a temporary directory at runtime. That temp folder changes each time you run it, so the reloader thinks files are changing continuously → endless restarts."