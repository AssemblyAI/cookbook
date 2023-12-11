## **Guide to Using Google Drive Links with AssemblyAI**

### **Step 1: Upload Your Audio File to Google Drive**

- **File Requirements**: Ensure your audio file is smaller than 100MB, as files larger than this cannot be directly downloaded from Google Drive links.  
- **Uploading**: Log into your Google Drive account and upload the audio file you want to use.

### **Step 2: Make Your File Publicly Accessible**

- **Right-Click** on the uploaded file in Google Drive.
- Select **'Get Link'**.
- Change the setting from “Restricted” to “Anyone with the link”. This makes the file publicly accessible.


### **Step 3: Obtain the Downloadable URL**

- Click on `Copy link` to copy your shared link.
- Initially, the shared link will look something like this: https://drive.google.com/file/d/1YvY3gX-4ZwY7K4r3J0THKNTvvolB3D-S/view?usp=sharing.
- To make it a downloadable link, modify it to this format:  
    `https://drive.google.com/u/0/uc?id=FILE_ID&export=download`.
- **Example**: If your shared link is `https://drive.google.com/file/d/1YvY3gX-4ZwY7K4r3J0THKNTvvolB3D-S/view?usp=sharing`,  
    change it to `https://drive.google.com/u/0/uc?id=1YvY3gX-4ZwY7K4r3J0THKNTvvolB3D-S&export=download`.

![Screenshot of Google Drive settings](https://cdn.discordapp.com/attachments/385968901797707783/1183781584491520082/image.png?ex=65899583&is=65772083&hm=99867e15b81e7b5e3917b2ae88367d8ab44a2de4613aa91e857938fc8f4b6120&)

### **Step 4: Use the URL with AssemblyAI**

- Now, you can use this downloadable link in your AssemblyAI API request. This URL directly points to your audio file, allowing AssemblyAI to access and process it.

```
transcriber = aai.Transcriber()  
  
audio_url = (  
"https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"  
)

transcript = transcriber.transcribe(audio_url)
```
### **Notes**

- **Security**: Ensure that sharing your audio file publicly complies with your privacy and security policies.
- If you prefer not to share your file publicly, you can [upload your file to our servers instead.](https://www.assemblyai.com/docs/guides/transcribing-an-audio-file#step-by-step-instructions)
- **File Format**: Check that your audio file is in a format supported by AssemblyAI.
