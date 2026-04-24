def content_agent(client, trends, business_type, platform):

    prompt = f"""
    Create an engaging {platform} post for a {business_type}.
    Use these trends:
    {trends}

    Include:
    - Caption
    - 5 hashtags
    - Call to action
    """

    response = client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": "You are a social media content creator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content