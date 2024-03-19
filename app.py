from loader import main
import asyncio
import sys

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    asyncio.run(main())
