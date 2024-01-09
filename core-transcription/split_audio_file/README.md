# Splitting audio file into shorter files
In this code snippet, we split an audio file into shorter files. You can specify the increments of each split file (in seconds) in the `duration` variable. This can be used for mutliple use cases which can include: asynchronous batch processing, splitting files that exceed the audio length limit (10 hours for the /v2/transcript endpoint) and more. 

Once the script has processed, the split files will be stored in the `output` folder which can be changed to any desired folder.

## How To Run the Project

### Instructions

1.  Clone the repo to your local machine.
2.  Open a terminal in the main directory housing the project.
3.  Add your audio files to the `/split_audio_file` folder
4.  Run  `pip install -r requirements.txt`  to ensure all dependencies are installed.
5.  Specify variables `input_file`, `output_folder` and `duration` 
6.  Run `split.py`

## File Size Limits
There is both a maximum file size and a maximum audio duration for files that can be submitted to the API. The maximum file size that can be submitted to the /v2/transcript endpoint for transcription is 5GB. The maximum file size for a local file uploaded to the API via the /v2/upload endpoint is 2.2GB.

The maximum audio duration for a file submitted to the /v2/transcript endpoint for transcription is 10 hours. 


## Contact Us

If you have any questions, please feel free to reach out to our Support team -  [support@assemblyai.com](mailto:support@assemblyai.com) or in our Community Discord!
