import uvicorn
from fastapi import FastAPI
from addresses_service.app.api.db import metadata, database, engine
from addresses_service.app.api.views import addresses

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(addresses, tags=['addresses'])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002)

