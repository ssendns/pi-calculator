from fastapi import FastAPI, Query
from celery.result import AsyncResult
from app.tasks import calculate_pi
from app.celery_worker import celery_app

app = FastAPI()


@app.get("/")
def root():
    return {"message": "test"}

@app.get("/calculate_pi")
def start_task(n: int = Query(..., gt=0, lt=1000)):
    task = calculate_pi.delay(n)
    return {"task_id": task.id}

@app.get("/check_task/{task_id}")
def check_task(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if result.state == "PENDING":
        return {"state": "PENDING", "result": None}
    elif result.state == "SUCCESS":
        return {"state": "FINISHED", "result": result.result}
    else:
        return {"state": result.state, "result": None}