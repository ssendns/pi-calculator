# pi-calculator

this project demonstrates how to use **FastAPI** + **Celery** + **Redis** for background processing of long-running tasks (e.g calculating pi to n decimal places)

## API documentation

1. **start a new task**

   `GET /calculate_pi?n=100`

   starts a background task to calculate pi to `n` digits
   returns a JSON with a unique `task_id`.

   **example request:**

   ```
   GET /calculate_pi?n=200
   ```

   **example response:**

   ```json
   {
     "task_id": "9a1e56f6-9c5b-4ad1-a5bb-09ffb49b43a3"
   }
   ```

2. **check task progress**

   `GET /check_task/{task_id}`

   Returns the current state, progress (from 0.0 to 1.0), and result if finished.

   **example request:**

   ```
   GET /check_task/9a1e56f6-9c5b-4ad1-a5bb-09ffb49b43a3
   ```

   **possible responses:**

   - if task is still running:

     ```json
     {
       "state": "PROGRESS",
       "progress": 0.42,
       "result": null
     }
     ```

   - if task is finished:

     ```json
     {
       "state": "FINISHED",
       "progress": 1.0,
       "result": "3.14159..."
     }
     ```

   - if task is still waiting in queue:
     ```json
     {
       "state": "PENDING",
       "progress": 0.0,
       "result": null
     }
     ```

## how to run locally with Docker

1. clone the repository
2. duild and run everything:
   ```bash
   docker-compose up --build
   ```
