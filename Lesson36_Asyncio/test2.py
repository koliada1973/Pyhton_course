import asyncio


async def find_divisibles(inrange, div_by):
    print(f"Пошук чисел у діапазоні {inrange}, що діляться на {div_by}")
    located = [i for i in range(inrange) if i % div_by == 0]
    for i in range(inrange):
        if i % 10000 == 0:
            await asyncio.sleep(0.00001)
    print(f"Виконано з числами в діапазоні {inrange}, що діляться на {div_by}")
    return located


async def main():
    # створюємо задачі
    divs1 = asyncio.create_task(find_divisibles(508000, 34113))
    divs2 = asyncio.create_task(find_divisibles(100052, 3210))
    divs3 = asyncio.create_task(find_divisibles(500, 3))

    # очікуємо завершення всіх
    results = await asyncio.gather(divs1, divs2, divs3)
    # return divs1, divs2, divs3
    return results

if __name__ == '__main__':
    # d1, d2, d3 = asyncio.run(main())
    # print(d1.result(), d2.result(), d3.result(), sep='\n')
    res = asyncio.run(main())
    print(res)