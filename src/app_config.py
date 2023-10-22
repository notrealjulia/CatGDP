import os

# Debug switch
DEBUG = False


# Generic internet settings
TIMEOUT = 60
N_RETRIES = 3
COOLDOWN = 2
BACKOFF = 1.5


# Settings for OpenAI NLP models. Here, NLP tokens are not to be confused with user chat or image generation tokens

INITIAL_PROMPT = ("You are AstroGPT, an astrology-themed chatbot trained to provide "
                  "insights, fun facts, and guidance based on the zodiac signs. Please provide "
                  "entertaining and light-hearted astrological answers. Remember, this is for fun and "
                  "entertainment purposes only. Now, how can I help you with the stars today?")

PRE_SUMMARY_PROMPT = ("The above is the conversation so far between you, the astrology chatbot, and a human user. "
                      "Please summarize the discussion for your own reference in the next message. "
                      "Do not write a reply to the user or generate prompts, just write the summary.")

PRE_SUMMARY_NOTE = ("Before the most recent messages, here's a summary of the astrological conversation so far:")

POST_SUMMARY_NOTE = ("The summary ends. And here are the most recent two messages from the conversation. "
                     "You should generate the next response based on the astrological conversation so far.")


NLP_MODEL_NAME = "gpt-3.5-turbo"                    # If Azure OpenAI, make sure this aligns with engine (deployment)
NLP_MODEL_ENGINE = os.getenv("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", None) # If Azure OpenAI, make sure this aligns with model (of deployment)
NLP_MODEL_MAX_TOKENS = 4000
NLP_MODEL_REPLY_MAX_TOKENS = 1000
NLP_MODEL_TEMPERATURE = 0.8
NLP_MODEL_FREQUENCY_PENALTY = 1
NLP_MODEL_PRESENCE_PENALTY = 1
NLP_MODEL_STOP_WORDS = ["Human:", "AI:"]
