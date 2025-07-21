from fastapi import FastAPI, UploadFile, File
import boto3

app = FastAPI()

s3 = boto3.client("s3")
BUCKET_NAME = "seu-bucket"  # substitua pelo seu bucket real

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file.filename,
        Body=contents
    )
    return {"message": f"Arquivo '{file.filename}' enviado com sucesso para o S3!"}
