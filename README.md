# AssemblyAI Cookbook 🧑‍🍳
The AssemblyAI Cookbook is a resource of code examples, guides, and tutorials for using the AssemblyAI API. Want to learn more about AssemblyAI? Check out this [product overview video](https://youtu.be/UT1sBCuSJxE)!

You will need an AssemblyAI account and API key to use these code examples. [Click here](https://www.assemblyai.com/dashboard/signup) to create and account for free.

Most code examples are written in Python or Javascript, but the concepts contained in these examples can be applied to any language. You can learn more about our various models in features in our [official documentation](https://www.assemblyai.com/docs/).

## Core Transcription 🎙️

Tutorial | Description |
:- | :-
[transcribe.ipynb](core-transcription/transcribe.ipynb)|Transcribe an Audio File
[transcribe_from_s3.ipynb](transcribe_from_s3.ipynb)|Transcribe from an AWS S3 Bucket
[transcribe_batch_of_files](core-transcription/transcribe_batch_of_files)|Transcribe a batch of files
[SDK_transcribe_batch_of_files](core-transcription/SDK_transcribe_batch_of_files)|Use the SDK to transcribe a batch of files
[batch_transcription.ipynb](core-transcription/SDK_transcribe_batch_of_files/batch_transcription.ipynb)|Transcribe multiple files simultaneously using our SDK
[transcribe_youtube_videos.ipynb](core-transcription/transcribe_youtube_videos.ipynb)|Transcribe YouTube videos
🆕[transcribing-google-drive-file.md](core-transcription/transcribing-google-drive-file.md)|Transcribe Google Drive links
🆕[detecting-low-confidence-words.md](core-transcription/detecting-low-confidence-words.md)|Detect Low Confidence Words in a Transcript
[subtitles.ipynb](core-transcription/subtitles.ipynb)|Generate Subtitles for Videos
[translate_subtitles.ipynb](core-transcription/translate_subtitles.ipynb)|Translate Subtitles
[specify-language.ipynb](core-transcription/specify-language.ipynb)|Specify Language
[automatic-language-detection.ipynb](core-transcription/automatic-language-detection.ipynb)|Use Automatic Language Detection
[detecting-low-confidence-words.md](core-transcription/detecting-low-confidence-words.md)|Detect Low Confidence Words
🆕[speaker_labelled_subtitles.ipynb](core-transcription/speaker_labelled_subtitles.ipynb)|Create Subtitles with Speaker Labels
🆕[split_audio_file](core-transcription/split_audio_file)|Split audio file to shorter files
🆕[delete_transcript.ipynb](core-transcription/delete_transcript.ipynb)|Delete a Transcript 

## Audio Intelligence 🤖
[Creating Summarized Chapters from Podcasts](audio-intelligence/auto_chapters.ipynb)  
[Identifying Hate Speech in Audio and Video Files](audio-intelligence/content_moderation.ipynb)     
[Identifying Highlights in Audio and Video Files](audio-intelligence/key_phrases.ipynb)      
[Identifying Speakers in Audio Recordings](audio-intelligence/speaker_labels.ipynb)      
[Summarizing Virtual Meetings](audio-intelligence/summarization.ipynb)

## Real-time 🕒
[Transcribe files in real-time with Node.js](real-time/file-transcription-nodejs)\
[Using Real-Time Streaming](real-time/real-time.ipynb)\
[Real-Time React Example](https://github.com/AssemblyAI-Examples/realtime-react-example)      \
[Using LeMUR with Real-Time Streaming](real-time/real_time_lemur.ipynb)\
[Terminate real-time session after a fixed duration of inactivity](real-time/terminate_realtime_programmatically.ipynb)\
[Using Partial Transcripts](real-time/partial_transcripts.ipynb)

## LeMUR 🐾
[Processing Audio Files with LLMs Using LeMUR](lemur/using-lemur.ipynb)  
[Using LeMUR Specialized Endpoints](lemur/specialized-endpoints.ipynb)  
[Leverage LeMUR for Customer Call Sentiment Analysis](lemur/call-sentiment-analysis.ipynb)     
[Extract Dialogue Data with LeMUR and JSON](lemur/dialogue-data.ipynb)     
[Automatically Generate Action Items from a Meeting with LeMUR](lemur/meeting-action-items.ipynb)     
[Implement a Sales Playbook Using LeMUR](lemur/sales-playbook.ipynb)     
🆕[Extract Citations from a Transcript with Semantic Search](lemur/transcript-citations.ipynb)    
🆕[Extract Quotes from a Transcript with LeMUR's Custom Text Input Parameter](lemur/timestamped-transcripts.ipynb)    
[Calculating LeMUR Costs by Counting Input Tokens](lemur/counting-tokens.ipynb)  
🆕[Processing Speaker Labels with LeMUR's Custom Text Input Parameter](lemur/input-text-speaker-labels.ipynb)  
🆕[Creating Chapter Summaries with LeMUR's Custom Text Input Parameter](lemur/input-text-chapters.ipynb)  

## SDKs and Other Resources 📚
Beyond the code examples here, you can learn about the AssemblyAI API from the following resources:
- [Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
- [Node.js SDK](https://github.com/AssemblyAI/assemblyai-node-sdk)
- [Java SDK](https://github.com/AssemblyAI/assemblyai-java-sdk)
- [Golang SDK](https://github.com/AssemblyAI/assemblyai-go-sdk)
- [AssemblyAI API Spec](https://github.com/AssemblyAI/assemblyai-api-spec)
- [Command Line Interface (CLI)](https://github.com/AssemblyAI/assemblyai-cli)
- [Discuss the API in the AssemblyAI Discord](https://www.assemblyai.com/discord)
- [Check out our YouTube Channel](https://www.youtube.com/c/assemblyai)
- [Follow us on X](https://twitter.com/AssemblyAI)

***
If you have any questions, please feel free to reach out to our Support team - support@assemblyai.com!
