import ngrok
import os 
import assemblyai as aai

listener = ngrok.connect(8000, authtoken_from_env=True)
public_url = listener.url()
print("Public url: ", public_url)

aai.settings.api_key = "YOUR-API-KEY"
transcriber = aai.Transcriber()

for file in os.listdir("audio"):
    config = aai.TranscriptionConfig(
        webhook_url=f"{public_url}/?filename={file}"
    )
    transcriber.submit(f"audio/{file}", config=config)

while True:
    user_input = input("Press enter once your transcriptions are complete")
    if user_input:
        break
