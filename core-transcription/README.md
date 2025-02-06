# Speech-To-Text 🎙️

The Speech Recognition model enables you to transcribe spoken words into written text and is the foundation of all AssemblyAI products.
On top of the core transcription, you can enable other features and models, such as [Speaker Diarization](https://www.assemblyai.com/docs/speech-to-text/speaker-diarization), by adding additional parameters to the same transcription request.

## Table of Contents

- [Speech-To-Text 🎙️](#speech-to-text-️)
  - [Table of Contents](#table-of-contents)
  - [All Speech-To-Text Cookbooks](#all-speech-to-text-cookbooks)
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

## All Speech-To-Text Cookbooks

<a name="basic"></a>

### Basic Transcription Workflows

[Speech-To-Text: Transcribe an Audio File](transcribe.ipynb)\
[Speech-To-Text: Specify a Language](specify-language.ipynb) \
[Speech-To-Text: Transcribe YouTube Videos](transcribe_youtube_videos.ipynb)\
[Speech-To-Text: Build a UI for Transcription with Gradio](gradio-frontend.ipynb)\
[Speech-To-Text: Detect Low Confidence Words in a Transcript](detecting-low-confidence-words.md)\
🆕 [Speech-To-Text: How to Use the EU Endpoint](how_to_use_the_eu_endpoint.ipynb)  

<a name="batch"></a>

### Batch Transcription

[Speech-To-Text: Transcribe a Batch of Files](transcribe_batch_of_files)\
[Speech-To-Text: Transcribe Multiple Files Simultaneously - Python SDK](SDK_transcribe_batch_of_files/batch_transcription.ipynb)\
[Speech-To-Text: Transcribe Multiple Files Simultaneously - Node SDK](SDK-Node-batch.md)

<a name="host-files"></a>

### Hosting Audio Files

[Speech-To-Text: Transcribe from an AWS S3 Bucket](transcribe_from_s3.ipynb)\
[Speech-To-Text: Transcribe Google Drive Links](transcribing-google-drive-file.md)\
[Speech-To-Text: Transcribe GitHub Files](transcribing-github-files.md)

<a name="speaker-labels"></a>

### Speaker Labels

[Speech-To-Text: Identify Speakers in Audio Recordings](speaker_labels.ipynb)\
[Speech-To-Text: Generate Speaker Labels with Make.com](make.com-speaker-labels.md)\
[Speech-To-Text: Calculate Talk/Listen Ratio of Speakers](talk-listen-ratio.ipynb)\
[Speech-To-Text: Create a Speaker Timeline with Speaker Labels](speaker_timeline.ipynb)\
[Speech-To-Text: Use Pyannote to Generate Custom Speaker Labels](Use_AssemblyAI_with_Pyannote_to_generate_custom_Speaker_Labels.ipynb)\
[Speech-To-Text: Speaker Diarization with Async Chunking](speaker-diarization-with-async-chunking.ipynb)\
[Speech-To-Text: Speaker Identification Across Files using Pinecone and Nvidia's TitaNet Model](titanet-speaker-identification.ipynb)

<a name="ald"></a>

### Automatic Language Detection

[Speech-To-Text: Use Automatic Language Detection](automatic-language-detection.ipynb)\
[Speech-To-Text: Automatic Language Detection as Separate Step from Transcription](automatic-language-detection-separate.ipynb)\
[Speech-To-Text: Route to Default Language if Language Detection Confidence is Low - Node SDK](automatic-language-detection-route-default-language-js.md)\
[Speech-To-Text: Route to Default Language if Language Detection Confidence is Low - Python SDK](automatic-language-detection-route-default-language-python.ipynb)\
[Speech-To-Text: Route to Nano Speech Model if Language Confidence is Low](automatic-language-detection-route-nano-model.ipynb)

<a name="subtitles"></a>

### Subtitles

[Speech-To-Text: Generate Subtitles for Videos](subtitles.ipynb)\
[Speech-To-Text: Create Subtitles with Speaker Labels](speaker_labelled_subtitles.ipynb)\
[Speech-To-Text: Create Custom-Length Subtitles](subtitle_creation_by_word_count.ipynb)

<a name="delete"></a>

### Delete Transcripts

[Speech-To-Text: Delete a Transcript](delete_transcript.ipynb)\
[Speech-To-Text: Delete Transcripts After 24 Hours of Creation](schedule_delete.ipynb)

<a name="errors"></a>

### Error Handling and Audio File Fixes

[Speech-To-Text: Troubleshoot Common Errors When Starting to Use Our API](common_errors_and_solutions.md)\
[Speech-To-Text: Automatically Retry Server Errors](retry-server-error.ipynb)\
[Speech-To-Text: Automatically Retry Upload Errors](retry-upload-error.ipynb)\
[Speech-To-Text: Identify Duplicate Channels in Stereo Files](identify_duplicate_channels.ipynb)\
[Speech-To-Text: Correct Audio Duration Discrepancies with Multi-Tool Validation and Transcoding](audio-duration-fix.ipynb)

<a name="translate"></a>

### Translation

[Speech-To-Text: Translate an AssemblyAI Transcript](translate_transcripts.ipynb)\
[Speech-To-Text: Translate an AssemblyAI Subtitle Transcript](translate_subtitles.ipynb)

<a name="chunking"></a>

### Async Chunking for Near-Realtime Transcription

🆕 [Speech-To-Text: Near-Realtime Python Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-py)\
🆕 [Speech-To-Text: Near-Realtime Node.js Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-js)\
[Speech-To-Text: Split Audio File into Shorter Files](split_audio_file)

<a name="migration-guides"></a>

### Migration Guides

[Speech-To-Text: AWS Transcribe to AssemblyAI](migration_guides/aws_to_aai.ipynb)\
[Speech-To-Text: Deepgram to AssemblyAI](migration_guides/dg_to_aai.ipynb)\
[Speech-To-Text: OpenAI to AssemblyAI](migration_guides/oai_to_aai.ipynb)\
[Speech-To-Text: Google to AssemblyAI](migration_guides/google_to_aai.ipynb)

<a name="do-more-with-sdk"></a>

### Do More with our SDKS

[Speech-To-Text: Do More with the Node SDK](do-more-with-sdk-js.md)\
[Speech-To-Text: Do More with the Python SDK](do-more-with-sdk-python.ipynb)
