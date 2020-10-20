# LetMeHack


## Main File

server02.py is the main file. 

# Alumina Platform
This is a project based on creating and maintaining a alumni platform for old boys.

### Installing

A step by step series of examples that tell you have to get a development env
running

Say what the step will be

```
git clone git@github.com:SOCSSabaragamuwa/DeadLock.git
```

## Other

Request/Response Format
All requests and responses must be in JSON, with the Content-Type header set to application/json.

Error Handling

For API to be consistent, always return error responses in json. JSON schema of the errors returned should be like the following:
```
{
"status": 401,
"message": "Invalid username or password.",
"developerMessage": "Login attempt failed because the specified password is incorrect."
}
```
### Technology Stack

Python
