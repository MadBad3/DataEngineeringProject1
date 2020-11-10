# DataEngineeringProject1
Web application for sentiment analysis into docker containers

- Pull the project into a directory, then do this command: `docker-compose up`

The application will run into a docker on the port 5000.

- Then to try the test functions, enter this command into a new terminal at the same directory of the docker container: `python test_app.py`

The dataset is at this link if you want to train again the model: https://www.kaggle.com/laowingkin/amazon-fine-food-review-sentiment-analysis?select=Reviews.csv

If you want to train the model again you should delete the model.pkl, because after the train it will load a new one, and you should do this command to train: `python model.py`
