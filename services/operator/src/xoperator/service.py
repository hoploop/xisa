# PYTHON IMPORTS
import os
import logging


# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.operator_pb2 import Answer, Question
from common.rpc.operator_pb2_grpc import OperatorServicer
from common.service import Service, ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# LIBRARY IMPORTS
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


log = logging.getLogger(__name__)


class OperatorServiceConfig(ServiceConfig):
    model: str
    huggingface:str
    database: MongodbConfig


class OperatorService(Service, OperatorServicer):

    def __init__(self, config: OperatorServiceConfig):
        OperatorServicer.__init__(self)
        Service.__init__(self)
        self.config: OperatorServiceConfig = config
        self.histories = {}

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)
        self.llm = self.get_llm_hf_inference()
        
        
    async def ask(self,request:Question,context) -> Answer:
        try:
            if request.session not in self.histories:
                self.histories[request.session] = []
            res, hist = self.get_response("empty",self.histories[request.session],request.message)
            self.histories[request.session] = hist
            return Answer(status=True,text=res)
        except Exception as e:
            log.warning(str(e))
            return Answer(status=False,message=str(e))
        

    def get_llm_hf_inference(self, max_new_tokens=128, temperature=0.1):
        """
        Returns a language model for HuggingFace inference.

        Parameters:
        - model_id (str): The ID of the HuggingFace model repository.
        - max_new_tokens (int): The maximum number of new tokens to generate.
        - temperature (float): The temperature for sampling from the model.

        Returns:
        - llm (HuggingFaceEndpoint): The language model for HuggingFace inference.
        """
        llm = HuggingFaceEndpoint(
            repo_id=self.config.model,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            huggingfacehub_api_token=self.config.huggingface
        )
        return llm
    
    def format_mistral_prompt(self,history):
        prompt = "<s>"
        for turn in history:
            if turn["role"] == "user":
                prompt += f"[INST] {turn['content']} [/INST]"
            elif turn["role"] == "assistant":
                prompt += f"{turn['content']} </s><s>"
        return prompt

   

    def get_response(
        self,
        system_message,
        chat_history,
        user_text,
        eos_token_id=["User"],
        max_new_tokens=256,
        get_llm_hf_kws={},
    ):
        """
        Generates a response from the chatbot model.

        Args:
            system_message (str): The system message for the conversation.
            chat_history (list): The list of previous chat messages.
            user_text (str): The user's input text.
            model_id (str, optional): The ID of the HuggingFace model to use.
            eos_token_id (list, optional): The list of end-of-sentence token IDs.
            max_new_tokens (int, optional): The maximum number of new tokens to generate.
            get_llm_hf_kws (dict, optional): Additional keyword arguments for the get_llm_hf function.

        Returns:
            tuple: A tuple containing the generated response and the updated chat history.
        """
        # Set up the model
        chat_history.append({"role": "user", "content": user_text})
        formatted_prompt = self.format_mistral_prompt(chat_history)

        response = self.llm(formatted_prompt, parameters={
            "max_new_tokens": 256,
            "temperature": 0.7,
            "do_sample": True,
            "stop": ["</s>"]
        })
        # Generate the response        
        chat_history.append({"role": "assistant", "content": response})
        return response, chat_history

    