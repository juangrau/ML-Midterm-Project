# Data Talks Club - Machine Learning Zoomcamp - Midterm project

## Predicting Telemarketing Campaign Success: A Machine Learning Approach

Telemarketing campaigns, while a common marketing strategy, often face challenges in terms of effectiveness and resource allocation. To optimize these campaigns, it's crucial to predict their potential success before execution. This project aims to develop a machine learning classification model to predict whether a telemarketing campaign will be successful or not.

By leveraging historical data on various factors influencing campaign outcomes, we can train a model to identify patterns and make accurate predictions. This predictive capability empowers businesses to make informed decisions regarding campaign planning, resource allocation, and overall strategy.

The core objective of this project is to:

- **Data Acquisition and Preparation**: In this case we are going to use the dataset available at [UC Irvine Machine Learning Repository - Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).
  - You can check the link above for further reference to this dataset.
  - For the purpose of this project the data has already been downloaded the this repository.
- **Model Development**: Train and tune a machine learning classification model, such as a Decision Tree, Random Forest or XGBoost, to learn from the historical data.
- **Model Evaluation**: Evaluate the model's performance using appropriate metrics like ROC AUC.   
- **Prediction and Insights**: Utilize the trained model to predict the success of future telemarketing campaigns and provide actionable insights.

By successfully implementing this machine learning solution, businesses can significantly enhance the efficiency and ROI of their telemarketing efforts.



## Available files on the repository

| File                      | Description                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| bank-additional-full.csv  | Dataset file used to train and test the machine learning models                                                            |
| bank-additional-names.txt | Text file with more information about the dataset, including the description of each of the columns                        |
| Dockerfile                | Docker file to create the image of this project and run the model as a service.                                            |
| model.bin                 | Pickle file with the model created for this project                                                                        |
| notebook.ipynb            | Jupyter Notebook where data loading, cleaning, EDA and Model comparison was done.                                          |
| Pipfile, Pipfile.lock     | Files generated by pipenv to create a virtual python environment with all the dependencies to run the project as a service |
| predict.py                | Python script that runs the project as a Flask service.                                                                    |
| train.py                  | Python script that train the model with the right parameters and export the model.bin Pickle file.                         |
| predict-test.py           | Python script that submit a customer data to the predict service and return if the campaign will be a success or not. The script includes some coments about how to tweak the sample customer in order to get a positive or negative prediction from the service     |



## How to run this project

1. Download all the files or clone this repository on your system. To clone the repo, you can execute the following command from the shell:

```shell
git clone https://github.com/juangrau/DTC-ML-course.git
```

2. Navigate to the project directory on your terminal.

3. build and run the docker image:

```shell
docker build -t go-marketing .

docker run -it -p 9696:9696 go-marketing:latest
```

4. The scope of this image is a web service based on Flask that allows to predict if a tele-marketing campaign will be successful for a customer of a bank.

5. To test it you can run the script *predict-test.py* like this:

```shell
python predict-test.py
```

Make sure you have the *requests* library installed. To install it you can run the follwing command on the terminal

```shell
pip install requests
```




