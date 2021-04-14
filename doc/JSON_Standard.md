# Authentication:   

## Login (POST)
* **Post**:
  - **email**: the user email
  - **password**: the hashed password (better to hash again on the backend for stronger security)   
  - example:
    <pre>
    { 
        "email": "example@email.com", 
        "password": "hashedPassword"
    }
    </pre>

* **Response**:
    - Status: The response result of the login.   
      - *SUCCESS*: if login verification passed.   
      - *USER_NOT_EXISTS*: if user email not exists in the database.
      - *INCORRECT_PASSWORD*: if the user exists but the password entered is incorrect. 
      - Server side may return other values but client side may not process the exception properly.   
    - example:   
        <pre>
        {
            "status": "SUCCESS/USER_NOT_EXISTS/INCORRECT_PASSWORD"
        }
        </pre>

## Register (POST)

* **Post**:   
    - **user_name**: the user name entered.
    - **phone**: the phone number entered.
    - **email**: the email entered;
    - **password**: once hash password entered.

* **Response**:   
    - Status: the response result of the register from server.
      - *SUCCESS*: if register success.
      - *USER_NAME_EXISTS*: if the username already exists in the database.
      - *EMAIL_EXISTS*: if the email already exists in the database.
      - *PHONE_EXISTS*: if the phone number already exists in the database.
      - *INVALID_DATA*: there maybe validation problem in the inputted data, make sure that client side has done validation check properly.