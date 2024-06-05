import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Set parameters for Azure OpenAI Service Whisper
openai.api_type = os.getenv("OPENAI_API_TYPE", "azure")
openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = os.getenv("OPENAI_API_VERSION")
deployment_id = os.getenv("AZURE_DEPLOYMENT_ID")

# Confirm parameters of Azure OpenAI Service
parameters = {
    'api_type': openai.api_type,
    'azure_endpoint': openai.azure_endpoint,
    'api_key': openai.api_key,
    'api_version': openai.api_version,
    'deployment_id': deployment_id
}
for param, value in parameters.items():
    print(f'{param} : {value}')

# Music files are copyrighted by MaouDamashii
# Redistribution and modification are permitted under the following rules page.
# https://maou.audio/rule/
audio_file_path = "./maou_14_shining_star.m4a"
with open(audio_file_path, "rb") as audio_file:
    # Executing the transcribe method
    transcript = openai.audio.transcriptions.create(
        model=deployment_id,
        file=audio_file
    )
    # Retrieve and print transcription results
    print(transcript)
