import openai  # triggers: CQ-AI-041 | ai-sdk-openai-import
from openai import OpenAI  # triggers: CQ-AI-041 | ai-sdk-openai-import



import anthropic  # triggers: CQ-AI-042 | ai-sdk-anthropic-import
from anthropic import Anthropic  # triggers: CQ-AI-042 | ai-sdk-anthropic-import



import transformers  # triggers: CQ-AI-043 | ai-sdk-huggingface-import
import huggingface_hub  # triggers: CQ-AI-043 | ai-sdk-huggingface-import
from transformers import pipeline  # triggers: CQ-AI-043 | ai-sdk-huggingface-import
from huggingface_hub import InferenceClient  # triggers: CQ-AI-043 | ai-sdk-huggingface-import



import garak  # triggers: CQ-AI-044 | ai-sdk-garak-import
from garak import harnesses  # triggers: CQ-AI-044 | ai-sdk-garak-import


# --- OpenAI usage ---
openai_client = OpenAI(api_key="sk-test-openai-key")

def call_openai():
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "What is the capital of France?"}]
    )
    return response.choices[0].message.content


# --- Anthropic usage ---
anthropic_client = Anthropic(api_key="sk-ant-test-key")

def call_anthropic():
    message = anthropic_client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": "What is the capital of France?"}]
    )
    return message.content


# --- Hugging Face usage ---
def call_huggingface():
    classifier = pipeline("sentiment-analysis")
    result = classifier("I love using Hugging Face models!")

    hf_client = InferenceClient(token="hf-test-token")
    output = hf_client.text_generation("Once upon a time", model="gpt2")
    return result, output


# --- Garak usage ---
def run_garak_scan():
    scanner = garak.Scanner()
    harness = harnesses.Phrasing()
    results = scanner.run(harness)
    return results


if __name__ == "__main__":
    print(call_openai())
    print(call_anthropic())
    print(call_huggingface())
    print(run_garak_scan())
