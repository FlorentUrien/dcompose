from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/rendu/{p}")
async def read_p(p: int):
    print(p)
    time.sleep(5 * p)
    return {"p": p}
