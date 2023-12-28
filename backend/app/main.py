from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from enum import Enum
from gen import gen_rand_password, gen_256_key, gen_512_key

class KeySize(Enum):
    SHA256 = '256'
    SHA512 = '512'

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')

@app.get("/key/")
def get_key(size: KeySize = Query(..., description="Key sizes: 256, 512")):
    if size == KeySize.SHA256:
        return {"key": gen_256_key()}
    elif size == KeySize.SHA512:
        return {"key": gen_512_key()}
    
@app.get("/password/{length}")
def get_password(length: int):
    
    if length < 1:
        raise HTTPException(status_code=400, detail="Password length must be greater than 0")
    elif length > 1000:
        raise HTTPException(status_code=400, detail="Password length must be less than 1000")
    else:
        return {"password": gen_rand_password(length)}
    