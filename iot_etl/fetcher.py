import threading
import requests
import time
from datetime import datetime as dt

class IOTFetcher(threading.Thread):
    def __init__(self, url: str, interval: int, callback):
        super().__init__(daemon=True)
        self.url = url
        self.interval = interval 
        self.callback = callback
        self._stop_event = threading.Event()

    def run(self):
        while not self.stopped():
            try:
                r = requests.get(self.url, timeout=10)
                r.raise_for_status()
                raw = r.json()
                if self.callback:
                    self.callback(raw)
            except requests.RequestException as e:
                print(f"[IOTFetcher] request error at {dt.now().replace(microsecond=0)}: {e}")
            except Exception as e:
                print(f"[IOTFetcher] unexpected error at {dt.now().replace(microsecond=0)}: {e}")
            
            time.sleep(self.interval)

    def stop(self):
        self._stop_event.set()
    
    def stopped(self):
        return self._stop_event.is_set()
    



# if __name__ == "__main__":
#     fetcher = IOTFetcher(
#         url = " https://thingspeak.mathworks.com/channels/1293177/feeds/last.json",
#         interval = 5,
#         producer = None
#     )
    

#     fetcher.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Stopping fetcher...")
#         fetcher.stop()
#         fetcher.join()