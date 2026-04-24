def trend_agent(client, business_type):

    prompt = f"""
    Give 5 trending content ideas for a {business_type} business.
    Keep them short and practical.
    """

    response = client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": "You are a digital marketing expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content