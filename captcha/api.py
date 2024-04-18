import base64
from fastapi import FastAPI
from captcha.semantic import Identity
# from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from pydantic import BaseModel
app = FastAPI()

class ImageItem(BaseModel):
    image: str
    text: str
    model: float = None

# model_name = "Helsinki-NLP/opus-mt-en-zh"
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# translation = pipeline("translation", model=model, tokenizer=tokenizer)


# @app.get("/translate/")
# async def translate_text(text: str):
#     result = translation(text, max_length=10240)[0]
#     return {"translation": result["translation_text"]}


@app.post("/identity")
async def identity(item: ImageItem):
    # try:
    identity = Identity(base64.b64decode(item.image), model_cls=item.model)
    res = identity.start(text=item.text)
    return {"code": 200, "data": res}
    # except Exception as e:
    #     return {"code": -1, "msg": str(e), "data":[]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
