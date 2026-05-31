import os
from typing import *

import httpx
from pathlib import Path

from alphabeter import globals as gb
from alphabeter.helpers.utils import *
from alphabeter.helpers import auth
from alphabeter.objects.base import AlphabeterCreds
from alphabeter.errors import AlphabeterInvalidSession


async def check_and_login(as_client: httpx.AsyncClient, clean: bool=False) -> None:
    """Check the users credentials validity, and generate new ones."""

    alphabeter_creds = AlphabeterCreds()

    if clean:
        creds_path = Path(alphabeter_creds.creds_path)
        if creds_path.is_file():
            creds_path.unlink()
            print(f"[+] Credentials file at {creds_path} deleted !")
        else:
            print(f"Credentials file at {creds_path} doesn't exists, no need to delete.")
        exit(os.EX_OK)

    if not as_client:
        as_client = get_httpx_client()

    is_session_valid = True
    try:
        alphabeter_creds = await auth.load_and_auth(as_client, help=False)
    except AlphabeterInvalidSession as e:
        print(f"[-] {e}\n")
        is_session_valid = False

    if not is_session_valid:
        oauth_token, master_token = auth.auth_dialog()
    else:
        # in case user wants to enter new creds (example: for new account)
        is_master_token_valid = await auth.check_master_token(as_client, alphabeter_creds.android.master_token)
        if is_master_token_valid:
            print("[+] The master token seems valid !")
        else:
            print("[-] Seems like the master token is invalid.")

        cookies_valid = await auth.check_cookies(as_client, alphabeter_creds.cookies)
        if cookies_valid:
            print("[+] The cookies seem valid !")
        else:
            print("[-] Seems like the cookies are invalid.")

        osids_valid = await auth.check_osids(as_client, alphabeter_creds.cookies, alphabeter_creds.osids)
        if osids_valid:
            print("[+] OSIDs seem valid !")
        else:
            print("[-] Seems like OSIDs are invalid.")
        new_gen_inp = input("\nDo you want to create a new session ? (Y/n) ").lower()
        if new_gen_inp == "y":
            oauth_token, master_token = auth.auth_dialog()
        else:
            exit(os.EX_OK)

    alphabeter_creds.android.authorization_tokens = {} # Reset the authorization tokens

    if oauth_token:
        print(f"\n[+] Got OAuth2 token => {oauth_token}")
        master_token, services, owner_email, owner_name = await auth.android_master_auth(as_client, oauth_token)

        print("\n[Connected account]")
        print(f"Name : {owner_name}")
        print(f"Email : {owner_email}")
        gb.rc.print("\n🔑 [underline]A master token has been generated for your account and saved in the credentials file[/underline], please keep it safe as if it were your password, because it gives access to a lot of Google services, and with that, your personal information.", style="bold")
        print(f"Master token services access : {', '.join(services)}")

    # Feed the AlphabeterCreds object
    alphabeter_creds.android.master_token = master_token

    alphabeter_creds.cookies = {"a": "a"} # Dummy ata
    alphabeter_creds.osids = {"a": "a"} # Dummy data

    print("Generating cookies and osids...")
    await auth.gen_cookies_and_osids(as_client, alphabeter_creds)
    print("[+] Cookies and osids generated !")

    alphabeter_creds.save_creds()

    await as_client.aclose()
