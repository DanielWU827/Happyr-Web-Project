'''
The location for the Flask app interface for the project.
'''

from flask import Flask, render_template, request
from ProductionCode.random_memory import get_random_memory
from ProductionCode.datasource import DataSource
from ProductionCode.find_min_and_max_id import get_min_max_id
from ProductionCode import category_helper
from ProductionCode.lookup_memory import get_memory_text_by_id


app = Flask(__name__)
ds = DataSource()


@app.route('/', strict_slashes=False)
def homepage():
    '''
    Route to the landing page with instructions on how to navigate to the other pages.
    '''
    return render_template("index.html", title = "Happy Memories")


@app.route('/random', strict_slashes=False)
def generate_random_memory():
    '''
    Route to display a random happy memory, fetched from the database.
    '''
    memory_text = get_random_memory(ds)
    if memory_text:
        return render_template("random.html", memory = memory_text)
    return "No memories found in the database."


@app.route('/memory/<hm_id>', strict_slashes=False)
def show_memory_by_id(hm_id):
    '''
    Route to display a happy memory based on its corresponding ID.
    '''
    MinID, MaxID = get_min_max_id()
    error_message_string = f"Invalid memory ID. Please enter an integer between {MinID} and {MaxID}, inclusive."
    try:
        hm_id = int(hm_id)
    except ValueError:
        return error_message_string
    text = get_memory_text_by_id(ds, hm_id)
    return text if text else error_message_string

@app.route('/category', strict_slashes=False)
def story_in_category():
    '''
    Route to select memories from categories.
    '''
    user_choice = request.args.get('category_choice') 
    story_content = None
    if user_choice:
        story_content = category_helper.story_in_the_category(ds, user_choice)
    return render_template("category.html",
                           choice_category = user_choice,
                            category_list = category_helper.return_categories(ds),
                           story = story_content)

@app.route('/help', strict_slashes=False)
def help():
    '''
    Route to display the help page.
    '''
    return render_template("help.html")

@app.route('/trigger_500', strict_slashes=False)
def trigger_500():
    '''
    Route for testing internal server error.
    Purposefully raises an exception to test error handling.
    '''
    raise Exception("Intentional server crash for testing 500 error handling.")


@app.errorhandler(404)
def page_not_found(e):
    '''
    Handle the landing for pages that do not exist. 
    '''
    return render_template("404.html"), 404

@app.errorhandler(500)
def bug(e):
   '''
   Handle internal coding errors.
   '''
   return "Check the integrity of the file. Debug the code.", 500


if __name__== '__main__':
   app.run(host='0.0.0.0', port=5118)
