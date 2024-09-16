# Transcribe a batch of audio files with AssemblyAI
In this app, we submit a folder of files from the user's computer and then submit them to AssemblyAI for asynchronous transcription. Once a transcript completes, a Webhook message from AssemblyAI triggers a server function that saves the transcript into a text file. This is accomplished using FastAPI for our server, ngrok to expose our development server to the public Internet, and AssemblyAI's Python SDK.

## How To Install and Run the Project

### Prerequisites
[An AssemblyAI account](https://www.assemblyai.com/dashboard/signup). We recommend upgrading to a Pro account which unlocks a [concurrency limit](https://www.assemblyai.com/docs/concepts/concurrency-limit) of 32 for faster transcriptions.
[A free ngrok account](https://dashboard.ngrok.com/signup).

### Instructions

1.  Clone the repo to your local machine.
2.  Open a terminal in the main directory housing the project.
3.  Add your audio files to be transcribed the `audio` directory
4.  Run  `pip install -r requirements.txt`  to ensure all dependencies are installed.
5.  Add your AssemblyAI key to line 5 of  `receiver.py` and line 12 of `submitter.py`.
6.  Export your authtoken from the ngrok dashboard as `NGROK_AUTHTOKEN` in your terminal using `export NGROK_AUTHTOKEN=YOUR_NGROK_TOKEN_HERE`
7.  Start the server with the command  `uvicorn receiver:app`  (will run on port 8000).
8.  Open a second terminal in the main directory of the project and start the submitter script with  `python submitter.py` 
9. Do not close or exit `submitter.py` until all of your transcripts are complete, as it keeps the public URL created by ngrok for your server alive.

## Further Documentation

- [Using Webhooks with AssemblyAI](https://www.assemblyai.com/docs/concepts/webhooks)
- [FastAPI](https://fastapi.tiangolo.com/)

## Contact Us

If you have any questions, please feel free to reach out to our Support team -  [support@assemblyai.com](mailto:support@assemblyai.com) or in our Community Discord!
