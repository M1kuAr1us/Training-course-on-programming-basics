import asyncio
import aiohttp
import aiofiles
import pathlib
import sys
import logging
from bs4 import BeautifulSoup

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

assert sys.version_info >= (3, 7)
here = pathlib.Path(__file__).parent

async def fetch_html(session, url):
    async with session.get(url, timeout=10) as response:
        response.raise_for_status()
        html = await response.text()
        logging.info(f"HTML received for {url}")
        return html

async def parse_links(html):
    links = set()
    soup = BeautifulSoup(html, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        links.add(a_tag['href'])
    logging.info(f"Found {len(links)} links")
    return links

async def save_links(file, source_url, links):
    async with aiofiles.open(file, mode="a", encoding="utf-8") as f:
        for link in links:
            await f.write(f"{source_url}\t{link}\n")
    logging.info(f"Saved {len(links)} links from {source_url}")

async def crawler_write(file, urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(handle_url(session, file, url))
        await asyncio.gather(*tasks)

async def handle_url(session, file, url):
    html = await fetch_html(session, url)
    if html:
        links = await parse_links(html)
        await save_links(file, url, links)

if __name__ == "__main__":
    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("found.txt")
    with open(outpath, "w", encoding="utf-8") as outfile:
        outfile.write("Source\tParsed link\n")

    asyncio.run(crawler_write(file=outpath, urls=urls))