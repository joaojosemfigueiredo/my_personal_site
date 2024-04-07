# Personal Website

This repository contains the source code for my personal website. The site showcases information about myself, my skills in technology and electrical engineering, my projects, and a way to get in touch with me.
I have hosted my site on Heroku, and you can access it here: https://joaojosemfigueiredo-15f897af9875.herokuapp.com/

## Technologies Used

- **Flask**: A micro web framework for Python that was used to build the backend of the site.
- **HTML**: Markup for the content of the pages.
- **CSS**: Visual styles for the pages.

## Project Structure
- `static/`: This folder contains static files such as CSS, JavaScript, and images.
- `templates/`: Contains HTML templates which are rendered by Flask.
- `app.py`: The main application file for Flask that includes the routes and server logic.

## Changes Required in `personal.py` for Email Functionality to Work
To set up the email functionality in your Flask application, you'll need to generate an app-specific password for your Gmail account. This is necessary because the Flask-Mail extension uses your email account to send messages from the contact form on your website.

### Setting Up Email Functionality

1. Ensure two-step verification is enabled for your Google account: [Enable two-step verification](https://myaccount.google.com/security).
2. Visit the Google App passwords page: [Generate App passwords](https://myaccount.google.com/apppasswords).
3. In the "Select app and device" section, choose "Other (Custom name)", give it a name (e.g., "Flask Mail"), and click "Generate".
4. Google will generate a 16-character password. Copy this password.
5. In your `personal.py` file, change the `MAIL_PASSWORD` in line 11:

from:
```python
app.config['MAIL_PASSWORD'] = ''  # Replace with the generated app password
```
to:
```python
app.config['MAIL_PASSWORD'] = 'your_16-character_password'
```

Make sure to replace the placeholder text `your_16-character_password` with the actual app password generated from Google. This will help secure the application by using credentials specific to the app, minimizing the risk of compromising your Gmail account.


## Running the Site Locally

To run the site on your local machine, you'll need Python installed along with the Flask and Flask-Mail packages. Clone the repository, install the dependencies, and start the server using the following commands:

```bash
git clone https://github.com/your-username/my-personal-website.git
cd my-personal-website
pip install -r requirements.txt
flask run
```

After running these commands, the site will be available at http://127.0.0.1:5000/ in your browser.

Contact
If you have any questions or wish to get in touch with me, please do not hesitate to send me a message.

Name: João José Medeiros de Figueiredo
Email: joaojose.mdf@gmail.com
