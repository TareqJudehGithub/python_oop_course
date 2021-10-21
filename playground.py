# n = 3
# result = str()
# for i in range(1,n + 1):
#      result += str(i)
#
# print(result)

import asyncio


async def main():
    print('Hello, ....')
    await asyncio.sleep(1)
    print('.... world!')


if __name__ == "__main__":
    asyncio.run(main())
