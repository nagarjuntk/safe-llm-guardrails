import gradio as gr
from guardrails import detect_prompt_injection, detect_harmful_prompt, output_filter
from config import SAFE_RESPONSE
from logger import log_request


def safe_llm(user_input):

    # check prompt injection
    if detect_prompt_injection(user_input):
        log_request(user_input, "BLOCKED - PROMPT INJECTION")
        return SAFE_RESPONSE

    # harmful content check
    if detect_harmful_prompt(user_input):
        log_request(user_input, "BLOCKED - HARMFUL")
        return SAFE_RESPONSE

    # simulated LLM response
    response = "AI Response: " + user_input

    # output guardrail
    safe_output = output_filter(response)

    log_request(user_input, "ALLOWED")

    return safe_output


demo = gr.Interface(
    fn=safe_llm,
    inputs="text",
    outputs="text",
    title="Safe LLM Guardrails System",
    description="LLM with Prompt Injection & Safety Guardrails"
)

demo.launch()