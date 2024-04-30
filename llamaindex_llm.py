from llama_index.llms.openai_like import OpenAILike
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
"""主要用于获取访问大模型的client"""

from llama_index.llms.openai_like import OpenAILike
llamaindex_llm = OpenAILike(
    api_key="EMPTY", 
    api_base="http://10.58.253.38:9989/v1", 
    model="qwen",
    temperature="0.1", 
    max_tokens=512, 
    context_window=8192,
    is_chat_model=True, 
    timeout=60
)
Settings.llm = llamaindex_llm

# responses = llamaindex_llm.chat(messages=[ChatMessage(content="你好")])
