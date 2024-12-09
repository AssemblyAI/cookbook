# Core Transcription 🎙️
The Speech Recognition model enables you to transcribe spoken words into written text and is the foundation of all AssemblyAI products.
On top of the core transcription, you can enable other features and models, such as [Speaker Diarization](https://www.assemblyai.com/docs/speech-to-text/speaker-diarization), by adding additional parameters to the same transcription request.

## Table of Contents

- [Core Transcription 🎙️](#core-transcription-️)
  - [Table of Contents](#table-of-contents)
  - [All Core Transcription Cookbooks](#all-core-transcription-cookbooks)
    - [Basic Transcription Workflows](#basic-transcription-workflows)
    - [Batch Transcription](#batch-transcription)
    - [Hosting Audio Files](#hosting-audio-files)
    - [Speaker Labels](#speaker-labels)
    - [Automatic Language Detection](#automatic-language-detection)
    - [Subtitles](#subtitles)
    - [Delete Transcripts](#delete-transcripts)
    - [Error Handling and Audio File Fixes](#error-handling-and-audio-file-fixes)
    - [Translation](#translation)
    - [Async Chunking for Near-Realtime Transcription](#async-chunking-for-near-realtime-transcription)
    - [Migration Guides](#migration-guides)
    - [Do More with our SDKS](#do-more-with-our-sdks)


## All Core Transcription Cookbooks

<a name="basic"></a>
### Basic Transcription Workflows
[Transcribe an Audio File](transcribe.ipynb)<br> 
[Specify a Language](specify-language.ipynb)  
[Transcribe YouTube videos](transcribe_youtube_videos.ipynb)<br>
[Build a UI for Transcription with Gradio](gradio-frontend.ipynb)  
[Detect Low Confidence Words in a Transcript](detecting-low-confidence-words.md)  

<a name="batch"></a>
### Batch Transcription
[Transcribe a batch of files using AssemblyAI](transcribe_batch_of_files)   
[Transcribe multiple files simultaneously using our Python SDK](SDK_transcribe_batch_of_files/batch_transcription.ipynb)      
[Transcribe multiple files simultaneously using our Node.js SDK](SDK-Node-batch.md) 

<a name="host-files"></a>
### Hosting Audio Files
[Transcribe from an AWS S3 Bucket](transcribe_from_s3.ipynb)  
[Transcribe Google Drive links](transcribing-google-drive-file.md)<br>
[Transcribe GitHub Files](transcribing-github-files.md) 

<a name="speaker-labels"></a>
### Speaker Labels
[Identify Speakers in Audio Recordings](speaker_labels.ipynb)<br>
[Generate Speaker Labels with Make.com](make.com-speaker-labels.md)\
[Calculate Talk/Listen Ratio of Speakers](talk-listen-ratio.ipynb)<br>
[Create a speaker timeline with Speaker Labels](speaker_timeline.ipynb)\
[Use AssemblyAI with Pyannote to generate custom Speaker Labels](Use_AssemblyAI_with_Pyannote_to_generate_custom_Speaker_Labels.ipynb)<br>
[Speaker Diarization with Async Chunking](speaker-diarization-with-async-chunking.ipynb)<br>
[Speaker Identification Across Files w/ AssemblyAI, Pinecone, and Nvidia's TitaNet Model](titanet-speaker-identification.ipynb)

<a name="ald"></a>
### Automatic Language Detection
[Use Automatic Language Detection](automatic-language-detection.ipynb)    
[Automatic Language Detection as separate step from Transcription](automatic-language-detection-separate.ipynb)    
[Route to Default Language if Language Detection Confidence is Low - JS](automatic-language-detection-route-default-language-js.md)\
[Route to Default Language if Language Detection Confidence is Low - Python](automatic-language-detection-route-default-language-python.ipynb)<br>
[Route to Nano Speech Model if Language Confidence is Low](automatic-language-detection-route-nano-model.ipynb)

<a name="subtitles"></a>
### Subtitles
[Generate Subtitles for Videos](subtitles.ipynb)\
[Create Subtitles with Speaker Labels](speaker_labelled_subtitles.ipynb)<br>
[Create custom-length subtitles with AssemblyAI](subtitle_creation_by_word_count.ipynb)

<a name="delete"></a>
### Delete Transcripts
[Delete a Transcript ](delete_transcript.ipynb)  
[Delete transcripts after 24 hours of creation](schedule_delete.ipynb)  

<a name="errors"></a>
### Error Handling and Audio File Fixes
[Troubleshoot common errors when starting to use our API](common_errors_and_solutions.md)<br>
[Automatically Retry Server Errors](retry-server-error.ipynb)  
[Automatically Retry Upload Errors](retry-upload-error.ipynb)\
[Identify Duplicate Channels in Stereo Files](identify_duplicate_channels.ipynb)\
[Correct Audio Duration Discrepancies with Multi-Tool Validation and Transcoding
](audio-duration-fix.ipynb)

<a name="translate"></a>
### Translation
[Translate Transcripts](translate_transcripts.ipynb)  
[Translate Subtitles](translate_subtitles.ipynb)

<a name="chunking"></a>
### Async Chunking for Near-Realtime Transcription
🆕 [Near-Realtime Python Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-py)\
🆕 [Near-Realtime Node.js Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-js)\
[Split audio file to shorter files](split_audio_file)

<a name="migration-guides"></a>
### Migration Guides
🆕 [AWS Transcribe to AssemblyAI](migration_guides/aws_to_aai.ipynb)\
🆕 [Deepgram to AssemblyAI](migration_guides/dg_to_aai.ipynb)<br> 
🆕 [OpenAI to AssemblyAI](migration_guides/oai_to_aai.ipynb)

<a name="do-more-with-sdk"></a>
### Do More with our SDKS
[Do more with the JavaScript SDK](do-more-with-sdk-js.md)\
[Do more with the Python SDK](do-more-with-sdk-python.ipynb)
