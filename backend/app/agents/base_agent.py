from openai import AzureOpenAI
import os
from dotenv import load_dotenv
from config.config import LLM_MODEL


class BaseAgent:
    """Base class for all agents in the system."""

    def __init__(self, model_name=LLM_MODEL, temperature=0.1):
        """
        Initialize the base agent with a language model.

        Args:
            model_name (str): The name of the model to use.
            temperature (float): Controls randomness in the model's output.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.client = self._init_client()

    def _init_client(self):
        """Initialize the Azure OpenAI client."""
        # Load environment variables
        load_dotenv()

        # Initialize Azure OpenAI client
        return AzureOpenAI(
            api_version="2024-02-15-preview",
            azure_endpoint="https://swisshacks-aoai-westeurope.openai.azure.com/",
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )

    def run(self, *args, **kwargs):
        """
        Run the agent. This method should be implemented by subclasses.

        Raises:
            NotImplementedError: If the subclass doesn't implement this method.
        """
        raise NotImplementedError("Subclasses must implement the 'run' method.")

    def get_completion(self, messages, temperature=None, response_format=None):
        """
        Get a completion from the Azure OpenAI API.

        Args:
            messages (list): List of message dictionaries with 'role' and 'content'.
            temperature (float, optional): Override the default temperature.

        Returns:
            str: The content of the completion.
        """
        if temperature is None:
            temperature = self.temperature

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            response_format=response_format,
        )

        return completion.choices[0].message.content
