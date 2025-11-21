from ProductionCode.datasource import DataSource
import psycopg2


def get_memory_text_by_id(ds: DataSource, hm_id: int):
    """
    Inputs:
        ds (DataSource): an initialized DataSource object
        hm_id (int): the memory's primary key

    Returns: the memory text (hm) if found, otherwise None
    Purpose: Fetch a memory by ID
    """

    sql = """
        SELECT hm
        FROM hm_data
        WHERE hm_id = %s;
    """
    try:
        with ds.connection.cursor() as cur:
            cur.execute(sql, (hm_id,))
            row = cur.fetchone()
            return row[0] if row else None

    except psycopg2.Error as e:
        print("Database lookup error:", e)
        return None
