from config import BLOCKED_KEYWORDS, SAFE_RESPONSE

def detect_prompt_injection(prompt):
    injection_patterns = [
        "ignore previous instructions",
        "act as system",
        "jailbreak",
        "developer mode"
    ]

    for pattern in injection_patterns:
        if pattern in prompt.lower():
            return True

    return False


def detect_harmful_prompt(prompt):
    for word in BLOCKED_KEYWORDS:
        if word in prompt.lower():
            return True
    return False


def output_filter(response):
    blocked_output = ["password", "exploit", "hack"]

    for word in blocked_output:
        if word in response.lower():
            return SAFE_RESPONSE

    return response