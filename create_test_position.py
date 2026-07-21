import asyncio

from app.core.database import SessionLocal
from app.models.position import Position


async def main():
    async with SessionLocal() as session:
        position = Position(
            name="Junior",
            description="An entry-level professional who has basic theoretical knowledge but limited real-world experience, typically between 0 to 2 years."
        )

        session.add(position)

        await session.commit()
        await session.refresh(position)

        print(f"Created position with id: {position.id}")


asyncio.run(main())