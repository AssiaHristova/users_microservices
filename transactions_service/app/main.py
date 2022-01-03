import uvicorn
from fastapi import FastAPI
from transactions_service.app.api.db import metadata, database, engine
from transactions_service.app.api.views import transactions

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(transactions, tags=['transactions'])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8003)

