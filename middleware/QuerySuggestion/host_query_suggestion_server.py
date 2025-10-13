import sys
from PIL import Image
import open_clip
import faiss
import torch
import asyncio
import websockets
import json
import pandas as pd
import os
import re
from websockets.exceptions import ConnectionClosedOK

clipdata = []

def search(text_features, k):
    D, I = index.search(text_features, k)
    return D, I

def similaritysearch(idx, k):
    D, I = index.search(clipdata[0][idx:idx+1], k)
    return D, I

def getLabels():
    return labels

def filterAndLabelResults(I, D, resultsPerPage, selectedPage):
    labels = getLabels()
    kfresults = []
    kfresultsidx = []
    kfscores = []
    num_results = len(I[0])

    if num_results == 0:
        raise Exception("No results from FAISS search.")

    ifrom = (selectedPage - 1) * resultsPerPage
    ito = selectedPage * resultsPerPage

    if ifrom >= num_results:
        return [], [], []
    
    for i in range(ifrom, min(ito, num_results)):
        idx = I[0][i]
        score = D[0][i]
        if idx == -1:
            continue
        kfresults.append(str(labels[idx]))
        kfresultsidx.append(int(idx))
        kfscores.append(str(score))

    return kfresults, kfresultsidx, kfscores



async def handler(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(message)
            msg = json.loads(message)
            event = msg['content']
            query = event["query"]

            tmp = json.dumps({ "suggestion": "Did you mean: " + query})
            await websocket.send(tmp)
    except ConnectionClosedOK:
        print("Connection closed gracefully.")
    except Exception as e:
        print("Exception: ", str(e))


async def main():
    port = 8001
    if len(sys.argv) > 1:
        port = sys.argv[1]
    async with websockets.serve(handler, "", port):
        print(f'listening on {port}')
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())