import os
import time
import threading
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import openai
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from email.mime.image import MIMEImage
import base64
import imghdr

# Set up GPT-3 API key
openai.api_key = "enter key here"

# Read topics from a text file
with open("topics.txt", "r") as file:
    topics = [line.strip() for line in file]

def generate_blog_post(topic):
    prompt = f"Enter Prompt Here"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3800,
        n=1,
        stop=None,
        temperature=0.8,
    )
    content = response.choices[0].text
    image_keyword_start = content.rfind("image keywords:")
    image_keywords = content[image_keyword_start + len("image keywords:"):].strip().split(', ')
    generated_content = content[:image_keyword_start].strip()

    # Remove the first line containing the topic
    generated_content = "\n".join(generated_content.split("\n")[1:])

    return generated_content, image_keywords

def send_email(blog_post, topic, service, image_keyword):
    message = MIMEMultipart()
    message["From"] = "Enter Email Address Here"
    message["To"] = "Enter Wordpress Email Address Here"
    message["Subject"] = f"{topic}"
    message.attach(MIMEText(blog_post, "html"))  # Change the MIME type to "html"

    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    send_message = (service.users().messages().send(userId="me", body=create_message).execute())

    print(F'sent message to {message["To"]} Message Id: {send_message["id"]}')

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://www.googleapis.com/auth/gmail.send'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

                                                    
def create_and_send_blog_post():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)
    topic = topics.pop(0)  # Get the first topic from the list and remove it

    # Update the topic file to remove the used topic
    with open("topics.txt", "w") as topic_file:
        for remaining_topic in topics:
            topic_file.write(f"{remaining_topic}\n")

    generated_content, image_keyword = generate_blog_post(topic)
    send_email(generated_content, topic, service, image_keyword)


# Schedule blog post creation and sending
schedule.every().day.at("08:00").do(create_and_send_blog_post)
schedule.every().day.at("14:00").do(create_and_send_blog_post)
schedule.every().day.at("20:00").do(create_and_send_blog_post)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

def user_input():
    while True:
        command = input("Enter 'send' to send a blog post instantly, or 'quit' to exit: ")
        if command.lower() == "send":
            create_and_send_blog_post()
        elif command.lower() == "quit":
            break

def send_multiple_blog_posts(num_posts):
    for _ in range(num_posts):
        create_and_send_blog_post()

def user_input():
    while True:
        command = input("Enter 'send' followed by a number to send that many blog posts instantly, 'send' to send a single blog post, or 'quit' to exit: ")
        command_parts = command.lower().split()
        if len(command_parts) == 1 and command_parts[0] == "send":
            create_and_send_blog_post()
        elif len(command_parts) == 2 and command_parts[0] == "send":
            try:
                num_posts = int(command_parts[1])
                send_multiple_blog_posts(num_posts)
            except ValueError:
                print("Invalid number. Please enter a valid number of blog posts to generate.")
        elif command.lower() == "quit":
            break

if __name__ == "__main__":
    scheduler_thread = threading.Thread(target=scheduler)
    scheduler_thread.start()
    user_input()
