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

[Async: Transcribe an Audio File](transcribe.ipynb)\
[Async: Specify a Language](specify-language.ipynb) \
[Async: Transcribe YouTube Videos](transcribe_youtube_videos.ipynb)\
[Async: Build a UI for Transcription with Gradio](gradio-frontend.ipynb)\
[Async: Detect Low Confidence Words in a Transcript](detecting-low-confidence-words.md)\
🆕 [Async: How to Use the EU Endpoint](how_to_use_the_eu_endpoint.ipynb)  

<a name="batch"></a>

### Batch Transcription

[Async: Transcribe a Batch of Files](transcribe_batch_of_files)\
[Async: Transcribe Multiple Files Simultaneously - Python SDK](SDK_transcribe_batch_of_files/batch_transcription.ipynb)\
[Async: Transcribe Multiple Files Simultaneously - Node SDK](SDK-Node-batch.md)

<a name="host-files"></a>

### Hosting Audio Files

[Async: Transcribe from an AWS S3 Bucket](transcribe_from_s3.ipynb)\
[Async: Transcribe Google Drive Links](transcribing-google-drive-file.md)\
[Async: Transcribe GitHub Files](transcribing-github-files.md)

<a name="speaker-labels"></a>

### Speaker Labels

[Async: Identify Speakers in Audio Recordings](speaker_labels.ipynb)\
[Async: Generate Speaker Labels with Make.com](make.com-speaker-labels.md)\
[Async: Calculate Talk/Listen Ratio of Speakers](talk-listen-ratio.ipynb)\
[Async: Create a Speaker Timeline with Speaker Labels](speaker_timeline.ipynb)\
[Async: Use Pyannote to Generate Custom Speaker Labels](Use_AssemblyAI_with_Pyannote_to_generate_custom_Speaker_Labels.ipynb)\
[Async: Speaker Diarization with Async Chunking](speaker-diarization-with-async-chunking.ipynb)\
[Async: Speaker Identification Across Files using Pinecone and Nvidia's TitaNet Model](titanet-speaker-identification.ipynb)

<a name="ald"></a>

### Automatic Language Detection

[Async: Use Automatic Language Detection](automatic-language-detection.ipynb)\
[Async: Automatic Language Detection as Separate Step from Transcription](automatic-language-detection-separate.ipynb)\
[Async: Route to Default Language if Language Detection Confidence is Low - Node SDK](automatic-language-detection-route-default-language-js.md)\
[Async: Route to Default Language if Language Detection Confidence is Low - Python SDK](automatic-language-detection-route-default-language-python.ipynb)\
[Async: Route to Nano Speech Model if Language Confidence is Low](automatic-language-detection-route-nano-model.ipynb)

<a name="subtitles"></a>

### Subtitles

[Async: Generate Subtitles for Videos](subtitles.ipynb)\
[Async: Create Subtitles with Speaker Labels](speaker_labelled_subtitles.ipynb)\
[Async: Create Custom-Length Subtitles](subtitle_creation_by_word_count.ipynb)

<a name="delete"></a>

### Delete Transcripts

[Async: Delete a Transcript](delete_transcript.ipynb)\
[Async: Delete Transcripts After 24 Hours of Creation](schedule_delete.ipynb)

<a name="errors"></a>

### Error Handling and Audio File Fixes

[Async: Troubleshoot Common Errors When Starting to Use Our API](common_errors_and_solutions.md)\
[Async: Automatically Retry Server Errors](retry-server-error.ipynb)\
[Async: Automatically Retry Upload Errors](retry-upload-error.ipynb)\
[Async: Identify Duplicate Channels in Stereo Files](identify_duplicate_channels.ipynb)\
[Async: Correct Audio Duration Discrepancies with Multi-Tool Validation and Transcoding](audio-duration-fix.ipynb)

<a name="translate"></a>

### Translation

[Async: Translate an AssemblyAI Transcript](translate_transcripts.ipynb)\
[Async: Translate an AssemblyAI Subtitle Transcript](translate_subtitles.ipynb)

<a name="chunking"></a>

### Async Chunking for Near-Realtime Transcription

🆕 [Async: Near-Realtime Python Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-py)\
🆕 [Async: Near-Realtime Node.js Speech-to-Text App](https://github.com/AssemblyAI-Solutions/async-chunk-js)\
[Async: Split Audio File into Shorter Files](split_audio_file)

<a name="migration-guides"></a>

### Migration Guides

[Async: AWS Transcribe to AssemblyAI](migration_guides/aws_to_aai.ipynb)\
[Async: Deepgram to AssemblyAI](migration_guides/dg_to_aai.ipynb)\
[Async: OpenAI to AssemblyAI](migration_guides/oai_to_aai.ipynb)\
[Async: Google to AssemblyAI](migration_guides/google_to_aai.ipynb)

<a name="do-more-with-sdk"></a>

### Do More with our SDKS

[Async: Do More with the Node SDK](do-more-with-sdk-js.md)\
[Async: Do More with the Python SDK](do-more-with-sdk-python.ipynb)
