import base64
import mimetypes
import os
import struct
from typing import Dict, List, Optional
from google import genai
from google.genai import types


class TextToSpeechService:
    """Service for converting text to speech using Google's Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the TextToSpeechService with API key.
        
        Args:
            api_key (str, optional): Gemini API key. If not provided, will look for GEMINI_API_KEY env variable.
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or through GEMINI_API_KEY environment variable")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.5-flash-preview-tts"

    def save_binary_file(self, file_name: str, data: bytes) -> None:
        """Save binary data to a file.
        
        Args:
            file_name (str): Name of the file to save
            data (bytes): Binary data to save
        """
        with open(file_name, "wb") as f:
            f.write(data)
        print(f"File saved to: {file_name}")

    def convert_to_wav(self, audio_data: bytes, mime_type: str) -> bytes:
        """Generates a WAV file header for the given audio data and parameters.

        Args:
            audio_data (bytes): The raw audio data as a bytes object.
            mime_type (str): Mime type of the audio data.

        Returns:
            bytes: A bytes object representing the WAV file header.
        """
        parameters = self.parse_audio_mime_type(mime_type)
        bits_per_sample = parameters["bits_per_sample"]
        sample_rate = parameters["rate"]
        num_channels = 1
        data_size = len(audio_data)
        bytes_per_sample = bits_per_sample // 8
        block_align = num_channels * bytes_per_sample
        byte_rate = sample_rate * block_align
        chunk_size = 36 + data_size  # 36 bytes for header fields before data chunk size

        header = struct.pack(
            "<4sI4s4sIHHIIHH4sI",
            b"RIFF",          # ChunkID
            chunk_size,       # ChunkSize (total file size - 8 bytes)
            b"WAVE",          # Format
            b"fmt ",          # Subchunk1ID
            16,               # Subchunk1Size (16 for PCM)
            1,                # AudioFormat (1 for PCM)
            num_channels,     # NumChannels
            sample_rate,      # SampleRate
            byte_rate,        # ByteRate
            block_align,      # BlockAlign
            bits_per_sample,  # BitsPerSample
            b"data",          # Subchunk2ID
            data_size         # Subchunk2Size (size of audio data)
        )
        return header + audio_data

    def parse_audio_mime_type(self, mime_type: str) -> Dict[str, int]:
        """Parses bits per sample and rate from an audio MIME type string.

        Args:
            mime_type (str): The audio MIME type string (e.g., "audio/L16;rate=24000").

        Returns:
            dict: A dictionary with "bits_per_sample" and "rate" keys.
        """
        bits_per_sample = 16
        rate = 24000

        parts = mime_type.split(";")
        for param in parts:
            param = param.strip()
            if param.lower().startswith("rate="):
                try:
                    rate_str = param.split("=", 1)[1]
                    rate = int(rate_str)
                except (ValueError, IndexError):
                    pass
            elif param.startswith("audio/L"):
                try:
                    bits_per_sample = int(param.split("L", 1)[1])
                except (ValueError, IndexError):
                    pass

        return {"bits_per_sample": bits_per_sample, "rate": rate}

    def generate_speech(self, text: str, output_prefix: str = "output") -> None:
        """Generate speech from text using Gemini TTS.
        
        Args:
            text (str): Text to convert to speech
            output_prefix (str): Prefix for output files
        """
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=text)],
            ),
        ]
        
        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            response_modalities=["audio"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker="Speaker 1",
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name="Zephyr"
                                )
                            ),
                        ),
                        types.SpeakerVoiceConfig(
                            speaker="Speaker 2",
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name="Puck"
                                )
                            ),
                        ),
                    ]
                ),
            ),
        )

        file_index = 0
        for chunk in self.client.models.generate_content_stream(
            model=self.model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue
                
            if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
                file_name = f"{output_prefix}_{file_index}"
                file_index += 1
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                data_buffer = inline_data.data
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                
                if file_extension is None:
                    file_extension = ".wav"
                    data_buffer = self.convert_to_wav(inline_data.data, inline_data.mime_type)
                    
                self.save_binary_file(f"{file_name}{file_extension}", data_buffer)
            else:
                print(chunk.text)


class PodcastContentGenerator:
    """Service for generating podcast content using Google's Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PodcastContentGenerator with API key.
        
        Args:
            api_key (str, optional): Gemini API key. If not provided, will look for GEMINI_API_KEY env variable.
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or through GEMINI_API_KEY environment variable")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash"

    def generate_podcast_content(self, book_content: str) -> Dict:
        """Generate podcast content from book content.
        
        Args:
            book_content (str): The content of the book chapter to convert to podcast format.
            
        Returns:
            Dict: A dictionary containing the podcast metadata and script.
        """
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=book_content)],
            ),
        ]
        
        generate_content_config = types.GenerateContentConfig(
            temperature=1.5,
            response_mime_type="application/json",
        )

        response = ""
        for chunk in self.client.models.generate_content_stream(
            model=self.model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text

        try:
            return eval(response)  # Convert string response to dict
        except Exception as e:
            print(f"Error parsing response: {e}")
            return {}


if __name__ == "__main__":
    # Example usage of TextToSpeechService
    tts_service = TextToSpeechService()
    sample_text = """Read aloud in a warm, welcoming tone
    Speaker 1: Hello! We're excited to show you our native speech capabilities
    Speaker 2: Where you can direct a voice, create realistic dialog, and so much more. Edit these placeholders to get started."""
    tts_service.generate_speech(sample_text)

    # Example usage of PodcastContentGenerator
    podcast_generator = PodcastContentGenerator()
    # Add your book content here
    # podcast_content = podcast_generator.generate_podcast_content(book_content) 