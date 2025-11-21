from ProductionCode.datasource import DataSource
import psycopg2

ds = DataSource()

def get_min_max_id():
    """Returns the minimum and maximum hm_id in the hm_data table."""
    try:
        with ds.connection.cursor() as cur:
            cur.execute("SELECT MIN(hm_id), MAX(hm_id) FROM hm_data;")
            row = cur.fetchone()
            if row:
                min_id, max_id = row
                return min_id, max_id
            else:
                return None, None
    except psycopg2.Error as e:
        print("Database lookup error:", e)
        return None, None