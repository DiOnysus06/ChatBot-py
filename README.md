# ChatGPT Python Script

This Python script is a simple chatbot using the **OpenAI GPT-3.5-turbo model**. It allows users to input text in a continuous loop, send queries to OpenAI's API, and receive responses from the model. The loop continues until the user types "exit."

## Requirements

Before running the script, ensure you have the following installed:

### Python Libraries:
- `openai`: To interact with OpenAI's GPT-3.5-turbo API.

To install the `openai` package, use the following command:

```bash
pip install openai
```

## How to Set Up

1. **Get an API Key**:
   - Sign up for an account on [OpenAI](https://platform.openai.com/).
   - Navigate to the [API Keys page](https://platform.openai.com/account/api-keys) and create a new API key.
   - Replace the placeholder `'YOUR_API_KEY'` in the code with your actual API key:
     ```python
     openai.api_key = 'your-api-key-here'
     ```

2. **Run the Script**:
   - Save the script in a `.py` file.
   - Run the script in a terminal or command prompt:
     ```bash
     python your_script.py
     ```

## Usage

### How It Works:
- The script sets up a continuous loop where the user can enter text-based queries.
- Each user message is appended to the `messages` list with the role `"user"`.
- The script sends the user's input to the OpenAI API using the `openai.ChatCompletion.create` method.
- The API responds with the model's message, which is then printed as `ChatGPT: {reply}`.
- The conversation history is maintained to provide context to the model for future messages.

### Exit Condition:
- To stop the conversation, type `exit`.
- The script will respond with "Goodbye!" and terminate the loop.

### Example Interaction:
```
User: Hello
ChatGPT: Hi! How can I assist you today?

User: What's the weather like?
ChatGPT: I don't have real-time information, but you can check a weather app for updates.

User: exit
ChatGPT: Goodbye!
```

## Error Handling

- If there's any issue with the API (e.g., incorrect API key or reaching the rate limit), the script will catch the exception and print an error message:
  ```
  An error occurred: {error_message}
  ```

## Notes

- **API Limitations**: Be aware of OpenAI’s API usage limits and pricing. You can monitor your API usage on the [OpenAI Dashboard](https://platform.openai.com/account/usage).
- **Message History**: The conversation is stored in the `messages` list. This helps the model maintain the context of the conversation for more intelligent responses.

---

### License

This script is provided for educational purposes. License provided by MIT.
