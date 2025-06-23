from typing import Any

from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class AgentCallBackHandler(BaseCallbackHandler):
    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],

        **kwargs: Any,
    ) ->Any:
        """Run when LLM start running"""
        print(f"**** Prompt to LLM was:***  \n{prompts[0]}")
        print("********")



    def on_llm_end(self,response: LLMResult,**kwargs: Any,)  -> Any:
        """Run when LLM ends running"""
        print(f"**** LLM Response ***:\n{response.generationsp[0][0].text}")
        print ("*******")
