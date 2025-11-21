# User Analysis

## User Analysis for Command_line

### Potential Users

The two command line functions we design target at two main groups of users. The first group of users are people who do not have preferences on the types of happy moments they want to see and just want to see some random moments decribed by other people. The second group of users are people who have specific preferences on certain types of happy moments they want to see, and as a result can request to see the possible memory categories.

### Potential Benefits

The random function can print out a random happy moment from the database. The category function prints each category. These two functions provide the users with two different ways to interact with the large database. A user may be happy or pleasently surprised by a moment brought by the randomness.

### Potential Harms/Exclusion

#### First Assumption

The users know about the form and data type for the correct input. It is hard for first-time users. If they don't know the form to type in correct input, they can't use these functions to interact with the database. Therefore, there is a help function and useful output when the input is invalid. The README file also provides useful information to correctly use these functions.

#### Second Assumption

The users can see the output on the screen. For people who have vision problems, these functions lose their original meanings. We have discussed building a function to read the output using some AI resources. If it can be accomplished, then the functions can be adapted to more people.

#### Third Assumption

Users understand the purpose and connection between “random” and “category” functions. A user might wonder: “Does the random story come from all categories or just one?” or “What do these categories represent?” This uncertainty can make the interface feel confusing. To solve this problem, we added more descriptive comments and short explanations that appear when users call these functions. We also updated the README to clarify their purpose.

There may be other possible exclusion such that people who may not feel comfortable reading other people's happy memories as it may trigger sad feelings or FOMO.

## User Analysis for Flask App

### Overview

This Flask app allows users to explore a dataset of happy moments through a simple web interface. It builds on earlier command-line functionality to make interaction easier and more visual.

### Potential Users

The app serves three main groups of users:

1. Casual users who want to see a random happy moment.
2. Users who want to browse moments by category.
3. Users interested in specific entries or database exploration.

Each of the four routes (`/random`, `/category`, `/memory/<id>`, and `/<row>/<column>`) supports one of these user goals.

### Potential Benefits

The random route gives users a spontaneous and enjoyable experience.  
The category route shows all available types of happy moments for easier browsing.  
The ID and cell routes allow precise data access for users who want to look deeper into the dataset.

### Assumptions (CIDER)

**Assumption 1:** Users understand the structure of the dataset, including what an ID or a cell position means.  
_Critique:_ This may exclude users unfamiliar with data formats.  
_Design Fix:_ Add a search or browse feature so users can find entries without knowing specific IDs.

**Assumption 2:** All happy moments are appropriate for all users.  
_Critique:_ Some entries might include sensitive or unwanted content.  
_Design Fix:_ Add a keyword filter or content preference option.

**Assumption 3:** Categories are specific and meaningful for all users.  
_Critique:_ Categories may be too broad or general.  
_Design Fix:_ Add subcategories or more detailed filtering options.

### Potential Harms and Exclusions

Users who do not understand the dataset structure may not be able to use the ID or cell routes effectively.  
Randomly generated results could include content that some users find inappropriate.  
Overly broad categories could make it hard for users to find specific types of happy moments.

## User analysis for Database Deliverable:

This database is designed to store, categorize, and retrieve happy memories. While the current structure enables efficient querying and filtering, it also embeds several assumptions about users, data, and memory representation. Below, we identify and critique those assumptions using the CIDER framework and propose design alternatives.

### Potential Users
Contributors — individuals who wish to record and preserve their happy memories for future reflection or sharing.

Explorers — users who enjoy browsing and discovering others’ memories, either for inspiration or emotional connection.

Analysts/Designers — researchers or developers interested in studying emotional data patterns, linguistic diversity, or interface usability based on memory entries.

### Potential Benefits
For contributors, it offers a structured yet personal space to capture and revisit meaningful experiences.

For explorers, it transforms the dataset into a source of empathy and positivity, allowing them to navigate through shared emotions by category, tag, or keyword.

For analysts or designers, it presents a rich dataset for testing human-centered design hypotheses and refining how digital systems represent emotional data.

## Assumptions (CIDER)

### Assumption 1: There is a single correct category for each memory

**Critique:** The database stores only one category per memory, which implies that emotional experiences can be placed into a single label such as "family" or "achievement." In reality, memories often relate to multiple themes at once. Storing only one category oversimplifies the emotional context and can misrepresent the lived experience.  
**Design Fix:** Allow memories to have multiple tags by using a many-to-many relationship between categories and memories. This would better support overlapping themes and provide more flexible search options.

### Assumption 2: All users express their memories in similar language

**Critique:** The database assumes that users will describe memories in a consistent or comparable way. However, writing styles vary significantly based on age, culture, personality, and language background. This can bias filtering and analysis tasks that rely on keyword searches or text pattern matching.  
**Design Fix:** Provide optional structured metadata such as mood selectors or short thematic checkboxes. This allows users with different communication styles to participate fully and creates a more accessible dataset for analysis.

### Assumption 3: Recently added or randomly surfaced memories are the most relevant

**Critique:** If the system primarily uses recency or randomness to decide which memories to show, some entries may rarely or never be viewed. This means that visibility is based on chance instead of emotional significance or user preference.  
**Design Fix:** Support additional retrieval modes such as "unseen memories," "older memories," or "high sentiment memories." This would give all entries a fair chance to resurface and would create a more meaningful browsing experience.



## User Analysis for Front-end Design

### Potential Users
The potential users of our web page are people who want to see others' happy memories and also who are willing to share their own stories with others. Some researchers who are interested in studying the happy moments of people are also included in the potential users. 

### Potential Benefits
We hope our web page can give people chances to gain comforts from others' happy memories. Meanwhile, we also wish to build up  a community where people can share their unique happy memories and also maybe interact with others. Our web also give people opportunities to retrieve data from the datasource. It may help people who have interest in researching on people's happy moments. 

### Assumptions and Potential Harms
Firstly, we assume that all the users can understand English. All the messages and stories are written in English. If users do not have a basic understanding of English, they won't get what the web is trying to do. To fix that, we designed the "I'm happy" message that can help people from different backgrounds to gain a basic sense of what this web is about. Its effects are limited. In the future, we should work on providing some translation function for people from different cultural backgrounds. Another assumption is that users are happy with the color design of our web page. The color we chose may make some users uncomfortable and cannot continue to surf the web. We should provide more patterns using different colors and provide the users different options of design. What's more, we assume that all users have capable visual ability to see all the contents. If a person is blind, he or she cannot use our web page since all the functions we build rely on visibility. To fix that, we should probably add a "read the page" function. It helps those blind people hear about the web and the happy stories from other people. 