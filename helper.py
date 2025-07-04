import openai
from matcher import nlp, matcher, match_string

def get_response(doc):
    matches = matcher(doc)
    if not matches:
        return ""

    for match_id, start, end in matches:
        span = doc[start:end]
        sub = ["math", "arithmetic", "geometry", "algebra", "calculus", "science", "english", "history", "geography", "biology", "zoology", "botany", "chemistry", "physics"]
        if p := match_string(sub, doc[end:].text):
            r = ""
            for s in p:
                if r != "":
                    r += " and "
                r += s
            return f"Sure, I can help with {r}. What specifically do you need help with?"
        elif "capital" in span.text:
            return f"The capital of {span[-1].text} is a great question! Let me look that up for you."
        elif "what" in span.text and "is" in span.text or "define" in span.text:
            return f"{doc[end:].text} is a great question! Let me look that up for you. \n"
        elif "i" in span.text and "am" in span.text or "my" in span.text and "name" in span.text and "is" in span.text:
            return f"Hi {doc[-1]} I'm CYD! How can I be of assistance to you."
        elif "how" in span.text and "are" in span.text and "you" in span.text:
            return f"I'm feeling great today!..Thank you for asking. How about you ?! "
        elif "fine" in span.text or "good" in span.text or "fantastic" in span.text:
            return f"Fantastic!! So how can I help you today?"
        elif "solve" in span.text and "equation" in span.text:
            return "Sure, I can help solve the equation. Please provide the equation."
        elif "thank" in span.text or "thanks" in span.text:
            return "You are welcome..Can I help you with something else"

    return ""

def get_airesponse(userinput):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a homework helper."},
            {"role": "user", "content": userinput}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def homework_helper_bot(user_input):
    if user_input.lower() in ["exit", "quit", "bye", "no", "terminate"]:
        return "Goodbye! Have a great day!"
    elif user_input.lower() in ["hi", "hello", "bonjour", "hii"]:
        return "Hello! How can I help you today?"

    doc = nlp(user_input.lower())
    response = get_response(doc)
    if response == "" or "Let me look that up for you." in response:
        response += get_airesponse(user_input)
    return response
