# Detecting Low Confidence Words in a Transcript

In this guide, we'll show you how to detect sentences that contain words with low confidence scores. Confidence scores represent how confident the model was in predicting the transcribed word. Detecting words with low confidence scores can be important for manually editing transcripts. 
Each transcribed word will contain a corresponding confidence score between 0.0 (low confidence) and 1.0 (high confidence). 
You can decide what your confidence threshold will be when implementing this logic in your application. For this guide, we will use a threshold of 0.4.

## Getting Started

Before we begin, make sure you have an AssemblyAI account and an API key. You can sign up for an account and get your API key from your [dashboard](https://www.assemblyai.com/app/account). This guide will use AssemblyAI's [node SDK](https://github.com/AssemblyAI/assemblyai-node-sdk). If you haven't already, install the SDK by following these [instructions](https://github.com/AssemblyAI/assemblyai-node-sdk#installation).

## Step-by-Step Instructions

Import the AssemblyAI package and create an AssemblyAI object with your API key:

```javascript
import { AssemblyAI } from "assemblyai";

const client = new AssemblyAI({
  apiKey: process.env.ASSEMBLYAI_API_KEY,
});
```

Next create the transcript with your audio file, either via local audio file or URL (AssemblyAI's servers need to be able to access the URL, make sure the URL links to a downloadable file).

```javascript
const transcript = await client.transcripts.transcribe({
  audio_url: './sample.mp4',
})
```

From there use the `id` from the transcript to request the transcript broken down into sentences.

```javascript
let { id } = transcript
let { sentences } = await client.transcripts.sentences(id)
```

Set the confidence score threshold to a value of you choice (0.5 or less is a good start). In this guide, we'll use 0.4.

```javascript
let confidenceThreshold = 0.4
```

Next, we will filter the sentences array down to just sentences that contain words with confidence scores of under 0.4.


```javascript
const sentencesWithLowConfidenceWords = (sentences, confidenceThreshold) => {
  return sentences.filter(sentence => {
    const hasLowConfidenceWord = sentence.words.some(word => word.confidence < confidenceThreshold);
    return hasLowConfidenceWord;
  });
}

const filteredSentences = sentencesWithLowConfidenceWords(sentences, confidenceThreshold);
```

Next we'll alter the `filteredSentences` array so that the `words` array for each sentence only contains the words with confidence scores under of 0.4.

```javascript
const filterScores = filteredSentences.map(item => {return {...item, words: item.words.filter(word => word.confidence < confidenceThreshold)}})
```

Finally, we'll display the final results. The final results will include the timestamp of the sentence that contains low confidence words, the sentence, the words that scored poorly, and their scores. 

```javascript
//This function is optional but can be used to format the timestamps from milleseconds to HH:MM:SS
const formatMilliseconds = (milliseconds) => {
  // Calculate hours, minutes, and seconds
  const hours = Math.floor(milliseconds / 3600000);
  const minutes = Math.floor((milliseconds % 3600000) / 60000);
  const seconds = Math.floor((milliseconds % 60000) / 1000);

  // Ensure the values are displayed with leading zeros if needed
  const formattedHours = hours.toString().padStart(2, '0');
  const formattedMinutes = minutes.toString().padStart(2, '0');
  const formattedSeconds = seconds.toString().padStart(2, '0');

  return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

//Format the final results to contain the sentence, low confidence words, timestamps, and confidence scores.
const finalResults = filterScores.map(res => {
  return `The following sentence at timestamp ${formatMilliseconds(res.start)} contained low confidence words: ${res.text} \n  Low confidence word(s) from this sentence: ${res.words.map(res => {return `${res.text}[score: ${res.confidence}]`}).join(', ')}}`
})

console.log(finalResults) 
```
The output will look something like this:
 
```
[
  'The following sentence at timestamp 00:04:34 contained low confidence words: I am contacting you first when I could just have phoned my bank and marked you as fraud in an instant. \n' +
    '  Low confidence word(s) from this sentence: marked[score: 0.33049]}',
  'The following sentence at timestamp 00:06:40 contained low confidence words: Sabitha, as much as I would like to help you, this is the best I can do for you. \n' +
    '  Low confidence word(s) from this sentence: Sabitha,[score: 0.22706]}',
  'The following sentence at timestamp 00:07:37 contained low confidence words: Thank you for calling Queston. \n' +
    '  Low confidence word(s) from this sentence: Queston.[score: 0.16557]}'
]
```
