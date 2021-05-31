from fastapi import FastAPI, Query
from core.config import settings
from enum import Enum
from typing import Optional
from pydantic import BaseModel


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

class ModelName(str, Enum):
    alexnet = "alexnet"
    trial = "trial"
    nowday = "nowday"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/models/{model_name}")
def get_item(model_name: ModelName, extra: Optional[str]=None):
    if model_name == ModelName.alexnet:
        return {"Model name": 'alexnet', "extra": extra}

    if model_name == ModelName.trial:
        return {"Model name": 'trial'}

    # if model_name == ModelName.nowday:
    return {"Model name": 'nowday'}

@app.post("/items/{item_id}")
def create_item(item: Item, item_id: int, q: Optional[str] = Query(None, min_length=3, max_length=40)):
    item_dict = item.dict()
    item_dict.update({"params": q})
    item_dict.update({"id": item_id})
    
    if (item.tax):
        item_dict.update({"price_with_tax": item.tax+item.price})

    return item_dict

"this is from branch one"

"this is from branch one again"