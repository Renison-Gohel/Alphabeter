import os

import httpx
import asyncio

import sys

from alphabeter.helpers.gmail import is_email_registered
from alphabeter.helpers.utils import get_httpx_client


async def main():
    if not sys.argv[1:]:
        print("Please give an email address.")
        exit()

    as_client = get_httpx_client() # Async Client

    email = sys.argv[1]
    is_registered = await is_email_registered(as_client, email)

    print("Registered on Google :", is_registered)

asyncio.run(main()) # running our async code in a non-async code