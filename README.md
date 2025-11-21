# Code authored and maintained by Leo Feingold, Alexei Mendez, Zheng Tan, Daniel Wu

# To connect to data:

\copy hm_data FROM 'Data/happydb/data/cleaned_hm.csv' DELIMITER ',' CSV HEADER
\copy writers_data FROM 'Data/happydb/data/demographic.csv' DELIMITER ',' CSV HEADER

# Commandline Usage

To get information on how to run the program:
python3 command_line.py --help

To access a random happy memory:
python3 command_line.py --random

To view the list of possible data categories:
python3 command_line.py --category

# Flask Usage

To begin the Flask session:
python3 flask_app.py

To open the website:
stearns.mathcs.carleton.edu:5118

# Data Statement

As of the Database deliverable, we have some excess data that we are not using.
Our plan for the future is to allow users to filter by demographic data.
However, this is currently unimplemented so writers_data table is unused.
Similarly, we plan on allowing users to filter by memory length and reflection period.
These features require the num_sentences and reflection_period parameters in hm_data

## Usability Principles

### Scanability

Each page uses clear headings (`<h1>` and `<h2>`) and consistent color themes to separate content. The purple and white contrast keeps the text readable, while margins and padding in the CSS prevent crowding. The navigation bar, mission section, and word cloud are visually distinct, making it easy for users to scan and locate what they need without reading every line.

### Satisficing

The interface makes it easy to reach a goal quickly. From the homepage, users can choose between three main actions: generating a random happy memory, filtering by category, or adding your own memory. Each button and link is labeled clearly and does exactly what it says. The user never has to overthink where to go or what a link means.

### Muddling Through

Users can explore and recover easily, even without instructions. Each page includes navigation links or a “Home” button for quick return. The help page explains all key features in plain language, and the 404 page offers clear next steps. These design choices make the site forgiving, intuitive, and easy to learn through exploration.

# Design improvements

1. Redundant commenting in test\_ files

Where to see the changes: in Tests/test_app and test_cl. We change lots of to make them look better

Most of our test functions used to contain an input and return statement. However, all of our tests were designed to be self-contained, and all of these functions took no inputs and returned no outputs.

This happened all throughout our two test\_ files and identifying each unique instance is difficult.

To fix this code smell, we shortened all of the docstrings to no longer include an input and return section. All test files now have a brief header that explains our choice to not include these frivolous albeit more thorough documentation.

2. Low color contrast on all pages

Where to see the changes: in static/datastyle.css line 11-16.

All of our pages had dark blue text on top of a light blue background. Users who have visibility issues or struggle to differentiate similar colors may have a difficult time navigating our website.

This happened all throughout our website across all pages.

To address this issue, we made the background blue lighter, to increase the contrast between the text and the background. Then, we ran our website through a third party accessibility checker to check that our color contrast was strong enough for all users to read our text.

3. Dynamic categories filtering

Where to see the change: in PrdocutionCode/category_helper line 3-19. We also make changes to commandline and the tests for it so that they fit with the new return_category function.

Our filters category selector is hard coded, instead of pulling from the database.

This change is specific to our Filters by Category page.

To fix this issue, we ensured that our category filter selector was dynamic, instead of static. Now, we pull from the database for all of the current categories, and list them there. In the future, if we choose to expand our database, the categories function will still work, even if we implement a feature in the future for people to add memories and be added to a "Miscellaneous" category. Furthermore, we updated the front end to replace underscores with spaces and capitalize the first letters of each category.

4. Redundant Variable Initialization and Numbers in Memory ID Validation

Where to see the changes: flask_app.py The route "/category" & The route "/memory/<hm_id>"

Some variables are initialized to None unnecessarily before immediately assigning them. And some routes used hard-coded ID boundaries in error messages instead of constant variable.

The route /category:
user_choice = None
user_choice = request.args.get('category_choice')

The route /memory/<hm_id>:
"Please enter an integer between 27673 and 128766"

To fix this issue, we deleted the redundant initialization, and dynamically fetch the values and set variables MaxID and MinID to store constants 27673 and 128766.

5. Alignment of componenets for the help page

Where to see the changes: in help.html line 27-33. In datastyle.css line 181-185.

In the original web page, the home button and the email address do not align with the texts above. It makes the help page look weird.

To fix it, we make the home button fixed at the lower left corner of the web page. We also changed the html structure so that the email address is included in the text paragraph.
