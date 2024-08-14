from claude_api import Client

class ClaudeWrapper:
    def __init__(self, cookie):
        self.client = Client(cookie)

    class Messages:
        def __init__(self, client):
            self.client = client

        def create(self, model, max_tokens, temperature=0, system=None, messages=None):
            conversation_id = self.client.create_new_chat()['uuid']
            prompt = ""
            for message in messages:
                if message['role'] == 'user':
                    for content in message['content']:
                        if content['type'] == 'text':
                            prompt += content['text'] + "\n"
                        elif content['type'] == 'image':
                            attachment = content['source']['data']
                            response = self.client.send_message(prompt, conversation_id, attachment=attachment, system_prompt=system)
                            return response
            response = self.client.send_message(prompt, conversation_id, system_prompt=system)
            return response

    @property
    def messages(self):
        return self.Messages(self.client)
