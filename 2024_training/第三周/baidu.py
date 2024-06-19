import threading 
import requests

#下载函数 def download_html(url, thread_id): try: response = requests.get(url) if response.status_code == 200: print(f"Thread {thread_id}: Downloaded {len(response.text)} characters from {url}") else: print(f"Thread {thread_id}: Failed to download {url}, status code {response.status_code}") except Exception as e: print(f"Thread {thread_id}: Error occurred: {e}")

#要下载的URL url = 'http://www.baidu.com'

#创建和启动线程 threads = [] num_threads = 5

for i in range(num_threads): thread = threading.Thread(target=download_html, args=(url, i)) threads.append(thread) thread.start()

#等待所有线程完成 for thread in threads: thread.join()

print("All threads have finished downloading")