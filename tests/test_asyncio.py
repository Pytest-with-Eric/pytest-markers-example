import pytest
import asyncio


# Async test function simulating asynchronous data fetch.
@pytest.mark.asyncio
async def test_fetch_data():
    await asyncio.sleep(1)  # Simulating some asynchronous operation
    data = {"key": "value"}
    assert data["key"] == "value"
