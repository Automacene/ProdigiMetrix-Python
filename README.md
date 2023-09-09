# Prodigi Metrix

Prodigi Metrix stands as a robust metrics logging tool, tailored to address the practical needs of AI projects. With its user-friendly features, it simplifies the intricate process of data tracking and analysis, seamlessly recording Unix timestamps, monitoring prompt frequency, and meticulously logging keyword events. This tool proves indispensable in various AI applications, including plugins and chat apps, as it empowers developers to glean profound insights into user behavior.

## Table of Contents

- [Installation](#installation)
- [Available Metric Types](#available-metric-types)
- [Usage Examples](#usage-examples)
- [Milestones/Roadmap](#milestonesroadmap)

## Installation

To use this metrics logging tool, you can install it directly from GitHub using the following steps:

1. Open your terminal or command prompt.

2. Use the following command to install the tool via the `git+` method:
    
    `pip install git+https://github.com/Automacene/ProdigiMetrix-Python`

    It fetches the latest version of the tool directly from the GitHub repository and installs it directly.
3. Once installed, you can import and use the tool in your Python code as shown in the [Usage Examples](#usage-examples) section below.

## Available Metric Types

This tool provides several types of metrics for logging. Below are the available metric types:

#### Basic Metrics

The basic metrics feature of this tool primarily focuses on tracking Unix timestamps of prompts and the frequency of prompt occurrences. This simplicity is valuable for users who need a lightweight and straightforward method to record and monitor prompt interactions. By providing a fundamental understanding of when and how often prompts are triggered, basic metrics serve as a foundational component for analyzing user engagement and activity within your application or system

#### Keyword Metrics

While building upon the foundation of tracking Unix timestamps and prompt frequency like the basic metrics, the keyword metrics feature adds a powerful dimension by enabling users to submit keywords alongside timestamps. You can use this to either track endpoint activations to track feature usage or gain insights into what users are interested in by having ChatGPT sumamrize and submit keywords along with queries.

## Obtaining Credentials

To use Prodigi Metrix and access the logging capabilities, you will need to obtain API credentials. Since this is an early project, credential management is handled manually to ensure the quality and suitability of projects.

### Getting Approved

To request credentials, please send an email to `prodigilink [at] gmail [dot] com` with the following information:

- Your Name
- Your Email Address
- The Name of Your Project (Exactly as the public sees it; this will be used to generate the plugin ID)

I will review your project and evaluate its suitability for accessing the Prodigi Metrix API. I welcome projects of varying sizes and complexities; what matters most is your genuine interest and commitment to using the tool. Even if you only have a few users, as long as you have put work into an existing live project, I'll consider it seriously, no matter how crazy the idea is. I am prioritizing AI related projects, but if you think you are a really good fit anyways, just shoot me a message.

Once your project is approved, you will receive a Plugin ID (which should be kept private) and an authorization token (which should also be kept private). The Plugin ID allows you to keep separate project metrics if you have multiple projects. I will provide you with these credentials to start using Prodigi Metrix in your AI project. I look forward to collaborating with you and supporting your data tracking and analysis needs.

## Usage Examples

Here are some usage examples demonstrating how to use the main metric types provided by this tool:

### Basic Metrics

```python
from prodigi_metrix.resources.basic import Basic
import asyncio

# Replace with your actual plugin ID and auth token. Message Codie Petersen for an account.
plugin_id = "your-plugin-id"
auth_token = "your-auth-token"

def main():
    # Initialize the Basic Metrics resource
    basic = Basic(plugin_id, auth_token)

    # Log a basic event with the current timestamp
    asyncio.run(basic.log_now())
    print("Basic event logged successfully.")

    # Retrieve and display basic metrics for the plugin
    metrics = basic.get()
    print(metrics.json())

if __name__ == "__main__":
    main()
```

### Keyword Metrics

```python
from prodigi_metrix.resources.keyword import Keyword
import asyncio

# Replace with your actual plugin ID and auth token. Message Codie Petersen for an account.
plugin_id = "your-plugin-id"
auth_token = "your-auth-token"

def main():
    # Initialize the Keyword Metrics resource
    keyword = Keyword(plugin_id, auth_token)

    # Log a keyword event with the current timestamp and keywords
    asyncio.run(keyword.log_now(["test"]))
    print("Keyword event logged successfully.")

    # Retrieve and display keyword metrics for the plugin
    metrics = keyword.get()
    print(metrics.json())

if __name__ == "__main__":
    main()

```

## Milestones/Roadmap

I'm just testing the waters right now. But these are a couple of things I want to develop further if people are interested in the tool.

- Custom Metrics: Users can create their own metrics protocol and log them accordingly.
- Authentication: A method for users to identify themselves for your plugin to interact with.
- User Stats: User provided metrics.
- Many more to come...

If you have ideas, please make an '*Issue*' on the repo and explain the features you think would be nice.