
README for Automated Blog Post Generation and Emailing
This python script uses GPT-3 for generating blog posts, emails them using the Gmail API, and sends the content to your Wordpress site through your Wordpress email. The script generates and sends the blog posts according to a predefined schedule.

Installation
You'll need Python 3.6 or later. If Python is not installed, you can download it from https://www.python.org/.

Required libraries:

openai
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
schedule
requests
threading
To install these, you can use pip, which is a package manager for Python:

bash
Copy code
pip install openai google-auth-oauthlib google-auth-httplib2 google-api-python-client schedule requests
Preparation
Before running the script, you need to do the following:

Create a file named "topics.txt" where each line is a blog post topic. The script will use these topics one by one to generate blog posts.

Register your application with the Google API. This process will provide you with a credentials.json file which you should put in the same directory as your script. If you need help doing this, you can follow the guide here: https://developers.google.com/workspace/guides/create-credentials.

Set your GPT-3 API key by replacing "enter key here" in the line openai.api_key = "enter key here". You can obtain this key by registering on the OpenAI platform.

Enter your email address and your WordPress email address in the send_email function where "Enter Email Address Here" and "Enter Wordpress Email Address Here" placeholders are found.

Adjust the schedule as per your needs. By default, it sends emails every day at 08:00, 14:00, and 20:00.

Running the script
To run the script, navigate to the directory where the script is located using a terminal and type:

bash
Copy code
python your_script_name.py
User Commands
While the script is running, you can interact with it via command line:

To send a single blog post instantly, type send and press enter.
To send multiple blog posts instantly, type send followed by the number of posts you want to send. For example, to send 5 posts, type send 5.
To quit the script, type quit and press enter.
Note: When you send an email for the first time, Google will ask you to authorize the app. Please follow the prompts to do so. The authorization token will be stored in 'token.json' for future use.

Getting the token.json from Google for the Gmail API
Use the Google Cloud Console to create a new Project or select an existing one.

Go to the APIs & Services Dashboard and select your project.

Click on "+ ENABLE APIS AND SERVICES" at the top of the page. Search for "Gmail API" and enable it for your project.

Click "Create credentials" on the right side of the page. Choose "Gmail API" for the API and "Web server (e.g. node.js, Tomcat)" for the place where you'll be calling the API from. Select "User data" as the kind of data you'll be accessing.

Click on "What credentials do I need?" and fill out the OAuth consent screen details. You'll also need to add your email address as a test user.

After saving, you'll be provided with an OAuth 2.0 client ID and secret. Download the JSON file and rename it to "credentials.json".

The first time you run your script, it will open a new window in your web browser and ask you to authorize access to your Gmail. After you authorize access, a token.json file will be created in your working directory. This file allows your script to access your Gmail account without asking for authorization every time.

Note: Keep your credentials.json and token.json files secure and do not share them. Anyone with access to these files can send emails from your Gmail account.

Getting Your WordPress Email to Post Credentials
WordPress provides a feature named "Post by Email" that allows you to post content via email. However, it requires using the Jetpack plugin and it is not as straightforward as just sending an email to your WordPress email address. Here's how to do it:

Log in to your WordPress admin dashboard.

Install and activate the Jetpack plugin if you haven't already. You can do this by going to Plugins -> Add New, then search for "Jetpack by WordPress.com". Click "Install Now" then "Activate".

Connect Jetpack to your WordPress.com account. If you don't have a WordPress.com account, you'll need to create one. This is necessary because the email servers used for the Post by Email feature are hosted on WordPress.com.

Once Jetpack is installed and connected, go to Jetpack -> Settings.

In the "Writing" tab, find the "Post by email" option and click "Enable".

After enabling, you should see a unique email address. This is the address you will use to send your blog post content. Every email sent to this address will create a new blog post.

Remember to keep this email address secure. Anyone who knows this email address can post to your blog. However, you can regenerate the email address at any time from the same settings page.

Additional Notes
This script currently does not handle the image keywords and does not use them in any way. You may modify the script to include relevant images in the blog posts.

Limitations and Recommendations
Make sure to handle the edge case where all the topics in the topics.txt file have been used. Currently, the script will give an index error if it runs out of topics.

The user input is expected to be in a specific format. Any deviation from it might lead to unexpected behavior. You may want to improve this to be more user-friendly or more robust against incorrect input.

You might want to include error handling for failed blog post generation or email sending attempts.

This script assumes that sending an email to your Wordpress email will result in a new blog post. This requires the Post-by-Email feature to be correctly set up on your Wordpress site. Make sure this is working as expected.

Customization
The script allows for customization:

If you want to use a different GPT-3 model, you can change the engine parameter in openai.Completion.create.

The max_tokens parameter in openai.Completion.create controls the length of the generated blog post. You can adjust this according to your needs.

The temperature parameter controls the randomness of the output. A higher value makes the output more random, while a lower value makes it more deterministic.

The prompt for the GPT-3 model is currently static. You could adjust the script to use different prompts for different topics.

Remember to always test your changes to make sure the script still works as expected.

Troubleshooting
If you get an error about missing packages, make sure you have installed all necessary packages with pip and that your Python environment has access to them.

If you get an error about unauthorized access from Google or OpenAI, make sure your credentials.json file and API key are correctly set up.

If your blog posts are not showing up on your Wordpress site, make sure the Post-by-Email feature is working correctly.

Contribution
Feel free to fork and contribute to this project. If you find any bugs or issues, you can raise an issue in the project repository.

License
This project is open-source and freely available to all. Use, distribute, and modify as you wish.
