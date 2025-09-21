import uvicorn




if __name__ == "__main__":
    #- Running Uvicorn as a script instead of as a module.
    #$ Need to pass application as import string
    uvicorn.run("agent.server.api:cheese_cake_server",  host="0.0.0.0", port=3001, reload=True)