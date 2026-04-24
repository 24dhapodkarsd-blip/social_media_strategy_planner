def judge_agent(client, content):

    prompt = f"""
    Review this social media content and give improvement suggestions:

    {content}
    """

    response = client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": "You are a marketing content reviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content