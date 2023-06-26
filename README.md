# GPT-Blog-Poster
Using Gmail/GPT-3(4)/&amp;Wordpress to automatically post word content

Find your GPT Key here: https://platform.openai.com/account/api-keys

If you have GPT-4 access you can open Blog_publisher.py and change this to GPT-4

def generate_blog_post(topic):
    prompt = f"Enter Prompt Here"
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=3800,
        n=1,
        stop=None,
        temperature=0.8,

You can also change all the GPT settings above as well.
