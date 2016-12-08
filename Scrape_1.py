#!/usr/local/bin/python3.5

def fdaurl(pages):
    async def fetch(url, session):       
        async with session.get(url) as response:
            x = await response.read()
            return x

    async def run(loop,  r):
        url = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?page={}"
        tasks = []
        start = r[0]
        stop = r[1]
        async with ClientSession() as session:
            for i in range(start,stop,1):
                task = asyncio.ensure_future(fetch(url.format(i), session))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            
        def print_responses(result,pages):
            start = pages[0]
            end = pages[1]
            count = start
            for i in result:
                content = i
                filename = "data/"+"page_" + str(count) + ".txt"
                with open(filename,"wb") as f:
                    f.write(i)
                count += 1
                
        print_responses(responses,pages)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(loop, pages))
    loop.run_until_complete(future)

if __name__ == "__main__":
    import time
    import asyncio
    from aiohttp import ClientSession
    start = time.time()
    fdaurl([0,905])
    finish = time.time() - start
    print (finish)
