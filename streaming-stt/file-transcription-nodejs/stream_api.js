const WebSocket = require("ws");
const fs = require("fs");

const ASSEMBLY_API_KEY = 'YOUR_API_KEY';

if(ASSEMBLY_API_KEY === 'YOUR_API_KEY') {
  throw console.error("Please set your AssemblyAI API key in the ASSEMBLY_API_KEY variable.");
}

//How to transcribe a local file using the AssemblyAI stream API.
function transcribeFile(filePath) {

  //Initialize the websocket connection.
  const url = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=8000";
  const socket = new WebSocket(url, {
    headers: {
      Authorization: ASSEMBLY_API_KEY
    }
  });


  let transcriptText = "";

  //Declare socket callbacks.
  socket.onmessage = async (message) => {
    const res = JSON.parse(message.data.toString());

    if (res.message_type == "PartialTranscript") {
      //The partial transcript is the current best guess of the transcription.
      console.log("Partial Text:", res.text);
    }
    if (res.message_type == "FinalTranscript") {
      //The final transcript is the final transcription of the audio.
      console.log("Final Text:", res.text);
      transcriptText += res.text + " ";
    }

    switch (res.message_type) {
      case "SessionBegins":
        console.log("Session Begins");
        const data = fs.readFileSync(filePath);
        // Loop through data sending 2000 bytes at a time
        for (let i = 0; i < data.length; i += 2000) {
          const chunk = data.slice(i, i + 2000)

          if (chunk.length < 2000) {
            continue;
          }

          const audioData = chunk.toString("base64");

          socket.send(JSON.stringify({ audio_data: audioData }));

          await new Promise(resolve => setTimeout(resolve, 50));
        }
        //When all audio data has been chunked and sent, send the terminate_session message to close the stream.
        socket.send(JSON.stringify({terminate_session: true}));
    }
  };

  socket.onerror = (event) => {
    console.error(event);
  }
  
  socket.onclose = event => {
    // Write final transcript text to file
    fs.writeFile("./example.wav_transcript.txt", transcriptText, (err) => {
      if (err) throw err;
    })

    console.log(`Got socket close event type=${event.type} code=${event.code} reason="${event.reason}" wasClean=${event.wasClean}`);
  }

  socket.onopen = () => {
    this.state = "started";
    console.log("socket open");
  };

}


transcribeFile("./example.wav");