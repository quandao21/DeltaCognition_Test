# Efficient Research Exploration: AI-Based Article Assessment and Summarization
> This is my solution for 3 days Take-home Challenge of Delta Cognition
---
## 1. Introduction

**1.1. Introduction:** You are an explorer who is constantly seeking out fresh information. As a scientist, you always learn about new issues through scientific study. But have you ever taken too long to decide whether you should read a certain article? Have you ever spent a lot of time reading an article only to discover that it didn't initially cover the topics you were interested in? Knowing this, I've brought a tool to make it easier for you to read the research. **We give you a way to summarize articles in a variety of ways and let you know whether or not you actually need to read this post**. Let's embark on this exploration and put this tool to the test.

**1.2. Work Flow:**

![Image](materials/Workflow.png)	
_Figure 1.1: Workflow of the project_

## 2. Set up for python

Install Python [(Setup instructions)](https://wiki.python.org/moin/BeginnersGuide)

**2.1. Create virtual environment**

If python's version is older than 3.3
```
pip install virtualenv
```
Create {env} virtual environment
```
python -m venv {env}
```

Activate virtual environment:
* Windows:
```
.\{env}\Scripts\activate
```
* macOS and Linux:
```
source {env}/bin/activate
```

**2.2. Install necessary libraries**

```
pip install -r api\requirements.txt
```

**2.3. Download a summarized model**

```
pip install -r saved_models\download_models.py
```

## 3. Running API

```
python api\main.py
```

## Running the Frontend
