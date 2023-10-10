from my_tasks import add_task


# Test function to check if celery task is executing correctly.
def test_celery_add():
    result = add_task.apply((5, 4))
    while not result.ready():  # Wait for the task to complete.
        pass
    assert result.result == 9
