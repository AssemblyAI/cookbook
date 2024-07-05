# Iterate over Speaker Labels with Make.com

## Introduction

This is a quick guide on how to iterate over speaker labels in Make.com. This guide will return speaker labels as a readable format to a Google Doc. The end result will look like the two images below.

#### Make.com Scenario:

<img alt="make.com scenario on how to transcribe an audio with speaker labels using AssemblyAI" src="../guide-images/make-scenario.png">

#### Google Doc Transcript:

<img width="649" alt="A Google Doc with a transcript divided into speaker labels" src="../guide-images/make-final-transcript.png">

## Instructions

### Step 1: Transcribe the Audio
Create a scenario in Make.com. Add a new module. Search for and select the AssemblyAI app and select the "Transcribe an Audio File" module. Add an audio URL. Select speaker labels and other models you’d like to run. 

<img width="400" alt="image of Transcribe an Audio File module setup" src="../guide-images/make-transcribe-audio.png">

### Click Run once to retrieve data.

<img width="400" alt="image of make.com run button" src="../guide-images/make-run.png">


### Step 2: Wait for Completion
Next, add the “Wait until Transcript is Ready” module.

<img width="400" alt="image of “Wait until Transcript is Ready” module" src="../guide-images/make-wait-for-completion.png">

### Select "ID" from the “Transcribe an Audio” module as input for the Transcript ID field.
<img width="400" alt="select ID for transcription" src="../guide-images/make-get-id.png">

### Step 3: Get a Transcript
Next, add the “Get a Transcript” module and select "ID" from the “Transcribe an Audio” module as input for the Transcript ID field.

<img width="400" alt="image Get a Transcript module" src="../guide-images/make-get-transcript.png">

### Step 4: Create a Document
Search for and add the Google Docs app. From there choose the “Create a Document” module. Connect your Google account and name the Doc what you’d like. Add some filler content as well. Additionally, choose where you’d like the Doc to be located.

<img width="400" alt="image of the“Create a Document” module" src="../guide-images/make-create-doc.png">

### Step 5: Iterator Tool
Add the Iterator tool next. The speaker label data is in the utterances array. Select that array as input from the “Transcribe an Audio File" module. This tool will be used to perform a task for each utterance in the array. The next module will repeat its action for each utterance.

<img width="400" alt="image of iterator module" src="../guide-images/make-iterator.png">

### Step 6: Write Speaker Labels Data to Google Doc
Add a module and choose the “Insert a Paragraph” module from Google Docs. Connect your Google account if it’s not already connected (you may have to reconnect it if you get a failed to load error). In the “Select a Document” drop-down, choose "by mapping". In the Document ID input field select document ID from the “Create a document” module. For appended text, you can follow the format below for a readable format.

<img width="400" alt="image of insert a paragraph module" src="../guide-images/make-insert-paragraph.png">

### Step 7: Run the Scenario.
Run the scenario and you should get a Google Doc in your Drive with the speaker labels included.

<img width="400" alt="A Google Doc with a transcript divided into speaker labels" src="../guide-images/make-final-transcript.png">