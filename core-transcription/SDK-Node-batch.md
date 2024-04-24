# Transcribe Multiple Files Simultaneously Using the Node SDK

In this guide, we'll show you how to transcribe multiple files simultaneously using the Node SDK.

## Getting Started

Before we begin, make sure you have an AssemblyAI account and an API key. You can sign up for an account and get your API key from your [dashboard](https://www.assemblyai.com/app/account). This guide will use AssemblyAI's [node SDK](https://github.com/AssemblyAI/assemblyai-node-sdk). If you haven't already, install the SDK in your project by following these [instructions](https://github.com/AssemblyAI/assemblyai-node-sdk#installation).

## Step-by-Step Instructions

Set up your application folder structure by adding an audio folder which will house the files you would like to transcribe, a transcripts folder which will house your completed transcriptions, and a new `.js` file in the root of the project. Your file structure should look like this:  
```
BatchApp
├───audio
│   ├───audio-1.mp3
│   └───audio-2.mp3
├───transcripts
├───batch.js
```

In the `batch.js` file import the AssemblyAI package, as well as the node fs and node path packages. Create an AssemblyAI object with your API key:

```
import { AssemblyAI } from "assemblyai";
import * as path from 'path';
import * as fs from 'fs';

const client = new AssemblyAI({
  apiKey: <Your API Key>,
});
```

Declare the variables `audioFolder`, `files`, `filePathArr`, and `transcriptsFolder`.
* `audioFolder` will be the relative path to the folder containing your audio files.
* `files` will read the files in the audio folder, and return them in an array.
* `filePathArr` will join the file names with the audio folder name to create the relative path to each individual file.
* `transcriptsFolder` will be the relative path to the folder containing your transcription files.

```
const audioFolder = './audio';
const files = await fs.promises.readdir(audioFolder);
const filePathArr = files.map(file => path.join(audioFolder, file));
const transcriptsFolder = './transcripts';
```

Next, we'll create a promise that will submit the file path for transcription. Make sure to add the parameters for the models you would like to run.

```
const getTranscript = (filePath) => new Promise((resolve, reject) => {
  client.transcripts.transcribe({
    audio: filePath,
    language_detection: true
  })
  .then(result => resolve(result))
  .catch(error => reject(error));
});
```

Next, we will create an async function that will call the `getTranscript` function and write the transcription text from each audio file to an individual text file in the transcripts folder.

```
const processFile = async (file) => {
  const getFileName = file.split('audio/'); //Separate the folder name and file name into substrings
  const fileName = getFileName[1]; //Grab the 2nd substring which is the file name 
  const filePath = path.join(transcriptsFolder, `${fileName}.txt`); //Relative path for transcription text files.

  const transcript = await getTranscript(file); //Request the transcript
  const text = transcript.text; //Grab transcription text from the JSON response
 
  //Write the transcription text to a text file
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, text, err => {
      if (err) {
        reject(err);
        return;
      }

      resolve({
        ok: true,
        message: 'Text File created!'
      });
    });
  });
}
```

Next, we will create the run function. This function will:
* Create an array of unresolved promises with each promise requesting a transcript.
* Use `Promise.all` to iterate over the array of unresolved promises.

Then we'll call the run function
```
const run = async () => {
  const unresolvedPromises = filePathArr.map(processFile);
  await Promise.all(unresolvedPromises);
}

run()
```

Your final file will look like this:

```
import { AssemblyAI } from "assemblyai";
import * as path from 'path';
import * as fs from 'fs';

const client = new AssemblyAI({
  apiKey: <Your API>,
});

const audioFolder = './audio';
const files = await fs.promises.readdir(audioFolder);
const filePathArr = files.map(file => path.join(audioFolder, file));
const transcriptsFolder = './transcripts'

const getTranscript = (filePath) => new Promise((resolve, reject) => {
  client.transcripts.transcribe({
    audio: filePath,
    language_detection: true,
  })
  .then(result => resolve(result))
  .catch(error => reject(error));
});

const processFile = async (file) => {
  const getFileName = file.split('audio/')
  const fileName = getFileName[1]
  const filePath = path.join(transcriptsFolder, `${fileName}.txt`);

  const transcript = await getTranscript(file);
  const text = transcript.text
 
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, text, err => {
      if (err) {
        reject(err);
        return;
      }

      resolve({
        ok: true,
        message: 'Text File created!'
      });
    });
  });
}

const run = async () => {
  const unresolvedPromises = filePathArr.map(processFile);
  await Promise.all(unresolvedPromises);
}

run()
```

If you have any questions, please feel free to reach out to our Support team - support@assemblyai.com or in our Community Discord!
