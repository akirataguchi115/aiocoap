#!/usr/bin/env python3

# This file is part of the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

"""This is a usage example of aiocoap that demonstrates how to implement a
simple server. See the "Usage Examples" section in the aiocoap documentation
for some more information."""

import datetime
import logging

import asyncio

import aiocoap.resource as resource
from aiocoap import oscore_sitewrapper
import aiocoap
import aiocoap.edhoc


# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['.well-known', 'core'],
            resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['.well-known', 'edhoc'],
            aiocoap.edhoc.EdhocResource())

    server_credentials = aiocoap.credentials.CredentialsMap()

    root = oscore_sitewrapper.OscoreSiteWrapper(root, server_credentials)

    protocol = asyncio.get_event_loop().run_until_complete(aiocoap.Context.create_server_context(root))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
