

def return_categories(ds):
    '''
    Input: None. 
    Purpose: return the available categories. 
    Return: a list of all available categories in the database. 
    '''
    try:
        query = "Select Distinct hm_category from hm_data"
        cursor = ds.connection.cursor()
        cursor.execute(query)
        list_of_tuples = cursor.fetchall()
        return_list_of_category=[]
        for tuple in list_of_tuples:
            return_list_of_category.append(tuple[0])
        return return_list_of_category
    except Exception as e:
        return f"Error! Something is wrong with the database: {e}"

def story_in_the_category(ds,category):
    '''
    Input: datasource that helps connect with the server & the intended category. 
    Purpose: return a random story from a specific category. 
    Return: a happy memeory in that specific category.
    '''
    try:
        cursor = ds.connection.cursor()
    except Exception as e:
        return f"Error! Something is wrong with the database:{e}"
    categories = return_categories(ds)
    if category in categories:
        query = "Select hm From hm_data where hm_category = %s Order by Random() Limit 1"
        cursor = ds.connection.cursor()
        cursor.execute(query,(category,))
        row = cursor.fetchone()
        if row:
            return (row[0])
        else:
            return "No stories found in that category"
    else:
        return "Unsupported category name, use category command to see all available categories"





    