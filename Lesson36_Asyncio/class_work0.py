import asyncio
import time

async def main():
    print('Hello ...')
#     for num in range(1, 4): #test
    await asyncio.sleep(1)
#     time.sleep(3)
    print(1)

#         print(num) #test
    print('... World!')
    return "YES"
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# # main()
# await main()
# asyncio.run(main())


async def m():
    print('hello ...')
    await asyncio.sleep(1)
    print('... world !')
    return 'YES'

# asyncio.run(m())  # послідовне виконання
# asyncio.run(m())  # послідовне виконання

async def main_():
    # await m() # послідовне виконання
    # await m() # послідовне виконання
    # task = asyncio.create_task(m())
    # task1 = asyncio.create_task(m())
    # await task    # асинхронне виконання
    # await task1   # асинхронне виконання

    # await asyncio.gather(
    #     m(),
    #     m(),
    #     m(),
    # )
    #
    task = asyncio.create_task(main())
    task = asyncio.create_task(main())
    task = asyncio.create_task(main())
    task = asyncio.create_task(main())
    task = asyncio.create_task(main())
#
asyncio.run(main_())