from celery import Celery

app = Celery('my_tasks', broker='pyamqp://guest:guest@localhost//')

# A sample celery task.
@app.task
def add_task(x, y):
    return x + y