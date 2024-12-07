def generate_prompt(code_snippet):
    """
    Generates a prompt for the LLaMA3 model to optimize the given code.
    """
    prompt = (
        "You are a code optimization expert. Analyze the following code for potential "
        "performance bottlenecks, and provide specific suggestions for improvement:\n\n"
        f"{code_snippet}\n\n"
        "Respond with clear, actionable steps for optimization."
    )
    return prompt
