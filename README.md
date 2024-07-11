# AssemblyAI Cookbook 🧑‍🍳
The AssemblyAI Cookbook is a resource of code examples, guides, and tutorials for using the AssemblyAI API. Want to learn more about AssemblyAI? Check out this [product overview video](https://youtu.be/UT1sBCuSJxE)!

You will need an AssemblyAI account and API key to use these code examples. [Click here](https://www.assemblyai.com/dashboard/signup) to create and account for free.

Most code examples are written in Python or Javascript, but the concepts contained in these examples can be applied to any language. You can learn more about our various models in features in our [official documentation](https://www.assemblyai.com/docs/).

## Core Transcription 🎙️
[Transcribe an Audio File](core-transcription/transcribe.ipynb)      
[Transcribe from an AWS S3 Bucket](core-transcription/transcribe_from_s3.ipynb)  
[Transcribe a batch of files using AssemblyAI](core-transcription/transcribe_batch_of_files)   
[Use our SDK transcribe a batch of files](core-transcription/SDK_transcribe_batch_of_files)  
[Transcribe multiple files simultaneously using our Python SDK](core-transcription/SDK_transcribe_batch_of_files/batch_transcription.ipynb)      
🆕[Transcribe multiple files simultaneously using our Node.js SDK](core-transcription/SDK-Node-batch.md)   
[Transcribe YouTube videos](core-transcription/transcribe_youtube_videos.ipynb)  
[Transcribe Google Drive links](core-transcription/transcribing-google-drive-file.md)  
[Detect Low Confidence Words in a Transcript](core-transcription/detecting-low-confidence-words.md)  
🆕[Translate Transcripts](core-transcription/translate_transcripts.ipynb)  
[Generate Subtitles for Videos](core-transcription/subtitles.ipynb)\
🆕[Generate Speaker Labels with Make.com](core-transcription/make.com-speaker-labels.md)\
[Translate Subtitles](core-transcription/translate_subtitles.ipynb)     
[Specify a Language](core-transcription/specify-language.ipynb)  
[Use Automatic Language Detection](core-transcription/automatic-language-detection.ipynb)    
[Automatic Language Detection as separate step from Transcription](core-transcription/automatic-language-detection-separate.ipynb)    
[Create Subtitles with Speaker Labels](core-transcription/speaker_labelled_subtitles.ipynb)   
[Split audio file to shorter files](core-transcription/split_audio_file)   
[Delete a Transcript ](core-transcription/delete_transcript.ipynb)  
🆕[Build a UI for Transcription with Gradio](core-transcription/gradio-frontend.ipynb)  
🆕[Troubleshoot common errors when starting to use our API](core-transcription/common_errors_and_solutions.md)  
🆕[Delete transcripts after 24 hours of creation](core-transcription/schedule_delete.ipynb)

## Audio Intelligence 🤖
[Create Summarized Chapters from Podcasts](audio-intelligence/auto_chapters.ipynb)  
[Identify Hate Speech in Audio and Video Files](audio-intelligence/content_moderation.ipynb)     
[Identify Highlights in Audio and Video Files](audio-intelligence/key_phrases.ipynb)      
[Identify Speakers in Audio Recordings](audio-intelligence/speaker_labels.ipynb)      
[Summarize Virtual Meetings](audio-intelligence/summarization.ipynb)      
[Create a redacted transcript with Entity Detection](audio-intelligence/entity_redaction.ipynb)      

## Streaming STT 🕒
[Transcribe files in real-time with Node.js](streaming-stt/file-transcription-nodejs)\
[Use Streaming STT with Python](streaming-stt/real-time.ipynb)\
[Real-Time React Example](https://github.com/AssemblyAI-Examples/realtime-react-example)      \
[Use LeMUR with Streaming STT](streaming-stt/real_time_lemur.ipynb)\
[Terminate Streaming STT session after a fixed duration of inactivity](streaming-stt/terminate_realtime_programmatically.ipynb)\
[Use Partial Transcripts](streaming-stt/partial_transcripts.ipynb)

## LeMUR 🐾
[Process Audio Files with LLMs Using LeMUR](lemur/using-lemur.ipynb)  
[Use LeMUR Specialized Endpoints](lemur/specialized-endpoints.ipynb)  
[Leverage LeMUR for Customer Call Sentiment Analysis](lemur/call-sentiment-analysis.ipynb)     
[Extract Dialogue Data with LeMUR and JSON](lemur/dialogue-data.ipynb)     
[Automatically Generate Action Items from a Meeting with LeMUR](lemur/meeting-action-items.ipynb)     
[Implement a Sales Playbook Using LeMUR](lemur/sales-playbook.ipynb)     
🆕[Extract Citations from a Transcript with Semantic Search](lemur/transcript-citations.ipynb)    
[Extract Quotes from a Transcript with LeMUR's Custom Text Input Parameter](lemur/timestamped-transcripts.ipynb)    
[Calculating LeMUR Costs by Counting Input Tokens](lemur/counting-tokens.ipynb)  
[Processing Speaker Labels with LeMUR's Custom Text Input Parameter](lemur/input-text-speaker-labels.ipynb)  
🆕[Creating Chapter Summaries with LeMUR's Custom Text Input Parameter](lemur/input-text-chapters.ipynb)  
🆕[How to Pass Context from Previous LeMUR Requests](lemur/past-response-prompts.ipynb)  
[Use LeMUR for Speaker Identification](lemur/speaker-identification.ipynb)  
🆕[Ask questions about a transcript using LeMUR's Task Endpoint](lemur/task-endpoint-structured-QA.ipynb)  
🆕[Create Custom Summaries using LeMUR's Task Endpoint](lemur/task-endpoint-custom-summary.ipynb)  

## SDKs and Other Resources 📚
Beyond the code examples here, you can learn about the AssemblyAI API from the following resources:
- [Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
- [JavaScript SDK](https://github.com/AssemblyAI/assemblyai-node-sdk)
- [Java SDK](https://github.com/AssemblyAI/assemblyai-java-sdk)
- [Golang SDK](https://github.com/AssemblyAI/assemblyai-go-sdk)
- [AssemblyAI API Spec](https://github.com/AssemblyAI/assemblyai-api-spec)
- [Command Line Interface (CLI)](https://github.com/AssemblyAI/assemblyai-cli)
- [Discuss the API in the AssemblyAI Discord](https://www.assemblyai.com/discord)
- [Check out our YouTube Channel](https://www.youtube.com/c/assemblyai)
- [Follow us on X](https://twitter.com/AssemblyAI)

***
If you have any questions, please feel free to reach out to our Support team - support@assemblyai.com!
