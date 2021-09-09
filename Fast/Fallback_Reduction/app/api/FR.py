from fastapi import APIRouter, File
from app.api import helper
from io import StringIO
from datetime import datetime
import pandas as pd
import boto3

fr = APIRouter()


@fr.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@fr.post("/predict")
async def predict(fall_file: bytes = File(...), db_file: bytes = File(...)):
    fall_data = pd.read_excel(fall_file)
    db_data = pd.read_excel(db_file)
    res = helper.predict_fr(db_data, fall_data)
    filename = 'fallback_reduction'
    date = datetime.now().strftime("%Y_%m_%d_%I%M%S_%p")
    key = "FR" + "/" + filename + "_" + date + '.csv'
    excel_buffer = StringIO()
    res.to_csv(excel_buffer)
    s3_resource = boto3.resource('s3', aws_secret_access_key=helper.AWS_SECRET_ACCESS_KEY, aws_access_key_id=helper.AWS_ACCESS_KEY_ID)
    s3_resource.Object(helper.AWS_S3_BUCKET, key).put(Body=excel_buffer.getvalue())
    object_name = helper.get_object_name(helper.AWS_S3_BUCKET, helper.PREFIX_FR)
    url = helper.create_presigned_url(helper.AWS_S3_BUCKET, object_name)
    return {"url": url}

