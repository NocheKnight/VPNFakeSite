from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import pages

app = FastAPI(title="Simple Site")

# Монтируем статику
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="templates")

app.state.templates = templates

app.include_router(pages.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}