from fastapi import FastAPI,Query
from .task_queue.conection import queue
from .task_queue.worker import process_query

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Chat API!"}

@app.post("/chat")
def chat(
    query:str= Query(...,description="ChatMessage")
    
):
    # Query ko Queue mei daal do
    job = queue.enqueue(process_query, query)  # process_query(query)

    # User ko bolo your job received
    return {"status": "queued", "job_id": job.id}
    pass
    