import schwabdev
from credentials import SCHWAB_APP_KEY, SCHWAB_APP_SECRET, REDIRECT_HOST

client = schwabdev.Client(SCHWAB_APP_KEY,SCHWAB_APP_SECRET,REDIRECT_HOST,"tokens.json")









#
# import os
# import base64
# import requests
# import webbrowser
# from loguru import logger
# from credentials import SCHWAB_APP_KEY, SCHWAB_APP_SECRET, REDIRECT_HOST
#
#
# def construct_init_auth_url() -> tuple[str, str, str]:
#
#
#     auth_url = f"https://api.schwabapi.com/v1/oauth/authorize?client_id={SCHWAB_APP_KEY}&redirect_uri={REDIRECT_HOST}"
#
#     logger.info("Click to authenticate:")
#     logger.info(auth_url)
#
#     return SCHWAB_APP_KEY, SCHWAB_APP_SECRET, auth_url
#
#
# def construct_headers_and_payload(returned_url, app_key, app_secret):
#     response_code = f"{returned_url[returned_url.index('code=') + 5: returned_url.index('%40')]}@"
#
#     credentials = f"{app_key}:{app_secret}"
#     base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
#         "utf-8"
#     )
#
#     headers = {
#         "Authorization": f"Basic {base64_credentials}",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#
#     payload = {
#         "grant_type": "authorization_code",
#         "code": response_code,
#         "redirect_uri": "https://127.0.0.1",
#     }
#
#     return headers, payload
#
#
# def retrieve_tokens(headers, payload) -> dict:
#     init_token_response = requests.post(
#         url="https://api.schwabapi.com/v1/oauth/token",
#         headers=headers,
#         data=payload,
#     )
#
#     init_tokens_dict = init_token_response.json()
#
#     return init_tokens_dict
#
#
# def main():
#     app_key, app_secret, cs_auth_url = construct_init_auth_url()
#     webbrowser.open(cs_auth_url)
#
#     logger.info("Paste Returned URL:")
#     returned_url = input()
#
#     init_token_headers, init_token_payload = construct_headers_and_payload(
#         returned_url, app_key, app_secret
#     )
#
#     init_tokens_dict = retrieve_tokens(
#         headers=init_token_headers, payload=init_token_payload
#     )
#
#     logger.debug(init_tokens_dict)
#
#     return "Done!"
#
#     symbol = 'AAPL'
#     r = c.get_quotes([symbol])
#     r.raise_for_status()
#
#     # Print the stock quote information
#     print(json.dumps(r.json(), indent=4))
#
#
#
#
# if __name__ == "__main__":
#     main()
#
#
#

