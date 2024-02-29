"""
This script uses the OpenAI API to perform sentiment analysis on news articles. The news articles are stored in a JSON file
and the output is written to a text file.
"""

import json
from enum import Enum

import tqdm
from openai import OpenAI


class GPTModel(Enum):
    GPT4 = "gpt-4"
    GPT4_TURBO = "gpt-4-turbo-preview"
    GPT_3_5_TURBO = "gpt-3.5-turbo"


if __name__ == "__main__":
    client = OpenAI()
    system_message = "You are a stock market news assistant. You will be given news articles with a headline, a short description\
                    and you will need to provide a sentiment analysis of the article. The sentiment analysis should be\
                    one of the following: bullish, bearish, or none. You will also need to provide a confidence\
                    score for your sentiment analysis. The confidence score should be a number between 0 and 1. If the \
                    confidence score is 0, you are not confident in your sentiment analysis. If the confidence score is 1,\
                    you are very confident in your sentiment analysis. If the confidence score is between 0 and 1, you are\
                    somewhat confident in your sentiment analysis. A bullish sentiment means that you think the stock price\
                    will go up. A bearish sentiment means that you think the stock price will go down. A none sentiment\
                    means that you think the stock price will stay the same or the article is not related to a stock. News articles\
                    that are opinion pieces or editorials should be marked as none. News articles that indicate fraud in a company\
                    should be marked as bearish with a high confidence score. News articles that indicate a company is doing well\
                    should be marked as bullish with a high confidence score. Give a very short single sentence summary\
                    of your reasoning. Finally ensure that you start the response with the company name to make it easy to search through,\
                    In general you will response with :$COMPANY_NAME, $BULLISH_OR_BEARISH_SIGNAL, $CONFIDENCE SCORE, $ONE SENTENCE SYUMMARY For example, see the article below:\n \
                    Headline: Dixon Tech to ramp up smartphone mfg, plans Rs 400 crore capex in FY25\n\
                    Description: It’s currently building a capacity of 30 million smartphones across three of its four plants in Noida.\
                    Then you would respond with: Dixon Tech, bullish, 0.9, Dixon Tech is investing heavily in smartphone manufacturing"
    with open("news.json") as file:
        news = json.load(file)

    output = ""
    for article in tqdm.tqdm(news["articles"], desc="Analyzing news articles"):
        headline = article["title"]
        description = article["description"]
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": f"Headline: {headline}\nDescription: {description}",
                },
            ],
        )
        current_output = completion.choices[0].message.content
        output += current_output + ", " + article["url"] + "\n"

    with open("analysis.txt", "w") as file:
        file.write(output)
