# POST Standard

* Request Format  
  * from frontend to backend (request) : Use Form Data to do POST.
  * **examples**:   

    *frontend*:
    ```
        let form = new FormData();
        form.append('key', 'value');
        axios.post(this.$store.getters.URL + '/endpoint', form).then((response) => {
            ...
        }).catch((error) => {
            ...
        });
    ```

    *backend*:
    ```
        valueVar = request.form.get('key');
    ```
* Response Format
  * from backend to frontend (response) : Use JSON(jsonify) to respond.
  * Data body
    * "STATUS": return SUCCESS if everythings OK, otherwise return a code that represents the exceotion.
    * "STATUS_CODE": return 200 if everythings OK, otherwise return a HTTP Error code.
    * "DATA": the main data body going to respond.
  * examples:   

    backend:
    ```
        response = jsonify(
            {
                'STATUS': 'SUCCESS',
                'STATUS_CODE': 200,
                'DATA': {
                    'key1': 'val',
                    'key2': 123
                }
            }
        )
        response.status_code = 200
        return response
    ```

    frontend:
    ```
        axios.post(...).then(
            (response) => {
                if (response)
                let body = response.data;
                let data = body['DATA'];
                let val1 = data['key1'];
                let val2 = data['key2'];
            }
        )
    ```

## Login (POST)
* **Post**:
  - **email**: the user email
  - **pw**: the hashed password (better to hash again on the backend for stronger security)   
  - example:
    <pre>
    { 
        "email": "example@email.com", 
        "pw": "hashedPassword"
    }
    </pre>

* **Response**:
    - *STATUS*: The response result of the login.   
      - *SUCCESS*: if login verification passed.   
      - *USER_NOT_EXISTS*: if user email not exists in the database.
      - *INCORRECT_PASSWORD*: if the user exists but the password entered is incorrect. 
      - Server side may return other values but client side may not process the exception properly.   
    - *STATUS_CODE*: 200/403/500

## Register (POST)

* **Post**:   
    - **fName**: the user's first name.
    - **sName**: the user's last name.
    - **phone**: the phone number entered.
    - **email**: the email entered;
    - **password**: once hash password entered.

* **Response**:   
    - *STATUS*: the response result of the register from server.
      - *SUCCESS*: if register success.
      - *USER_NAME_EXISTS*: if the username already exists in the database.
      - *EMAIL_EXISTS*: if the email already exists in the database.
      - *PHONE_EXISTS*: if the phone number already exists in the database.
      - *INVALID_DATA*: there maybe validation problem in the inputted data, make sure that client side has done validation check properly.

    - STATUS_CODE: 200/500