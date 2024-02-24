import os
import soundfile as sf
import numpy as np

def read_opus(opus_file_path):
    # Read Opus file using soundfile
    opus_data, sample_rate = sf.read(opus_file_path)
    
    # Convert to numpy array
    opus_np_array = np.array(opus_data)

    return opus_np_array, sample_rate

def convert_opus_to_mp3(opus_file_path, output_folder):
    opus_np_array, sample_rate = read_opus(opus_file_path)

    # Replace '.opus' extension with '.mp3'
    mp3_filename = os.path.splitext(os.path.basename(opus_file_path))[0] + '.mp3'
    output_mp3_path = os.path.join(output_folder, mp3_filename)

    # Save as MP3 using soundfile
    sf.write(output_mp3_path, opus_np_array, sample_rate)

    print(f"Conversion complete. MP3 file saved: {output_mp3_path}")

    return mp3_filename

def convert_opus_files(opus_folder, mp3_output_folder):
    mp3_files = []

    for filename in sorted(os.listdir(opus_folder)):
        if filename.endswith(".opus"):
            opus_file_path = os.path.join(opus_folder, filename)

            # Convert Opus to MP3 and save in the MP3 output folder
            mp3_filename = convert_opus_to_mp3(opus_file_path, mp3_output_folder)
            mp3_files.append(mp3_filename)

    return mp3_files

def combine_mp3_files(mp3_files, combined_output_folder):
    # Combine the MP3 files into one
    combined_mp3_filename = "opus_combined.mp3"
    combined_mp3_path = os.path.join(combined_output_folder, combined_mp3_filename)

    # Concatenate the individual MP3 files into one using soundfile
    combined_audio, combined_sample_rate = zip(*[sf.read(os.path.join(mp3_output_folder, mp3_file)) for mp3_file in mp3_files])
    combined_audio = np.concatenate(combined_audio)
    sf.write(combined_mp3_path, combined_audio, combined_sample_rate[0])  # Using sample rate from the first file

    print(f"Combination complete. Combined MP3 file saved: {combined_mp3_path}")

    return combined_mp3_filename

# Replace 'opus_folder' with the path to the folder containing your Opus files
opus_folder = "/home/soyrl/opus_files/"
# Replace 'mp3_output_folder' with the path to the folder for individual MP3 files
mp3_output_folder = "/home/soyrl/files_combined_mp3/"
# Replace 'combined_output_folder' with the path to the folder for the combined MP3 file
combined_output_folder = "/home/soyrl/"

# Ensure the output folders exist
os.makedirs(mp3_output_folder, exist_ok=True)
os.makedirs(combined_output_folder, exist_ok=True)

# Convert Opus files to MP3, get the list of saved MP3 files
saved_mp3_files = convert_opus_files(opus_folder, mp3_output_folder)

# Combine the MP3 files into one and get the combined MP3 filename
combined_mp3_filename = combine_mp3_files(saved_mp3_files, combined_output_folder)

# Print the list of saved MP3 files
print("List of saved MP3 files:")
for mp3_file in saved_mp3_files:
    print(os.path.join(mp3_output_folder, mp3_file))

# Print the path of the combined MP3 file
print(f"Combined MP3 file: {os.path.join(combined_output_folder, combined_mp3_filename)}")