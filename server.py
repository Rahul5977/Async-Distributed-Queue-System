from fastapi import FastAPI,Query
app=FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Chat API!"}

@app.post("/chat")
def chat(
    query:str= Query(...,description="ChatMessage")
):
    pass
    