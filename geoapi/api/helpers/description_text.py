def api_description_text():
    return """<p style='font-size: 16px;'>A RESTful API 
    that returns geodata linked to an IP address by 
    leveraging the MaxMind GeoLite2 database. Familiarize 
    yourself with the API by clicking on the namespaces 
    and models below.</p>"""


def ns_geodata_description_text():
    return """<p style='font-size: 16px;'>The geodata \
    namespace contains the routes for the API. \
    <a href='#'>Click here</a> to view the routes.</p>"""


def create_account_description_text():
    return """<p style='font-size: 16px;'>Create an 
    account by making a POST request to this route. 
    The request payload must contain an email address, 
    password, and password confirmation. The API will 
    return a response with a payload containing the API 
    key and refresh API key needed to request data from 
    the API.</p>"""


def ns_user_description_text():
    return """<p style='font-size: 16px;'>The user \
    namespace contains the routes for user operations, \
    such as creating an account, refreshing an API key, \
    etc. <a href='#'>Click here</a> to view the routes.</p>"""


def get_new_api_description_text():
    return """<p style='font-size: 16px;'>Obtain a new API 
    key by making a GET request to this route. The request 
    must include the refresh API key in the header. The new 
    API key will be returned as the payload and the old API 
    key will be invalidated immediately.</p>"""


def forgot_api_keys_description_text():
    return """<p style='font-size: 16px;'>If you lose or
    forget your API keys, make a POST request to this route. 
    The request must contain the email address and password 
    that the account was created with. The API will return the 
    API key and refresh API as the response payload.</p>"""


def get_new_refresh_api_key_description_text():
    return """<p style='font-size: 16px;'>Obtain a new 
    refresh API key by making a POST request to this 
    route. The request must contain the email address 
    that the account was created with and the current 
    account password. The new refresh API key will be 
    returned as the response payload and the old refresh 
    API key will be invalidated immediately.</p>"""


def update_password_description_text():
    return """<p style='font-size: 16px;'>Make a POST 
    request to this route to update a password. The 
    request must contain the email address that the 
    account was created with, the current account password, 
    and a 'new_password' field containing the desired 
    new password. The new password must be between 8-64 
    characters. Upon successful completion of the request, 
    the API will return a success message and the old 
    password will be invalidated immediately.</p>"""


def get_geodata_description_text():
    return """<p style='font-size: 16px;'>Obtain geodata 
    from an IP address by making a GET request to this 
    route. The request must include the API key in the 
    header. The API will return the relevant geodata as 
    the payload.</p>"""
