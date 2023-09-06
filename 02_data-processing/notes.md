# Encoding

Encoding data means converting categorical data into numerical data.

E.g. Converting the names of the three types of Iris' to numbers such as 1, 2, 3.

# Six Types of Encode

## Label encoding
Each category is assigned a number from 1 to N (where N is the number of categories)

Downside is that the machine might interpret the sequential numbers as inferring a sequential relationship among the classes. E.g. there is no numerical relationship between the three types of Iris'

## Feature Encoding
Use numbers to represent the feature. E.g. ratings such as low, medium, and high can be represented as 1, 2, and 3

## One Hot Encoding
Map each category to a vector that has n-1 0s and one 1 to signify the category value.

Downside is that large numbers of categories result in large encoding size which can signifcantly slow down model generation.

## Binary Encoding
Consider 7 categories. They can be represented with three binary digits (from 001 to 111). In Binary Encoding the categories are converted to binary representation where each digit is one feature column (e.g. 0 | 1 | 1 for feature #3)

