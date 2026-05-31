import httpx

import asyncio
import sys

from alphabeter.apis.peoplepa import PeoplePaHttp
from alphabeter.objects.base import AlphabeterCreds
from alphabeter.helpers.utils import get_httpx_client


async def main():
    if not sys.argv[1:]:
        exit("Please give an email address.")
    email = sys.argv[1]

    alphabeter_creds = AlphabeterCreds()
    alphabeter_creds.load_creds() # Check creds (but it doesn't crash if they are invalid)

    as_client = get_httpx_client() # Async client

    people_api = PeoplePaHttp(alphabeter_creds)
    found, person = await people_api.people_lookup(as_client, email, params_template="just_name")
                                                                    # You can have multiple "params_template" for the Alphabeter APIs,
                                                                    # for example, on this endpoint, you have "just_gaia_id" by default,
                                                                    # "just_name" or "max_details" which is used in the email CLI module.

    print("Found :", found)
    if found:
        if "PROFILE" in person.names: # A specification of People API, there are different containers
                                          # A target may not exists globally, but only in your contacts,
                                          # so it will show you only the CONTACT container,
                                          # with the informations you submitted.
                                          # What we want here is the PROFILE container, with public infos.

            print("Name :", person.names["PROFILE"].fullname)
        else:
            print("Not existing globally.")

asyncio.run(main()) # running our async code in a non-async code