## Begin Graphlab Crete
import graphlab
## Store data set into "sales" variable
sales = graphlab.SFrame('home_data.gl/')
## Investigate data set
sales
## Use a scatter plot to understand the relationship between house price and size
graphlab.canvas.set_target('ipynb')
sales.show(view="Scatter Plot", x="sqft_living", y="price")

## Set the ratio of tranning and testing data 
train_data,test_data = sales.random_split(.8,seed=0) #Trick:Tab gives you a list of function; ".8" means 80% training data 20% testing data

## Store features for regression model
advanced_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode','condition', 
'waterfront', 'view', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated','lat', 'long', 'sqft_living15', 'sqft_lot15']
## Build a regression model based on the features
advanced_features_model = graphlab.linear_regression.create(train_data, target='price', features=advanced_features, validation_set=None)
## Evaluate the regression model
print advanced_features_model.evaluate(test_data) # throw test_data back to our model and evaluate by rmse
advanced_features_model.get('coefficients') # check the coefficients in the model
