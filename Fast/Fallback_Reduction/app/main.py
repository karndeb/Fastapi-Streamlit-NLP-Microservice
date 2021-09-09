from fastapi import FastAPI
from app.api.FR import fr
# import uvicorn

app = FastAPI(openapi_url="/api/v1/fallback_reduction/openapi.json", docs_url="/api/v1/fallback_reduction/docs")

app.include_router(fr, prefix="/api/v1/fallback_reduction", tags=["fallback_reduction"])

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080)
