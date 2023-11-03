from fastapi import FastAPI
import assemblyai as aai
from pydantic import BaseModel

aai.settings.api_key = "YOUR-API-KEY"

app = FastAPI()

class Result(BaseModel):
    status: str
    transcript_id: str

@app.post("/")
async def retrieve(filename: str, result: Result):
    if result.status == "completed":
        transcription_result = aai.Transcript.get_by_id(result.transcript_id)
        with open(f"transcripts/{filename}.txt", "w") as f:
            f.write(transcription_result.text)
    elif result.status == "error":
        transcription_result = aai.Transcript.get_by_id(result.transcript_id)
        print("Error: ", transcription_result.error)