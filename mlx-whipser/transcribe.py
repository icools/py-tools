import mlx_whisper
import sys

if len(sys.argv) < 2:
    print("Please provide the path to the audio file.")
    sys.exit(1)

file_path = sys.argv[1]

# Perform the transcription
result = mlx_whisper.transcribe(file_path, path_or_hf_repo="./whisper")

# Generate SRT format
def write_srt(transcription_result, srt_file_path):
    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        for idx, segment in enumerate(transcription_result['segments'], start=1):
            start_time = format_timestamp(segment['start'])
            end_time = format_timestamp(segment['end'])
            srt_file.write(f"{idx}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{segment['text']}\n\n")

# Helper function to format timestamp in SRT format
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Write the transcription result to an SRT file
if file_path.lower().endswith(".mp3"):
    srt_file_path = file_path.replace(".mp3", ".srt")
elif file_path.lower().endswith(".wav"):
    srt_file_path = file_path.replace(".wav", ".srt")
else:
    print("Unsupported file format. Please provide a .mp3 or .wav file.")
    sys.exit(1)

write_srt(result, srt_file_path)
print(f"SRT file saved as {srt_file_path}")