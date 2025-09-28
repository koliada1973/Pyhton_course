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
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
# # main()
# asyncio.run(main())


async def m(val):
    print('hello ...', val)
    await asyncio.sleep(1)
    print('... world !')
    return 'YES'

# asyncio.run(m())  # послідовне виконання
# asyncio.run(m())  # послідовне виконання

async def main_():

    # # await m() # послідовне виконання
    # # await m() # послідовне виконання
    task = asyncio.create_task(m('usd'))
    task1 = asyncio.create_task(m('eur'))
    await task 	# асинхронне виконання
    # await task1 	# асинхронне виконання

    # task = asyncio.create_task(main())
    # task = asyncio.create_task(main())
    # task = asyncio.create_task(main())
    # task = asyncio.create_task(main())
    # task = asyncio.create_task(main())
#
asyncio.run(main_())
