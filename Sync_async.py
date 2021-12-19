import asyncio  
import time  
  
async def execute(delay, value):  
    await asyncio.sleep(delay)  
    print(value)  
  
async def main():  
    print(f"started at {time.strftime('%X')}")  
  
    await execute(10, 'Hemanth')  
    await execute(2, 'Loh')  
  
    print(f"finished at {time.strftime('%X')}")  
  
asyncio.run(main())  


'''
PS D:\Code_Place\2_test> python .\Sync_async.py
started at 22:45:29
Hemanth
Loh
finished at 22:45:41
PS D:\Code_Place\2_test> 
'''