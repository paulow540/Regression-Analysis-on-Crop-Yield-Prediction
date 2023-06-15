# Introduction


## Objective:

Our goal for this project is to forecast production or farm yield based on other variables such as Temperature,Precipitation,Export,Fertilizer,Crop_Avocados,Crop_Bananas,Crop_Rice,Crop_Wheat,as both impact Yield. 


## Problems to beaddressed:

    - Investigate the data and create newfeatures
    - Estimate each farm crop's production.
    - Create a sourcing plan for an ingredient based on expected demand for the next fewmonths.

## Approach:

For this analysis we have taken agricultural dataset and climate dataset from Kaggle and merged them based on the common fields to predict crop yield. We built 3 different models and compared the results to find the best model for our analysis.


# DataSynthesis

## DataOverview

Our data is around 2080580 bytes in size,with 7 properties.Crop	Year	Yield	Temperature (Avg)	Precipitation	Export Quantity	Fertilizer Usage all of which contain a combination of category and numeric variables, are contained in one datasets. The attribute yield is an independent variable, while the rest of the attributes are dependent. 

#### Farm Yield Data

| Crop	 | Unique farm ids |
| --- | --- |
| Date | Dates per hour from 2016 in train and from 2017 in test |
| Ingredient\_type | Type of ingredient in the farm : There are 4 types - w,x,y,z |
| Yield | Yield for each farm per hour |

#### Farm Data
Crop	Year	Yield	Temperature (Avg)	Precipitation	Export Quantity	Fertilizer Usage
0	Avocados	1961	48990	8.45	738.74	NaN	7466210.65
1	Avocados	1962	44532	8.74	677.47	NaN	8274858.92
2	Avocados	1963	50850	8.90	630.36	NaN	9169916.54
3	Avocados	1964	31137	8.30	705.13	NaN	9793376.58
4	Avocados	1965	57109	8.46	715.33	NaN	10803761.20

 
## DataProcessing:

1. Converted date
2. Checking and clearingduplicates
3. **135568** duplicate records have different yieldvalues
  - Dropped the duplicates by copying to another dataframe
  - Taken average and replaced the mean for duplicatevalues
  - Merge the average replaced records back with originaldata
  - **148920** records are dropped as whole rows are duplicated in thetable
4. Identified the percentage of null values in eachcolumn
  - Dropped columns with missing value percentage \>40%
  - Imputation is performed for records with missing values \< 40% usingmean.
  - Imputing with mode i.e. as 0 is occurring majority of the times inprecipitation
5. Merge operation onData
  - Farm\_data + test -\> initial\_merged\_test (+ weather\_test) -\> finaltest
  - Farm\_data + train -\> initial\_merged\_train (+ weather\_train) -\> finaltrain
6. Removed outliers with **z-score \>** 1.96
7. Removing columns that are no longer needed like Weekday, Index, Date, andTimestamp
8. Label Encoding is done for categoricalcolumns
9. Extracted Features from Time stamp suchas:
  - Time Stamp: Extracting features from datetime as weekday, day\_name, dayofyear, day, month, is\_month\_end,is\_month\_start
  - Weekend or Weekday: Appending weekend with 0 and weekday with1
  - Morning Evening Night: Segregated time into categoricalvariables
  - Splitting the data for validation Data split is done based on time stamp. For train data we used 2016 data and for test data, 2017 data is used for all months and compared yields based onmonths.

**MODEL BUIDLING**

## LINEAR REGRESSION MODEL
Regression models describe the relationship between variables by fitting a line to the observed data. Linear regression models use a straight line, while logistic and nonlinear regression models use a curved line.
After dummification, Linear Regression model is performed which resulted in **mean absolute error** of 573.68 and mean squared error is 5663965.13.


### DecisionTree

Decision Tree is performed without outliers and with hyperparameter and we get to compare the results.



### RandomForest

Before changes we got Mean absolute error of 587.83 and mean squared error was 5812902.98


### XGBoost:

Preprocessing: Label Encoding done on columns dayofyear, day and hour

**MAE value for XG Boost** is 575.912



# Evaluations andResults


### EvaluationMethods

Compared the errors of all the models performed and evaluated theresults

| Linear Regression | Decision Tree without outlier | Decision Tree with Hyperparameter | Random Forest | XG Boost |
| --- | --- | --- | --- | --- |
| 573.8 | 143.86 | 563.30 | 558.67 | 573 |

When compared to all other models, the **Decision Tree without outliers** produces the least error, hence it is the best model to utilize for agricultural yield production.

Compared Yield produced - Actual Versus OriginalDemand:

Predicted yield for every month for 2017 is presented below



**Results and Findings**

Extra Yield is calculated by comparing actual consumption to the original demand, making it easier to predict and develop crops to meet future needs.

1. Conclusions and Future Work
  1. Conclusions
    - Among all the models evaluated, the Decision Tree is the mostappropriate.
    - The monthly harvest is more than enough forconsumption.
    - Any excess product can be preserved for futureuse.
  2. Limitations
    - Cropforecastwasbasedon2yearsofdata;however, thenumberofyearsanalyzed mightbe increased to obtain a more efficient conclusion based on annual demandincreases.
    - Future demand can be forecasted using previous data for the next number of years, ratherthan just one ortwo.
  3. Potential Improvements or Future Work
    - Density Based clustering Technique can be used on Crop yieldPrediction.
    - Factors affecting agricultural yield output can be identified and worked towards anefficient method of yield prediction using the density-based clusteringtechnique.
