# Iterate over Speaker Labels with Make.com

## Introduction

This is a quick guide on how to iterate over speaker labels in Make.com. This guide will return speaker labels as a readable format to a Google Doc. The end result will look like the two images below.

#### Make.com Scenario:

![AD_4nXegtq2UpaHhC3djXpm95g6ev4F45H5z0Q7v6YR9ZheL6rB7JQu_FU1dBw_c9f2xasBoBfEJIXG-UkUzxTmNAV8jF8RhBqL_Q7ZXOxKfGX8XnaxfY3E05uxH](https://gist.github.com/assets/77217156/8bb036d7-bdc4-4d23-90ff-d2352d0eef36)

#### Google Doc Transcript:

<img width="649" alt="Speaker A Runner's knee runner's knee is a condition characterized by pain behind or around" src="https://gist.github.com/assets/77217156/b03ea259-b51b-48e5-acf0-d15e898f7270">

## Instructions

### Step 1: Transcribe the Audio
Create a scenario in Make.com. Add a new module. Search for and select the AssemblyAI app and select the "Transcribe an Audio File" module. Add an audio URL. Select speaker labels and other models you’d like to run. 

<img width="735" alt="AD_4nXc6CNRbFW1dgfID9u3FsmJaiSijT-NDFLtE5S8Me4rUH_zsZnZKHFHz7DCi0-FmW2YPvpT5gyu8YC6dwzQXc9QYaGBlH4Seuz0kLJnHYQkdERT-97dA4Hj6" src="https://gist.github.com/assets/77217156/e072926f-6fc6-4b2b-a312-9c366d3ed137">

### Click Run once to retrieve data.

<img width="365" alt="AD_4nXfCJw9bQaEJdUqgatNhGVE1yRyLLS_fE2CsGir6CvfzL-nkRqKoo8F0e7RRE6LMOhTequyzTub635Pz5ZDUN3CYFs9wq8x-mL0L7KQVv_iPag4FBnn195TO" src="https://gist.github.com/assets/77217156/dcf8fcce-68ca-44f5-88ce-1a9cde8fc6fc">


### Step 2: Wait for Completion
Next, add the “Wait until Transcript is Ready” module.

<img width="402" alt="AD_4nXd-jAG4sD6pnMp0mHa-8eWz3h_AzMyfaUiOhy7W8BBWORQnXy6UpVraH4XMapxBgnuzMvjLUNKeuvQP1UbBw3xqE53NhstH9mVCqU_jNbrlko4PRlua6WVJ" src="https://gist.github.com/assets/77217156/f7aebe61-91df-4210-bb0e-d2042a66ff7a">

### Select "ID" from the “Transcribe an Audio” module as input for the Transcript ID field.
<img width="560" alt="Search items" src="https://gist.github.com/assets/77217156/906c8f88-3df6-4731-979a-f5bfad961f0d">

### Step 3: Get a Transcript
Next, add the “Get a Transcript” module and select "ID" from the “Transcribe an Audio” module as input for the Transcript ID field.

<img width="739" alt="Get a Transcript" src="https://gist.github.com/assets/77217156/2318ba07-a217-4a2f-84ab-0260fdcb8408">

### Step 4: Create a Document
Search for and add the Google Docs app. From there choose the “Create a Document” module. Connect your Google account and name the Doc what you’d like. Add some filler content as well. Additionally, choose where you’d like the Doc to be located.

<img width="694" alt="AD_4nXeHToxlejkxkyTpXWI05XlfbA-195P0N1fMFsLSc-u9CxiMiraesCSqhXByAbB6Vqeeqb6Sr3Ws5Isz__hAOgDmnzOHK75hG4hJz10VMVBINBSl2kj9oFdM" src="https://gist.github.com/assets/77217156/c0853bd7-1f61-4359-9e72-260b904faa66">

### Step 5: Iterator Tool
Add the Iterator tool next. The speaker label data is in the utterances array. Select that array as input from the “Transcribe an Audio File" module. This tool will be used to perform a task for each utterance in the array. The next module will repeat its action for each utterance.

<img width="730" alt="Flow Control" src="https://gist.github.com/assets/77217156/e7677f22-bf18-4555-9d37-c6b8ec36af69">

### Step 6: Write Speaker Labels Data to Google Doc
Add a module and choose the “Insert a Paragraph” module from Google Docs. Connect your Google account if it’s not already connected (you may have to reconnect it if you get a failed to load error). In the “Select a Document” drop-down, choose "by mapping". In the Document ID input field select document ID from the “Create a document” module. For appended text, you can follow the format below for a readable format.

<img width="724" alt="AD_4nXdtIm8oyHXkiPwtHu5kbshDfQFcxJjK9Z1beBawfcfr4HVgxh_uCQABRXD-uUp2sHbRdk1LWcul3oVHYRBLijoGaBnv3lYZknohyJvSJBamACkEYK9A2ZLY" src="https://gist.github.com/assets/77217156/de444a27-bbeb-476c-96eb-519047e094d3">

### Step 7: Run the Scenario.
Run the scenario and you should get a Google Doc in your Drive with the speaker labels included.

<img width="649" alt="AD_4nXdixHKCSJg9pmslBhOl2bJBqw_MlA2negJZwe_mTVkC1rZ_i1JA-T7zMeSWo7cErMW_4gBWis23gdK3Wk1EQM4Oef-W1Cg90ZEtX8miEU_Cr4FqE4xKrCCc" src="https://gist.github.com/assets/77217156/d04d361f-48c8-4272-9729-fbddaa513606">