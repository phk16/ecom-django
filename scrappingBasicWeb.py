import aiohttp
import asyncio
import random
import pandas as pd

# List of proxies (replace with your actual proxy IPs)
proxies = [
    "http://<proxy1-ip>:3128",
    "http://<proxy2-ip>:3128",
    "http://<proxy3-ip>:3128",
    # Add more proxies as needed
]

# Target URL for scraping
url = "https://example.com"

# List to store the results
results = []

# Function to make a request using a proxy
async def fetch_with_proxy(session, proxy):
    try:
        async with session.get(url, proxy=proxy) as response:
            data = {
                'proxy': proxy,
                'status_code': response.status,
                'url': response.url,
                'content': await response.text()[:100]  # Store the first 100 characters of the content
            }
            results.append(data)  # Append the result to the list
    except Exception as e:
        results.append({'proxy': proxy, 'status_code': None, 'url': None, 'content': str(e)})

# Function to run scraping concurrently
async def run_scraping():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):  # 100 requests in total (you can adjust this)
            proxy = random.choice(proxies)  # Randomly choose a proxy
            tasks.append(fetch_with_proxy(session, proxy))
        
        # Run all tasks concurrently
        await asyncio.gather(*tasks)

# Run the scraping function
asyncio.run(run_scraping())

# Convert results to DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv('scraping_results.csv', index=False)

# Print the DataFrame
print(df.head())
