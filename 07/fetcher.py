import argparse
import asyncio
import aiohttp


def get_urls(file):
    with open(file, "r", encoding="utf-8") as filed:
        for line in filed:
            yield line


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()

        return resp.status, len(data)


async def worker(queue, session):
    while True:
        url = await queue.get()
        try:
            res = await fetch_url(url, session)
            print(res)
        finally:
            queue.task_done()


async def fetch_batch_urls(queue, workers):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(queue, session)) for _ in range(workers)]
        await queue.join()

        for task in tasks:
            task.cancel()


async def main(file, workers):
    urls_queue = asyncio.Queue()

    for url in get_urls(file):
        await urls_queue.put(url)

    await fetch_batch_urls(urls_queue, workers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n_workers', default=10, type=int)
    parser.add_argument('file', nargs='?', default='urls.txt', type=str)
    args = parser.parse_args()
    asyncio.run(main(args.file, args.n_workers))
