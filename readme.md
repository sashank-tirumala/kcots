# Auto-Generated ChatGPT docs

### Required Tools
- Python version 3.10
- Access to a terminal or command prompt

## Step 1: Setting Up Python & Virtual Environment

Ensure you have Python 3.10 installed. You can verify the installation by running the following command in your terminal:

```
python --version
```

or

```
python3 --version
```

### Creating a Virtual Environment

Once Python 3.10 is installed, navigate to the project directory and create a virtual environment. Here is how you can do it:

**For Windows:**

```
python -m venv venv
```

**For macOS/Linux:**

```
python3 -m venv venv
```

### Activating the Virtual Environment

Activate the virtual environment by running:

**Windows:**

```
.\venv\Scripts\activate
```

**macOS/Linux:**

```source
venv/bin/activate
```

## Step 2: Install Dependencies

With the virtual environment activated, install the project dependencies by running:

```
pip install -r requirements.txt
```

## Step 3: Setting Up Environment Variables

This project requires two environment variables: `OPENAI_API_KEY` and `NEWS_API_KEY`. These keys can be obtained by signing up for OpenAI and NewsAPI, respectively.

### Windows

Set the environment variables in Windows using the set command:

```
set OPENAI_API_KEY=your_openai_api_key_here
set NEWS_API_KEY=your_news_api_key_here
```

### macOS/Linux

On macOS or Linux, use the export command:

```
export OPENAI_API_KEY=your_openai_api_key_here
export NEWS_API_KEY=your_news_api_key_here
```

These environment variables are temporary and will need to be set again if you close your terminal or deactivate the virtual environment. To make them permanent, you can add them to your `.bashrc`, `.zshrc`, or appropriate shell configuration file.

## Step 4: Running the Project

With your environment prepared and dependencies installed, you can run the project scripts. Start by running the news aggregator:

```
python news_aggregator.py
```

After the news aggregator script completes, you can proceed to run the sentiment analysis:

```
python openai_sentiment_analysis.py
```

Congratulations! You've successfully set up and run the project.

## Troubleshooting

- Ensure that your Python version is 3.10 as required.
- Make sure the virtual environment is activated whenever you're working with the project.
- Verify that your `OPENAI_API_KEY` and `NEWS_API_KEY` are correctly set as environment variables.
- Check that all dependencies are correctly installed by reviewing the `requirements.txt` file.