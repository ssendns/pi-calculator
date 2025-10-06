from fastapi import FastAPI
from celery.result import AsyncResult
from app.tasks import add_five
from app.celery_worker import celery_app

app = FastAPI()


@app.get("/")
def root():
    return {"message": "test"}

@app.get("/start_task")
def start_task():
    task = add_five.delay()
    return {"task_id": task.id}

@app.get("/check_task")
def check_task(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if result.state == "PENDING":
        return {"state": "PENDING", "result": None}
    elif result.state == "SUCCESS":
        return {"state": "FINISHED", "result": result.result}
    else:
        return {"state": result.state, "result": None}