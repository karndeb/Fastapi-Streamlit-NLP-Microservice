from fastapi import FastAPI
from app.api.NQR import nqr
# import uvicorn

app = FastAPI(openapi_url="/api/v1/next_query_recommendation/openapi.json", docs_url="/api/v1/next_query_recommendation/docs")

app.include_router(nqr, prefix="/api/v1/next_query_recommendation", tags=["next_query_recommendation"])

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080)
