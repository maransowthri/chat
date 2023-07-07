import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


while True:
	system_content_str = ''
	
	with open('content.txt') as system_content_file:
		system_content_str = system_content_file.read().replace('\n', '')

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": system_content_str},
			{"role": "user", "content": input('>> ')}
		]
	)

	print('>> ' + completion.choices[0].message.content)