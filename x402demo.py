import asyncio
from eth_account import Account
from x402.clients.httpx import x402HttpxClient

async def main():
    # Initialize account
    account = Account.from_key("764217ebff46faf0101b18d795d94bfb11863913fc16281a4b0a5b1a4c6853cb")

    # Create client and make request
    async with x402HttpxClient(account=account, base_url="https://api.example.com") as client:
        response = await client.get("https://www.x402.org/protected")
        print(await response.aread())

if __name__ == "__main__":
    asyncio.run(main())