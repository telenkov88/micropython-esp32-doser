import gc
import time
import asyncio

print("Extract app to flash")
extart_start = time.time()
from release_tag import *  # dinamically created in init.sh

# Application can be loaded from frozen module and written to flash.
# For startup optimization we're rewriting app only if it's different from current version.
with open("version.txt", "a+") as release:
    release_ver = release.read().rstrip()
print(f"Current app version: {release_ver}, frozen app version: {RELEASE_TAG}")
if RELEASE_TAG != release_ver:
    print("Rewrite app")
    import frozen_app

    with open("version.txt", "w") as release:
        release.write(RELEASE_TAG)

print(f"Finished in {time.time()-extart_start}sec")

from lib.servo42c import *
from config.pin_config import *


if __name__ == '__main__':
    gc.collect()
    print('Start')
    import connect_wifi
    import web

    loop = asyncio.get_event_loop()
    loop.run_forever()

