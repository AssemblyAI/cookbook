# Core Transcription 🎙️
The Speech Recognition model enables you to transcribe spoken words into written text and is the foundation of all AssemblyAI products.
On top of the core transcription, you can enable other features and models, such as [Speaker Diarization](https://www.assemblyai.com/docs/speech-to-text/speaker-diarization), by adding additional parameters to the same transcription request.

## All Core Transcription Cookbooks

### General
[Transcribe an Audio File](core-transcription/transcribe.ipynb)<br> 
[Specify a Language](core-transcription/specify-language.ipynb)  
[Transcribe YouTube videos](core-transcription/transcribe_youtube_videos.ipynb)<br>
[Do more with the JavaScript SDK](core-transcription/do-more-with-sdk-js.md)\
[Do more with the Python SDK](core-transcription/do-more-with-sdk-python.ipynb)\
[Split audio file to shorter files](core-transcription/split_audio_file)  
[Build a UI for Transcription with Gradio](core-transcription/gradio-frontend.ipynb)  
[Detect Low Confidence Words in a Transcript](core-transcription/detecting-low-confidence-words.md)  


### Batch Transcription
[Transcribe a batch of files using AssemblyAI](core-transcription/transcribe_batch_of_files)   
[Use our SDK transcribe a batch of files](core-transcription/SDK_transcribe_batch_of_files)  
[Transcribe multiple files simultaneously using our Python SDK](core-transcription/SDK_transcribe_batch_of_files/batch_transcription.ipynb)      
[Transcribe multiple files simultaneously using our Node.js SDK](core-transcription/SDK-Node-batch.md) 

### Hosting Audio Files
[Transcribe from an AWS S3 Bucket](core-transcription/transcribe_from_s3.ipynb)  
[Transcribe Google Drive links](core-transcription/transcribing-google-drive-file.md)<br>
[Transcribe GitHub Files](core-transcription/transcribing-github-files.md) 

### Speaker Labels
[Identify Speakers in Audio Recordings](audio-intelligence/speaker_labels.ipynb)<br>
[Generate Speaker Labels with Make.com](core-transcription/make.com-speaker-labels.md)\
[Calculate Talk/Listen Ratio of Speakers](core-transcription/talk-listen-ratio.ipynb)
[Create a speaker timeline with Speaker Labels](core-transcription/speaker_timeline.ipynb)\
[Use AssemblyAI with Pyannote to generate custom Speaker Labels](core-transcription/Use_AssemblyAI_with_Pyannote_to_generate_custom_Speaker_Labels.ipynb) 

### Automatic Language Detection
[Use Automatic Language Detection](core-transcription/automatic-language-detection.ipynb)    
[Automatic Language Detection as separate step from Transcription](core-transcription/automatic-language-detection-separate.ipynb)    
[Route to Default Language if Language Detection Confidence is Low - JS](core-transcription/automatic-language-detection-route-default-language-js.md)\
[Route to Default Language if Language Detection Confidence is Low - Python](core-transcription/automatic-language-detection-route-default-language-python.ipynb)

### Subtitles
[Generate Subtitles for Videos](core-transcription/subtitles.ipynb)\
[Create Subtitles with Speaker Labels](core-transcription/speaker_labelled_subtitles.ipynb)  

### Delete Transcripts
[Delete a Transcript ](core-transcription/delete_transcript.ipynb)  
[Delete transcripts after 24 hours of creation](core-transcription/schedule_delete.ipynb)  

### Error Handling and File Corrections
[Troubleshoot common errors when starting to use our API](core-transcription/common_errors_and_solutions.md)<br>
[Automatically Retry Server Errors](core-transcription/retry-server-error.ipynb)  
[Identify Duplicate Channels in Stereo Files](core-transcription/identify_duplicate_channels.ipynb)\
[Audio Duration Fix](core-transcription/audio-duration-fix.ipynb)

### Translation
[Translate Transcripts](core-transcription/translate_transcripts.ipynb)  
[Translate Subtitles](core-transcription/translate_subtitles.ipynb)     
