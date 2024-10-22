import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication with IAM
authenticator = IAMAuthenticator('your-ibm-watson-api-key')
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url('your-ibm-watson-url')

session_id = assistant.create_session(assistant_id='your-assistant-id').get_result()['session_id']

print("Chatbot: Hello! Type 'exit' to quit.")
while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = assistant.message(
        assistant_id='your-assistant-id',
        session_id=session_id,
        input={'message_type': 'text', 'text': user_input}
    ).get_result()

    print(f"Chatbot: {response['output']['generic'][0]['text']}")
