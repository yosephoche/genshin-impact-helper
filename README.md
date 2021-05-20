# Genshin Impact Check-In Helper

[Daily Check-In](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us)

[Original Repository (defunct)](https://github.com/y1ndan/genshin-impact-helper)

[TakaGG fork](https://github.com/takagg/genshin-impact-helper)

[Napkatti fork](https://github.com/napkatti/genshin-impact-helper/)

[am-steph fork (Heroku tutorial)](https://github.com/am-steph/genshin-impact-helper/tree/heroku)

## Usage

### Actions tutorial has been removed due to Github terms of service.

To run this script, please download the repository and schedule `notify.py` to run every day using an always-on PC, a Raspberry Pi, or cloud services such as Heroku etc.

You will need to set up the environment variables named `OS_COOKIE`, `USER_AGENT` (and optionally `DISCORD_WEBHOOK`)  
`USER_AGENT` is basically the identifier of the web browser that you are pretending to be when making the check-in request to Mihoyo's servers.  
Google "what is my user agent" and it should tell you (hint: it should begin with `Mozilla/5.0`)

If you are running it from a private PC, feel free to hard-code the cookie text into the script since the entire script will be private anyway.

***While it is certainly possible to re-enable the Github Actions workflow since the instructions are not buried particularly deep, do so at your own risk. You may face a ban from Github.***

## How to get your Cookies

1. Go to the Daily Check-In event website https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us
3. Log in with your MiHoYo/Genshin Impact account.  
   *If you have never checked in before, manually check in once to ensure that your cookies are set properly.*
4. Open the developer tools on your web browser (F12 on firefox/chrome)
5. Click on the "Console" tab
6. Type in `document.cookie` in the console
7. Copy the text output from the console  
   ![](https://imgur.com/eWP1OyO.png)
    - Remove any quotation marks "" at the front or end of the text 
    - Go back to the MiHoYo event website. You may close the tab but do not click the "Log Out" button because it may cause your cookie to expire.
    - **IF YOU WANT TO CHECK-IN MULTIPLE GENSHIN ACCOUNTS:**
    1. Paste your first cookie into the Value box on GitHub, but do not click "Add Secret" yet.
    2. Open a new private browsing / Incognito window
    3. Go to the MiHoYo event website on your new browser instance, and log in with your second account
    4. Copy the `document.cookie` as before
    5. Go back to the GitHub page, and type a hash `#` at the end of your first cookie
    6. Paste your second cookie immediately after the `#` and remove the quotation marks "" if needed
    
## How to get your Discord Webhook
This is an **OPTIONAL** step to let the script send you a notification on Discord whenever it runs a check-in.

Instructions provided by https://github.com/am-steph/genshin-impact-helper
1. Edit channel settings. (Create your own discord server or private channel for this)
   ![](https://i.imgur.com/Q0KFNzv.png)
2. Go into Integrations and view webhooks.
   ![](https://i.imgur.com/Z4pfACE.png)
3. Create a new webhook and copy the URL.
   ![](https://i.imgur.com/b3ZL3m3.png)
