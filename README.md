# Voice Cloning Tools


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)

<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT) -->
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)]( https://github.com/nsourlos/semi-automated_installation_exe_msi_files-Windows_10)

## **1. TTS Voice Cloning Documentation**

### Description

This [script](./tortoise_TTS_local.py) performs text-to-speech synthesis using the TTS (Text-to-Speech) library with two distinct models: XTTS v2.0.2 and Tortoise. The script also includes a utility function for converting MP3 files into segmented WAV files.

### Prerequisites

Before running the script, ensure that the TTS library is installed using the following command:

```
pip install TTS==0.22.0 transformers==4.37.2 torch torchaudio soundfile librosa
```

### Execution

```
python tortoise_TTS_local_best.py
```

### Tasks 

1. XTTS v2.0.2 Synthesis:

    - Utilizes the XTTS v2.0.2 model from the Coqui TTS library.
    - Performs text-to-speech synthesis with the specified input text.
    - Saves the synthesized audio to WAV files, both with and without sentence splitting.

2. MP3 to WAV Conversion

    - Converts an input MP3 file into segmented WAV files without using the pydub library. 
    - Segments the audio into 10-second intervals and saves them as individual WAV files (needed for Tortoise).

3. Tortoise Model Synthesis
Description:

    - Utilizes the Tortoise model from the Coqui TTS library for high-quality synthesis.
    - Loads the pre-trained Tortoise model and synthesizes speech based on the input text.
    - Saves the synthesized audio as a WAV file.

### Additional Information

XTTS v2.0.2 is suggested for its speed and reasonable quality.
Tortoise provides the best quality but has a longer inference time.

### Notes

- Ensure that dependencies are installed and file paths are adjusted accordingly.
- URLs in the comments provide more information about the models and configurations.
- Feel free to modify the script based on specific requirements, and ensure that necessary adjustments are made to file paths and dependencies for successful execution.








## **2. TTS Model Analyzer Documentation**

### Description

This [script](./TTS_download_and_test_all_models.py) analyzes the Text-to-Speech (TTS) models available in the TTS library, specifically focusing on their language support and vocoder capabilities. It categorizes models based on:

- **Multi-language vs. English-only**: Whether the model supports multiple languages or only English.
- **Custom vs. default English vocoder**: Whether the model has a custom English vocoder that allows for voice cloning or a default vocoder that doesn't.

The script also tracks the number of models with errors and those that are ignored due to specific reasons (e.g., known error-causing models).

### Code Breakdown

#### Prerequisites

Before running the script, ensure that the TTS library is installed using the following command:

```
pip install TTS==0.13.3
```

#### Execution

```
python TTS_download_and_test_all_models.py
```

#### Output
The script generates information about multi-language models with an English vocoder, English models with custom vocoders, multi-language models with default English vocoders, and English models with default English vocoders. Additionally, it identifies models that support non-English languages, models with errors, and models that should be ignored.

#### Script Explanation
The script performs the following tasks:

1. Imports necessary libraries (TTS, time, os).

2. Sets up a timer to measure script execution time.

3. Defines a sample text for speech synthesis.

4. Initializes counters and lists for various model categories.

5. Iterates through all available TTS models.

6. Downloads and loads each model to perform different text-to-speech tasks, categorizing them based on language support and vocoder types.

7. Prints the results, including the count and names of models in each category, along with any errors encountered during the process.

8. Displays the total number of models checked and the script execution time.

9. Performs an assertion check to ensure the correct counting of models.

10. Provides an example of using TTS for text-to-speech with a multi-speaker and multi-lingual model.

#### Notes
Some models may be ignored due to errors or other reasons (specified in the code).
The script also includes an example for Greek text-to-speech in Colab, using a specific model.

#### Additional Information
- TTS Library: https://github.com/mozilla/TTS
- TTS Documentation: https://tts.readthedocs.io/

Feel free to modify the script as needed for your specific use case or integrate it into your projects for TTS model analysis.


## **3. Voice Clone Using official Tortoise Repository**

### Overview

This [script](./tortoise_API.py) demonstrates the usage of Tortoise TTS (Text-to-Speech) system to generate speech from input text. The script utilizes the Tortoise TTS library and provides instructions for installation. The generated speech is saved as a WAV file.

### Installation

```bash
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
pip install -r requirements.txt
pip install librosa einops rotary_embedding_torch omegaconf pydub inflect
python setup.py install
```
### Usage

- Replace the path in voice variable with the desired speaker's voice samples.
- Optionally, modify the text variable to specify the desired input text.
- Run the script with ```python tortoise_API.py``` to perform Tortoise TTS and save the generated speech as a WAV file.

### Task Descritpion

1. Import Necessary Libraries:

    - Imports required libraries including torchaudio, tortoise.api, tortoise.utils, and os.
    
2. Initialize Tortoise TTS:

    - Initializes Tortoise TTS using tortoise.api.TextToSpeech.
    - Optionally, enables DeepSpeed for faster performance (commented out as it might be slower in practice).
3. Specify Input Text:

    - Sets the input text to be converted to speech.
4. Choose Preset and Voice:

    - Selects a preset mode for determining the quality of the output ("ultra_fast", "fast", "standard", or "high_quality").
    - Chooses a specific voice by providing the path to the speaker's voice samples.
5. Load Reference Clips:

    - Loads reference audio clips from the chosen voice path.
6. Perform TTS with Tortoise:

    - Utilizes Tortoise TTS to generate speech from the input text.
    - Saves the generated speech in WAV format.

### Additional Information
- The script downloads required models from the Hugging Face (HF) model hub.
- Adjust parameters such as preset and voice according to your preferences.
- The generated audio is saved as 'generated_hq_faceswap.wav' in the specified directory.



## **4. Opus to MP3 Conversion (for cloning from WhatsApp Recordings)**

### Overview

This [script](./opus_to_mp3_combine.py) facilitates the conversion of Opus audio files to MP3 format. It includes functions to read Opus files, convert them to MP3, and combine multiple MP3 files into a single file. The script provides flexibility by allowing users to specify input and output folders.

### Parameters

```opus_folder:``` Path to the folder containing Opus files.

```mp3_output_folder:``` Path to save individual MP3 files.

```combined_output_folder:``` Path to save the combined MP3 file.

The script creates output folders if they do not exist.

### Prerequisites

- **Dependencies:**
  - `os`
  - `soundfile`
  - `numpy`

### Tasks

1. Read Opus File:
    - Reads Opus files using the soundfile library.
    - Returns a NumPy array and the sample rate.
2. Convert Opus to MP3
    - Utilizes the read_opus function to read Opus files.
    - Converts Opus to MP3 using the same sample rate.
    - Saves the MP3 file to the specified output folder.
3. Convert Opus Files
   - Iterates through Opus files in a folder and converts each to MP3.
   - Returns a list of saved MP3 filenames.
4. Combine MP3 Files
    - Combines individual MP3 files into one.
    - Saves the combined MP3 file to the specified output folder.



## **5. Bark Google Colab (not very good)**

### Overview

This [jupyter notebook](./bark_colab.ipynb) demonstrates the process of cloning a voice using the Bark Voice Clone system. It involves mounting Google Drive to access audio samples for cloning, installing necessary libraries, loading models, generating semantic tokens, and finally, using these tokens for voice cloning.

### Tasks

1. **Mount Google Drive:**
   - Mounts Google Drive to access the folder containing voice samples to clone.

2. **Set Parameters:**
   - Defines parameters such as the path to the audio file, the name of the voice, and the output path for saving cloned voice prompts.

3. **Install and Import Libraries:**
   - Installs and imports required libraries, PyTorch, NumPy, and others.

4. **Install Bark with Voice Clone:**
   - Installs the Bark with Voice Clone library from the provided GitHub repository.

5. **Load Models and Initialize HuBERT:**
   - Loads necessary models and initializes the HuBERT manager for semantic token extraction.

6. **Load and Process Audio:**
   - Loads the audio file and converts it for further processing.
   - Extracts semantic vectors and tokens using the HuBERT model.

7. **Encode and Save Prompts:**
   - Encodes audio frames using EnCodec.
   - Saves fine, coarse, and semantic prompts as numpy arrays.

8. **Generate Audio Using Bark:**
   - Preloads Bark models for text, coarse, fine generation, and codec.
   - Generates audio using text prompts, semantic prompts, and history prompts.

9. **Play and Save Generated Audio:**
   - Plays the generated audio using IPython's Audio.
   - Optionally, saves the generated audio as a WAV file.

10. **Total Runtime:**
    - Displays the total time taken to execute the script.

### Script Usage

- Ensure Google Drive is mounted with access to the desired voice samples folder.
- Modify parameters such as `audio_filepath`, `voice_name`, and `output_path` according to your setup.
- Run the script to clone the voice, generate audio, and optionally save the output.

### Additional Information

- The script installs and uses the Bark with Voice Clone library from the provided GitHub repository.
- Adjust paths, parameters, and prompts as needed for your voice cloning project.
- Generated audio can be played directly or saved as a WAV file.
- Ensure that the necessary dependencies are installed and properly configured.


## **6. Coqui TTS calling API (not exist anymore - cannot be used)**

### Overview

This [script](./coqui_TTS_API_voice_cloning.py) showcases the process of cloning a voice using the Coqui TTS API. It involves importing necessary libraries, making API calls to clone a voice from an audio file, and generating text-to-speech using the cloned voice.

### Tasks

1. **Import Libraries:**
   - Imports required libraries, including `requests` for making API calls.

2. **Set Parameters:**
   - Sets parameters such as the path to the input audio file, the path to save the new audio file, and the text to be read.

3. **Call Coqui TTS API for Voice Cloning:**
   - Calls the Coqui TTS API to clone a voice from the provided audio file.
   - Extracts the voice ID of the cloned voice for subsequent text-to-speech.

4. **Call Coqui TTS API for Text-to-Speech:**
   - Calls the Coqui TTS API to convert the specified text into speech using the cloned voice.
   - Retrieves the audio URL of the generated speech.

5. **Download and Save Audio:**
   - Downloads the generated audio file from the provided URL.
   - Saves the audio file to the specified path.

### Script Usage

- Provide the path to the input audio file (`path_audio`), the path to save the new audio file (`save_path`), and the text to be read (`text_to_read`).
- Obtain the necessary API key from the Coqui TTS website and replace the placeholder in the `headers` with the actual key.
- Run the script to clone the voice and generate text-to-speech.

### Additional Information

- The script uses the Coqui TTS API for voice cloning and text-to-speech.
- Adjust parameters and replace the API key to suit your specific use case.
- Ensure that you comply with Coqui TTS API usage policies.
- Downloaded audio files are saved locally as specified in `save_path`.