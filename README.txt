# Cyber Security Engineering Project - Secure Flask Login Site

## Environment Setup

1. Clone or download my project code
2. Navigate to project directory:
  cd code

3. Download rockyou.txt under 'APPENDIX/code' in (https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt), 
you will get 'APPENDIX/code/rockyou.txt'

4. Create a virtual environment in Mac:
  python3 -m venv venv
  source venv/bin/activate

5. Install dependencies:
  pip install flask

6. Generate HTTPS certificate:
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes \-subj "/C=AU/ST=NSW/L=Sydney/O=FlaskTest/OU=Dev/CN=localhost" #Mac

  It will generate key.pem and cert.pem file.
  Note: If using Windows, install OpenSSL separately

## Run the Flask Server

```bash

## Before run my HTTP: you should go to my app.py and use line: app.run(debug=True) and comment this line of code:app.run(ssl_context=('cert.pem', 'key.pem'), debug=True).

7. Run in terminal: python app.py
You should click the link in your terminal: http://127.0.0.1:5000, 
Then you can see the login page like 'APPENDIX/screenshots/login' and register page like 'APPENDIX/screenshots/register'.

## Before run my HTTP: you should go to my app.py and use line: app.run(ssl_context=('cert.pem', 'key.pem'), debug=True) and comment this line of code: app.run(debug=True).
8. Run in terminal: python app.py
You should click the link in your terminal: https://127.0.0.1:5000, 
and you will go to my website and see a warning like 'APPENDIX/screenshots/warning'. And you should
click 'Advanced' button and click the bottom link: 'Proceed to 127.0.0.1(unsafe)'.

Then you can see the login page like 'APPENDIX/screenshots/login' and register page like 'APPENDIX/screenshots/register'.

9. Run in terminal: python3 database.py

Then I register twice, the user names are 'YoungOGGG' and 'YoungOG'. The passwords are both '123'.

10. Then I used Wireshark to capture the packets. I captured the packet with TCP protocol in HTTPS website and HTTP protocol in HTTP website. 
The example result in HTTPS is like 'APPENDIX/screenshots/wireshark_encrypted.png'.
The example result in HTTP is in 'APPENDIX/screenshots/wireshark_unencrypted.png'.

11. Then I use SQL injection, I use ‘' OR '1'='1’ as in the input, I can get all usernames and hashed-passwords in 'APPENDIX/screenshots/search.png'.
Attention: When using SQL injection, you should change the url to 'https://127.0.0.1:5000/search' in website and put ‘' OR '1'='1’ in the input like in 'APPENDIX/screenshots/search_input.png'.

12. After running 'attacker.py', you can see the real password like 'APPENDIX/screenshots/real_password.png'.
Attention: The value of 'target_hash' in the third line of the 'attacker.py' should be the value you captured in 'APPENDIX/screenshots/search.png'.

