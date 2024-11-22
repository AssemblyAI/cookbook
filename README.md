# AssemblyAI Cookbook 🧑‍🍳

The AssemblyAI Cookbook is your go-to resource for code examples, guides, and tutorials to leverage the AssemblyAI API effectively.

## Quick Links
- [Product Overview Video](https://youtu.be/UT1sBCuSJxE)
- [Sign Up for AssemblyAI (Free)](https://www.assemblyai.com/dashboard/signup)
- [Official Documentation](https://www.assemblyai.com/docs/)

### Requirements
- An AssemblyAI account and API key.
- Most examples are in **Python** or **JavaScript**, but concepts can be applied to other languages.

---

## 📂 **Categories**

### Core Transcription 🎙️
Explore fundamental transcription capabilities.

- **Basic Transcription**
  - [Transcribe an Audio File](core-transcription/transcribe.ipynb)
  - [Transcribe from an AWS S3 Bucket](core-transcription/transcribe_from_s3.ipynb)
  - [Transcribe a Batch of Files (Python)](core-transcription/transcribe_batch_of_files)
  - [Transcribe a Batch of Files (Python SDK)](core-transcription/SDK_transcribe_batch_of_files)

- **Multi-File Transcription**
  - [Simultaneous Transcription (Python SDK)](core-transcription/SDK_transcribe_batch_of_files/batch_transcription.ipynb)
  - [Simultaneous Transcription (Node.js SDK)](core-transcription/SDK-Node-batch.md)

- **Platform Integrations**
  - [Transcribe YouTube Videos](core-transcription/transcribe_youtube_videos.ipynb)
  - [Transcribe Google Drive Links](core-transcription/transcribing-google-drive-file.md)
  - 🆕 [Transcribe GitHub Files](core-transcription/transcribing-github-files.md)

- **Advanced Features**
  - [Detect Low Confidence Words](core-transcription/detecting-low-confidence-words.md)
  - [Translate Transcripts](core-transcription/translate_transcripts.ipynb)
  - [Generate Subtitles for Videos](core-transcription/subtitles.ipynb)

- **Speaker Labeling & Subtitles**
  - [Generate Speaker Labels (Make.com)](core-transcription/make.com-speaker-labels.md)
  - [Translate Subtitles](core-transcription/translate_subtitles.ipynb)
  - [Create Subtitles with Speaker Labels](core-transcription/speaker_labelled_subtitles.ipynb)

- **Language Detection**
  - [Specify a Language](core-transcription/specify-language.ipynb)
  - [Automatic Language Detection](core-transcription/automatic-language-detection.ipynb)
  - 🆕 [Run Language Detection Separately](core-transcription/automatic-language-detection-separate.ipynb)

- **Other Features**
  - [Delete Transcripts](core-transcription/delete_transcript.ipynb)
  - [Build a Gradio UI](core-transcription/gradio-frontend.ipynb)
  - 🆕 [Retry Server Errors Automatically](core-transcription/retry-server-error.ipynb)

---

### Audio Intelligence 🤖
Leverage advanced audio analysis capabilities.

- **Audio Analysis**
  - [Create Summarized Chapters](audio-intelligence/auto_chapters.ipynb)
  - [Identify Hate Speech](audio-intelligence/content_moderation.ipynb)
  - [Highlight Key Phrases](audio-intelligence/key_phrases.ipynb)

- **Speaker Identification**
  - [Label Speakers in Recordings](audio-intelligence/speaker_labels.ipynb)
  - 🆕 [Create Redacted Transcripts](audio-intelligence/entity_redaction.ipynb)

- **Meeting Summarization**
  - [Summarize Virtual Meetings](audio-intelligence/summarization.ipynb)

---

### Streaming STT 🕒
Real-time streaming speech-to-text (STT).

- **Quick Start**
  - [Real-Time Transcription (Node.js)](streaming-stt/file-transcription-nodejs)
  - [Real-Time Transcription (Python)](streaming-stt/real-time.ipynb)

- **Real-Time Best Practices**
  - 🆕 [Best Practices for Streaming STT](streaming-stt/real-time-best-practices.ipynb)
  - [Use Partial Transcripts](streaming-stt/partial_transcripts.ipynb)

- **Platform-Specific Examples**
  - [Twilio Integration (JavaScript SDK)](https://github.com/AssemblyAI/twilio-realtime-tutorial)
  - 🆕 [Stream System Audio (macOS)](streaming-stt/transcribe_system_audio.ipynb)

---

### LeMUR 🐾
Use LeMUR for audio processing with LLMs.

- **Core Features**
  - [Process Audio Files](lemur/using-lemur.ipynb)
  - [Specialized Endpoints](lemur/specialized-endpoints.ipynb)
  - 🆕 [Boost Transcription Accuracy](lemur/custom-vocab-lemur.ipynb)

- **Advanced Capabilities**
  - [Extract Dialogue Data](lemur/dialogue-data.ipynb)
  - 🆕 [Generate Custom Summaries](lemur/task-endpoint-custom-summary.ipynb)
  - 🆕 [AI Coaching with Task Endpoint](lemur/task-endpoint-ai-coach.ipynb)

---

## SDKs and Resources 📚
Extend your capabilities with SDKs and other tools.

- **SDKs**
  - [Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
  - [JavaScript SDK](https://github.com/AssemblyAI/assemblyai-node-sdk)

- **Community & Support**
  - [Discord](https://www.assemblyai.com/discord)
  - [YouTube](https://www.youtube.com/c/assemblyai)

---

### 📩 Questions?
Reach out to [support@assemblyai.com](mailto:support@assemblyai.com) for help!
