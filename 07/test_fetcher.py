import asyncio
import os
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
import aiohttp
from fetcher import get_urls, fetch_url, fetch_batch_urls, worker


class TestFetcher(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_urls.txt"
        self.test_urls = [
            "https://www.youtube.com/",
            "https://aliexpress.ru/",
            "https://yandex.ru/",
        ]

        with open(self.test_file, "w", encoding="utf-8") as file:
            for url in self.test_urls:
                file.write(f"{url}\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_get_urls(self):
        urls = list(get_urls(self.test_file))
        expected_urls = [url + "\n" for url in self.test_urls]
        self.assertEqual(urls, expected_urls)

    async def test_fetch_url(self):
        url = 'http://test.com'
        session = MagicMock()
        session.get = AsyncMock(return_value=MagicMock(status=200, content=b'Test Content'))

        status, length = await fetch_url(url, session)

        self.assertEqual(status, 200)
        self.assertEqual(length, 12)

    @patch('aiohttp.ClientSession.get')
    async def test_worker(self, mock_get):
        queue = asyncio.Queue()
        await queue.put('http://test.com')
        session = aiohttp.ClientSession()

        mock_get.return_value = MagicMock(aiohttp.ClientResponse)
        mock_get.return_value.read.return_value = b'data'
        mock_get.return_value.status = 200

        await worker(queue, session)

        mock_get.assert_called_once_with('http://test.com')
        self.assertTrue(queue.empty())

    @patch('fetcher.worker')
    @patch('aiohttp.ClientSession')
    async def test_fetch_batch_urls(self, session_mock, worker_mock):
        session_mock.return_value.__aenter__.return_value = 'session'
        worker_mock.return_value = AsyncMock()

        queue = asyncio.Queue()
        await queue.put('http://example.com')
        await queue.put('http://example.org')

        await fetch_batch_urls(queue, 2)

        worker_mock.assert_called_with(queue, 'session')
        self.assertEqual(queue.qsize(), 0)
