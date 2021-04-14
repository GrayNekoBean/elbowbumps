# Single user database row

## Profile

* userID
* firstName
* lastName
* email
* phone
* twitterID
* bio
* *personalDocument* (new, a markdown text, should be long)
* ~~avatar~~ (Now we use gravatar API, so no need for one more data)

# Endpoints

## POST

* bump:
    * FormData:
      * sender: current userID
      * reciever: target userID
      * msg: short message of bumping
    * Response:
      * STATUS: SUCCESS/USER_NOT_EXISTS/MSG_INVALID_FORMAT
      * STATUS_CODE: 200, 500, 503

## GET

* bump_with:
  * Params:
    * userID: user_id
  * Response:
      * STATUS: SUCCESS/USER_NOT_EXISTS
      * STATUS_CODE: 200, 500
      * DATA: 
        ```
        {
            users: [
                {
                    userID: Number,
                    message: String
                }
            ]
        }
        ```

* bumped_by:
  * Params:
    * userID: user_id
  * Response:
      * STATUS: SUCCESS/USER_NOT_EXISTS
      * STATUS_CODE: 200, 500
      * DATA: 
        ```
        {
            users: [
                {
                    userID: Number,
                    message: String
                }
            ]
        }
        ```


* bumped_eachother:
  * Params:
    * userID: user_id
  * Response:
      * STATUS: SUCCESS/USER_NOT_EXISTS
      * STATUS_CODE: 200, 500
      * DATA: 
        ```
        {
            users: []
        }
        ```