import argparse
import itertools
import socket
import threading


class Client:
    def __init__(self, n_threads, file):
        self.n_threads = n_threads
        self.file = file
        self.host = "localhost"
        self.port = 5000

    def get_urls(self):
        with open(self.file, "r", encoding="utf-8") as filed:
            for line in filed:
                yield line.strip()

    def get_client_socket(self):
        client_socket = socket.socket()
        client_socket.connect((self.host, self.port))
        return client_socket

    def process(self, urls):
        for url in urls:
            with self.get_client_socket() as client_socket:
                try:
                    client_socket.send(url.encode())
                    data = client_socket.recv(1024).decode()
                    if data:
                        print(data, flush=True)
                except ConnectionError:
                    print("Connection Failed", flush=True)

    def start(self):
        urls = self.get_urls()

        threads = [
            threading.Thread(target=self.process, args=(chunk,), )
            for chunk in self.separation(urls, self.n_threads)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    @staticmethod
    def separation(iterable, count):
        it_ = iter(iterable)
        item = list(itertools.islice(it_, count))
        while item:
            yield item
            item = list(itertools.islice(it_, count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n_threads', default=10, type=int)
    parser.add_argument('file', nargs='?', default='urls.txt', type=str)
    args = parser.parse_args()
    client = Client(args.n_threads, args.file)
    client.start()
