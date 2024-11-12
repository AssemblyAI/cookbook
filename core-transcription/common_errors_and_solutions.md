# Guide to troubleshoot Common Errors

AssemblyAI's API always returns a response even when there is an error. This guide is designed to help you navigate and resolve common issues when implementing AssemblyAI.

## Understanding Errors with AssemblyAI

There are primarily two types of errors you might encounter when working with AssemblyAI:
- errors that occur when requesting a transcription
- errors that occur while the transcription is processing 

The first category includes issues such as authentication errors, invalid request parameters, or server-related errors, which are typically flagged immediately when you attempt to initiate a request.

The second category, failed transcription jobs, pertains to errors that occur during the transcription process itself. These might be due to issues with the audio file, unsupported languages, or internal errors on our end.

## Handling Errors with AssemblyAI

### Error handling with AssemblyAI's SDKs (Recommended)
When using any of our SDKs, both types of errors are surfaced via the error key in a transcript object. For example in Python:

```
if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
```

### Error handling with HTTPS requests
For errors when making a request for a transcription, you will have to check the status code that we respond with. For errors that occur during the transcription process, you will need to access the "error" key in the JSON response. For other HTTP errors you can print the information from the response object. Here is an example you can use:
```
if response.status_code != 200:
    try:
        print(response.json()['error'])
    except Exception:
        print(response.status_code, response.text, response.url)
```

## Common errors when making a request for a transcription

#### 1. Models are not Supported for a Particular Language

```
# Status code: 400
{  
"error": "The following models are not available in this language: speaker_labels"  
}
```

- **Solution**: Before you start, make sure to check our [Supported Languages page](https://www.assemblyai.com/docs/concepts/supported-languages). This page provides detailed information on what features are available for each language, helping you to choose the right options for your transcription or analysis needs.
#### 2. Insufficient Funds
```
# Status code: 400
{  
"error": "Your current account balance is negative. Please top up to continue using the API."  
}
```

**Solution**:
- **Auto-pay**: Enable auto-pay in your account settings to automatically add funds when your balance runs low.
- **Check Funds**: Regularly check your account balance to ensure you have sufficient funds for your transcription requests.
- **Add Funds**: If needed, add funds to your account to continue using our services without interruption.

#### 4. Invalid API Token
```
# Status code: 401
{  
"error": "Authentication error, API token missing/invalid."  
}
```
An invalid API token will prevent you from making successful requests.

**Solution**:
- Double-check that the API token you're using matches exactly with the token shown in your dashboard. Even a small typo can lead to authentication errors.

#### 5. Unsupported Characters in Custom Vocabulary
```
# Status code: 400
{  
"error": "'🇸🇬' was included in the word boost list but contains unsupported characters"  
}
```

Custom vocabulary only supports ASCII characters, but attempts to normalise text first before throwing an error. This error is usually caused by words or symbols that do not have an ASCII-equivalent.

**Solution**:
- Check that the word or phrase can be normalized prior to submitting it to Custom Vocabulary. Here is a code snippet that does this using Python's [unicodedata package](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize):
```

def filter_unsupported_characters(phrase):
    cleaned_phrase = `unicodedata.`normalize('NFKD', phrase).encode('ascii', 'ignore').decode('ascii')
    if len(cleaned_phrase) != len(phrase):
        raise Error("Unsupported characters in phrase")
    return cleaned_phrase
```
#### 6. Transcript ID not found
```
# Status code: 400
{  
"error": "Transcript lookup error, transcript id not found" 
}
```

**Solution**:
- **Verify the endpoint and method that you are using**: Check that you are making a `POST` request to `http://api.assemblyai.com/v2/transcript`or a `GET` request to `http://api.assemblyai.com/v2/transcript/{transcript_id}` and not `http://api.assemblyai.com/v2/transcript/`
- **Token Verification**: Double-check that the API token you're using matches exactly with the token used to make the original request.
- If you're using Postman, ensure that `Encode URL automatically` under Settings is **disabled**.
#### 7. Server Errors
```
# Status code: 500
{  
"error": "Server error, developers have been alerted." 
}
```

Server errors rarely happen but can occasionally occur on our side.

**Solution**:
- **Retries**: Implement retries in your code for when our server returns a 500 code response.
- **Automatic Retries**: Enable automatic retries for your transcription jobs under [Account > Settings](https://www.assemblyai.com/app/account) on your dashboard. This ensures that if a job fails due to a temporary server issue, it will automatically be retried.
- **Check our Status page** to verify that we are not currently undergoing an incident
- **Reach out to Support**: Remember to provide the transcript ID, audio file used, and parameters used in your request or the full JSON response in your message. You can also email support@assemblyai.com for help!

## Common transcription processing errors
#### 1. Audio File URL Errors

##### Attempting to transcribe webpages
```
{
  "status": "error",
  "audio_url": "https://www.youtube.com/watch?v=r8KTOBOMm0A",
  "error": "File does not appear to contain audio. File type is text/html (HTML document, ASCII text, with very long lines (56754)).",
  ...
}
```

Our API requires a publicly accessible URL that points to an audio file to retrieve your file for transcription. To transcribe a YouTube video, [check out this Cookbook](https://github.com/AssemblyAI/cookbook/blob/master/core-transcription/transcribe_youtube_videos.ipynb).

##### Attempting to transcribe audio files that are not accessible
```
{
  "status": "error",
  "audio_url": "https://foo.bar",
  "error": "Download error, unable to download https://foo.bar. Please make sure the file exists and is accessible from the internet.",
}
```

**Solution**:
- **Public Access**: Verify that the audio file URL is publicly accessible. Our servers cannot transcribe audio from private or restricted URLs.
- **Google Drive URLs**: For audio stored on Google Drive, consult our [Google Drive Transcription Cookbook](https://github.com/AssemblyAI/cookbook/blob/master/core-transcription/transcribing-google-drive-file.md) to correctly format your URLs for access.
- **Direct Upload**: Utilize the [AssemblyAI Upload endpoint](https://www.assemblyai.com/docs/api-reference/upload) to upload files directly from your device, eliminating the need for a public URL.
- **AWS S3 Pre-signed URLs**: [This Cookbook](https://github.com/AssemblyAI/cookbook/blob/master/core-transcription/transcribe_from_s3.ipynb) shows you how to use pre-signed URLs for AWS S3 storage to provide secure, temporary access for transcription without making your files public.

#### 2. Audio File Errors

##### Attempting to transcribe audio files that are too short
```
{
  "status": "error",
  "audio_url": "https://foo.bar",
  "error": "Audio duration is too short.",
}
```

The minimum audio duration for a file submitted to our API is 160ms.

**Solution**:
- **Add error handling for this error message**: When this error occurs, handle it safely by checking the error string and returning the error.
- **Add pre-submit checks for the duration of the audio file**: Prior to submitting a file for transcription, check the duration using a tool like soxi (part of the SoX package): `soxi -D audio.mp3`
