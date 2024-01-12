from pydub import AudioSegment
import os
import math

def split_audio(input_file, output_folder, duration):
    audio = AudioSegment.from_mp3(input_file)
    total_length = len(audio)
    num_parts = math.ceil(total_length / (duration * 1000))
 
    for i in range(num_parts):
        start = i * duration * 1000
        end = (i + 1) * duration * 1000
        split_audio = audio[start:end]
        output_path = os.path.join(output_folder, f"part_{i+1}.mp3")
        split_audio.export(output_path, format="mp3")
        print(f"Exported {output_path}")

        total_length = len(audio)
        num_parts = math.ceil(total_length / (duration * 1000))

input_file = "audio.mp3"  # Replace with your input mp3 file
output_folder = "output"  # Output folder for the split audio files
duration = 30  # Duration in seconds for each split audio file
 
split_audio(input_file, output_folder, duration)