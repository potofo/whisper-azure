# Simple sample code to use the Azure OpenAI Service's Whisper API from Python
# LICENSE:MIT License

# requirements python packages
# openai==0.28.1
# python-dotenv==1.0.0

import openai
import os
from os.path import join, dirname # for establish path
from dotenv import  load_dotenv   # for Loading .env file

# Get Environment Variables
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Set parameter of Azure OpenAI Service whisper
# The actual parameters are read from those stored in the .env file
# openai.api_type = 'azure'
# openai.api_base = "https://xxxxxxxx.openai.azure.com/"
# openai.api_key ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# openai.api_version ='2023-09-01-preview'
# deployment_id       = 'whisper'
# language            = 'ja'
# OPENAI_API_TYPE    : The API type provided in invalid. Please select one of the supported API types: 'azure', 'azure_ad', 'open_ai'
openai.api_type    = os.getenv("OPENAI_API_TYPE")
# OPENAI_API_HOST    : Access denied due to invalid subscription key or wrong API endpoint. Make sure to provide a valid key for an active subscription and use a correct regional API endpoint for your resource. 
openai.api_base    = os.getenv("OPENAI_API_HOST")
# OPENAI_API_KEY     : The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.
#                      Access denied due to invalid subscription key or wrong API endpoint. Make sure to provide a valid key for an active subscription and use a correct regional API endpoint for your resource.
openai.api_key     = os.getenv("OPENAI_API_KEY")
# OPENAI_API_VERSION : Resource not found error if you make a mistake
openai.api_version = os.getenv("OPENAI_API_VERSION") 
# LANGUAGE           : Invalid language 'japanese'. Language parameter must be specified in ISO-639-1 format.
language           = os.getenv("LANGUAGE")
# AZURE_DEPLOYMENT_ID: The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.
deployment_id      = os.getenv("AZURE_DEPLOYMENT_ID") # Deployment in Azure AI Studio

# Confirm Parameter of Azure openAI Service
print(f'api_type      :{openai.api_type}')
print(f'api_base      :{openai.api_base}')
print(f'api_key       :{openai.api_key}')
print(f'api_version   :{openai.api_version}')
print(f'language      :{language}')
print(f'deployment_id :{deployment_id}')

# Specify model engine name
# This parameter necessary always be whisper-1.
model_engine = 'whisper-1'

# Music files are copyrighted by MaouDamashii
# Redistribution and modification are permitted under the following rules page.
# https://maou.audio/rule/
audio_file= open("./maou_14_shining_star.m4a", "rb")

# Executing the transcribe method
transcript = openai.Audio.transcribe(model=model_engine,
                                    file=audio_file,
                                    deployment_id=deployment_id,
                                    language=language)

# Retrieve transcription results
print(str(transcript["text"]))
