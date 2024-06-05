# Sample Code to Use Azure OpenAI Service's Whisper API from Python

This is a simple sample code that demonstrates how to use the Azure OpenAI Service's Whisper API to transcribe audio files using Python.

## Installation and Setup
1. Ensure you have Python installed on your machine.
2. Clone the repository and navigate to the project folder.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a `.env` file in the project directory and provide the necessary environment variables as mentioned below.

## Environment Variables
The following environment variables need to be set in the `.env` file:

- `OPENAI_API_TYPE`: The type of API for the Azure OpenAI Service. Choose one of the supported API types: 'azure', 'azure_ad', 'open_ai'.
- `OPENAI_API_HOST`: The API host endpoint for the Azure OpenAI Service.
- `OPENAI_API_KEY`: The API key for the Azure OpenAI Service.
- `OPENAI_API_VERSION`: The version of the Azure OpenAI Service API.
- `LANGUAGE`: The language parameter for the Azure OpenAI Service. Must be specified in ISO-639-1 format.
- `AZURE_DEPLOYMENT_ID`: The deployment ID for the Azure AI Studio.

## Code Explanation
1. First, the necessary libraries are imported: `openai`, `os`, `join` and `dirname` from `os.path`, and `load_dotenv` from `dotenv`.
2. The `.env` file is loaded to get the environment variables.
3. The parameters for the Azure OpenAI Service whisper are set based on the values read from the `.env` file.
4. The parameter values are confirmed by printing them.
5. The model engine name is specified as `whisper-1`.
6. An audio file is opened for transcription. Please note that the `maou_14_shining_star.m4a` file used in this code is copyrighted and can only be used as per the rules specified in the provided link.
7. The `transcribe` method of the `Audio` class from `openai` is executed with the specified parameters.
8. The resulting transcription text is printed.

Please make sure to replace the placeholder values in the `.env` file with your own valid API credentials and deployment information before running the code.

## Requirements
Make sure to add the following Python packages to your requirements.txt file:
```
openai >= 1.0.0
python-dotenv == 1.0.1
```

## Troubleshoot
If the REST API throws an exception and you get the following error, please refer to the instructions on how to deal with it and try to fix it.

- The API type provided in invalid. Please select one of the supported API types: 'azure', 'azure_ad', 'open_ai'
->Confirm the OPENAI_API_TYPE environment valiables.

- Access denied due to invalid subscription key or wrong API endpoint. Make sure to provide a valid key for an active subscription and use a correct regional API endpoint for your resource. 
 ->Confirm the OPENAI_API_HOST environment valiables.

- The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.
->Confirm the OPENAI_API_KEY environment valiables.

- Access denied due to invalid subscription key or wrong API endpoint. Make sure to provide a valid key for an active subscription and use a correct regional API endpoint for your resource.
->Confirm the OPENAI_API_KEY environment valiables.

- Resource not found error if you make a mistake
->Confirm the OPENAI_API_VERSION environment valiables.

- Invalid language 'japanese'. Language parameter must be specified in ISO-639-1 format.
->Confirm the LANGUAGE environment valiables.
  and, reffer to https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

- The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.
->Confirm the AZURE_DEPLOYMENT_ID environment valiables.

- Resource not found error
->I restarted Powershell running the Python commands and it fixed it. I don't know why, but I think it was probably an environment variable that was no longer being taken.

## Author
- potofo

## Revision
- 2023/10/08 01-00 @potofo: Initial Creation.
- 2024/06/05 01-01 @cnkang: Initial Creation.
  Updated openai package version in requirements.txt to openai >=1.0.
  Adjusted code to align with changes in the OpenAI API, ensuring compatibility with the new version.
  Tested all functionalities to ensure that existing features operate smoothly with the upgraded library.
- 2024/06/05 01-01 @potofo: Rename requirement.txt to requirements.txt


## License
This code is licensed under the MIT License.
