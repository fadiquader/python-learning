import asyncio
import aiohttp
from bs4 import BeautifulSoup


"""
Asynchronous programming allows you to write code that can run concurrently, 
enabling your program to handle multiple tasks at once without blocking. 
This is particularly useful for I/O-bound tasks, such as network requests or file operations, 
where waiting for a response can slow down your application.

Key Concepts
- Event Loop: The core of asynchronous programming. 
It manages the execution of asynchronous tasks and handles I/O operations without blocking.
- Coroutines: Special functions defined with async def that can be paused and resumed, allowing other tasks to run in the meantime.
- Await: The await keyword is used to pause the execution of a coroutine until a given task is complete.
Tasks: A way to schedule coroutines to run concurrently.
"""

# Basic Example
async def fetch_data(delay, data):
    print(f"Fetching {data}...")
    await asyncio.sleep(delay)  # Simulate an I/O operation
    print(f"Fetched {data}!")
    return data

async def main():
    # Schedule multiple coroutines to run concurrently
    task1 = asyncio.create_task(fetch_data(2, "Data 1"))
    task2 = asyncio.create_task(fetch_data(1, "Data 2"))

    # Wait for both tasks to complete
    result1 = await task1
    result2 = await task2

    print(f"Results: {result1}, {result2}")

# Run the main coroutine
asyncio.run(main())

# Web Scraping with Asynchronous Requests
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            return await response.text()

# Basic scrapper
async def scrapper(urls):
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, content in zip(urls, results):
        print(f"Fetched {len(content)} characters from {url}")

asyncio.run(scrapper(['https://example.com']))

# More advanced scrapper
async def fetch_page(session, url):
    """Fetch a web page and return its content."""
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Error fetching {url}: {response.status}")
            return None

async def get_title(url):
    """Get the title of a web page."""
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else 'No title found'
            return title
        return None

async def advanced_scrapper(urls):
    """Main function to fetch titles from multiple URLs."""
    tasks = [get_title(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, title in zip(urls, results):
        print(f"Title for {url}: {title}")


asyncio.run(advanced_scrapper([
    'https://www.example.com',
    'https://www.wikipedia.org',
    'https://www.python.org',
    'https://www.github.com',
    'https://www.reddit.com'
]))
