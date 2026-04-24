def scheduler_agent(client, platform):

    prompt = f"""
    Suggest a weekly posting schedule for {platform}.
    Include best days and times.
    """

    response = client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": "You are a social media strategist."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content