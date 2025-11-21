# random_memory.py
import sys
from ProductionCode.datasource import DataSource

def get_random_memory(ds):
    """
    Input: DataSource object to connect to database
    Returns: The text (str) of one random happy memory from the database.
    Purpose: Fetch a random memory from the database. 
    """
    try:
        with ds.connection.cursor() as cur:
            cur.execute("""
                SELECT hm
                FROM hm_data
                ORDER BY RANDOM()
                LIMIT 1;
            """)
            row = cur.fetchone()
            return row[0] if row else None
    except Exception as e:
        print("Database error:", e)
        sys.exit(1)


def main():
    ds = DataSource()
    memory = get_random_memory(ds)
    if memory:
        print(memory)
    else:
        print("No memories found.")


if __name__ == "__main__":
    main()
