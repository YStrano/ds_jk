# Lesson Materials and Topic

### [Lesson 3: Introduction to Pandas and Matplotlib](https://github.com/jfkoehler/GA-errata)

**GOALS**: 
  - Use Pandas to explore data
  - Use Plots to explore data
  - Perform basic descriptive statistics on data

### [Lesson 4: Introduction to Linear Regression](https://github.com/jfkoehler/GA-regression)


**GOALS**:
  - Introduce predictive modeling with Least Squares Models
  - Implement Linear Regression with StatsModels and Numpy
  - Transform non-linear data to linear models with logarithmic transformations and perform linear fit

### [Lesson 5: Improving the Model](https://github.com/jfkoehler/GA-02-Modeling)

**GOALS**:
- Examine multiple features with regression
- Code categorical variables and interpret with regression
- Examine polynomial regression
- Understand Collinearity
- Assess model using Train/Test split
- Scale features with `MaxMinScaler` and `StandardScaler`
- Use `Lasso`, 'Ridge`, and `ElasticNet` models 

**Resources**:

- [Andrew Ng Lectures on Regularized Methods]()
- [University of Michigan Lectures on Regularized Methods]()
- [An Introduction to Statistical Learning](): chapter on linear regression
- [SciKitLearn Documentation on Regression]()
- [JVDP on Regression]()

### [Lesson 6: Cross Validation and Grid Search](https://github.com/jfkoehler/GA-Cross-Validation)

**GOALS**:
- Use cross validation to build models on training data
- Use grid search to tune hyperparameters of models
- Determine best model based on grid search results

**Resources**:

- [An Introduction to Statistical Learning](): Chapter on Cross-Validation
- [Hands on Machine Learning](): Jupyter Notebook covering Cross-Validation and Grid Search
- [Andrew Ng on Cross Validation]()
- [University of Michigan Lecture on Cross-Validation]()
- [SciKitLearn Documentation on Cross-Validation]()

### [Lesson 7: Introduction to Classification: KMeans and KNN](https://github.com/jfkoehler/GA-Clustering-I)

**GOALS**:
- Understand the nature of Classification Problems with Clustering
- Use `KNearestNeighbors` to understand classification of data
- Evaluate model with accuracy

### [Lesson 8: Classification with Logistic Regression](https://github.com/jfkoehler/GA-Logistic-Regression)

**GOALS**
- Understand Logistic Regression and binary classification 
- Use `LogisticRegression` to examine probability of class inclusion
- Introduce metrics for model evaluation from `confusion_matrix`

**Resources**
- [An Introduction to Statistical Learning](): Chapter on Logistic Regression
- [JVDP on CLassification]()
- [Andrew Ng on Classification]()
- [Yasser Abu-Mustafa of CalTech](https://www.youtube.com/watch?v=FIbVs5GbBlQ&hd=1): Lecture on Linear models.


### [Lesson 9: Model Evaluation and Interpretation](https://github.com/jfkoehler/GA-Classification-Evaluation)
**GOALS**:
- Review evaluation metrics for Classification
- Introduce ROC and AUC plots
- Presentations and Assignment 4

### [Lesson 10: Gradient Descent in Regression and Classification](https://github.com/jfkoehler/GA-Model-Selection)
**GOALS**
- Investigate Regression Evaluation and compare methods
- Understand the difference between gradient descent and closed form solutions to optimization problems
- Compare scenarios for using Gradient Descent and evaluate implementation in sklearn
- Review Cross-Validation and Grid Search: Select Best Model

### [Lesson 11: Web Scraping API's](https://github.com/jfkoehler/GA-scrape-NLTK)
**GOALS**
- Use Requests and BeautifulSoup to extract data from the web
- Use API's to access data

[notebook link II](https://github.com/ga-students/DAT-NYC-3.20.18/tree/master/lessons/working-with-api-data)

**Resources**:

- [Requests Documentation](http://docs.python-requests.org/en/master/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [Webscraping Trump](https://www.youtube.com/watch?v=r_xb0vF1uMc): Justin Markham's tutorial on scraping and structuring a New York Times article on Donald Trump.
- [PythonProgramming.net Tutorial](https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/)

### [Lesson 12: NLP and Text Classification](https://github.com/jfkoehler/GA-NLP)
**GOALS**
- Use advanced NLTK strategies to investigate product reviews
- Use and understand Naive Bayes for text classification
- Use Twitter API to investigate tweet content

**Resources**:
- [NLTK Book]()
- [NLTK Lectures from University of Michigan]()
- [Jake VanDerPlas' Notebook on Naive Bayes]()
- []()

### [Lesson 13: Decision Trees](https://github.com/jfkoehler/GA-DecisionTrees/blob/master/README.md)
**GOALS**
- Use Decision Trees to investigate classification and regression problems

### [Lesson 14: Random Forest Models and Ensemble Methods](https://github.com/jfkoehler/GA-Ensembles)
**GOALS**
- Use Random Forrest models to ensemble methods

### [Lesson 15: Timeseries I](https://github.com/jfkoehler/GA-Time-Series)

### [Lesson 16: Working with Databases](https://github.com/jfkoehler/GA-Database-FeatureSelect)

### [Lesson 17: Feature Selection, Pipelines, and Evaluation](https://github.com/jfkoehler/Pipelines-and-Pickles)

### [Lesson 18: Introduction to Neural Networks](https://github.com/jfkoehler/GA-FLASK)

## Additional Resources

For more information on this topic, check out:

- [The Flask Documentation](http://flask.pocoo.org/docs/0.11/)
- [A Flask tutorial to follow along with](https://github.com/miguelgrinberg/flask-pycon2014)
- [Another tutorial that gets into CSS styling](https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822)
- [The Flask mega tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [Flask's development server is not for production](https://stackoverflow.com/questions/12269537/is-the-server-bundled-with-flask-safe-to-use-in-production)
- [Setting up Flask on AWS EC2](http://bathompso.com/blog/Flask-AWS-Setup/). This should be your next step if you want to share your model with the world!
- [A great guide to those weird "decorators"](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).

### Production coding

- Add [logging](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) to your code; you'll be very glad you did.
- Think ahead and include [error handling](https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/), via [try/except clauses](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
- Get more comfortable with git, including [feature branching](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).
- Include [unit tests](http://www.diveintopython.net/unit_testing/index.html); the [pytest module](http://pythontesting.net/framework/pytest/pytest-introduction/) is great.
- [Integrate databases](http://zetcode.com/db/sqlitepythontutorial/)!
- Beware technical debt, especially [machine learning technical debt](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43146.pdf).

## In Course Projects

- [Project I](https://github.com/ga-students/DAT-NYC-3.20.18/tree/master/projects/unit-projects/project-1)

- [Project II](https://github.com/jfkoehler/GA-regression)

- [Project III: Final Project Part I](https://github.com/jfkoehler/GA-Cross-Validation/blob/master/Final-Project-1.ipynb)

- [Project IV: Modeling Project I](projectIII.md)





