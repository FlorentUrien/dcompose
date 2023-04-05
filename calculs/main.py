from fastapi import FastAPI
import threading
import requests
import time


def lanceRendu(p: int):
    """response = requests.get("http://0.0.0.0:500" + str(p) + "/rendu/" + str(p))"""
    response = requests.get("http://rendu" + str(p) + ":500" + str(p) + "/rendu/" + str(p))
    print("Rendu (" + str(p) + ")" + str(response))


time.sleep(5)
param = 1
thread1 = threading.Thread(target=lanceRendu, args=(param,))
param = 2
thread2 = threading.Thread(target=lanceRendu, args=(param,))
param = 3
thread3 = threading.Thread(target=lanceRendu, args=(param,))
thread1.start()
thread2.start()
thread3.start()

app = FastAPI()


@app.get("/")
async def rendu():
    return "Florent"
