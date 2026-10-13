import gradio as gr
from guardrails import detect_prompt_injection, detect_harmful_prompt, output_filter
from config import SAFE_RESPONSE
from logger import log_request
from llm import get_llm_response


def safe_llm(user_input):

    # check prompt injection
    if detect_prompt_injection(user_input):
        log_request(user_input, "BLOCKED - PROMPT INJECTION")
        return SAFE_RESPONSE

    # harmful content check
    if detect_harmful_prompt(user_input):
        log_request(user_input, "BLOCKED - HARMFUL")
        return SAFE_RESPONSE

    # real LLM response
    try:
        response = get_llm_response(user_input)
    except Exception as e:
        log_request(user_input, f"ERROR - {e}")
        return "Sorry, something went wrong calling the model."

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