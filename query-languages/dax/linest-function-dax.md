---
description: "Learn more about: LINEST"
title: "LINEST function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.subservice: dax
ms.date: 01/18/2023
ms.topic: reference
author: masanto-msft
ms.author: masanto
recommendations: false

---

# LINEST

Uses the Least Squares method to calculate a straight line that best fits the given data, then returns a table describing the line. The equation for the line is of the form: y = **Slope1**\*x1 + **Slope2**\*x2 + ... + **Intercept**.

## Syntax

```dax
LINEST ( <columnY>, <columnX>[, …][, <const>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|columnY|The column of known y-values. Must have scalar type.|
|columnX|The columns of known x-values. Must have scalar type. At least one must be provided.|
|const|(Optional) A constant TRUE/FALSE value specifying whether to force the constant **Intercept** to equal 0.</br>If TRUE or omitted, the **Intercept** value is calculated normally; If FALSE, the **Intercept** value is set to zero.|

## Return value

A single-row table describing the line, plus additional statistics. These are the available columns:

- **Slope1**, **Slope2**, ..., **SlopeN**: the coefficients corresponding to each x-value;
- **Intercept**: intercept value;
- **StandardErrorSlope1**, **StandardErrorSlope2**, ..., **StandardErrorSlopeN**: the standard error values for the coefficients **Slope1**, **Slope2**, ..., **SlopeN**;
- **StandardErrorIntercept**: the standard error value for the constant **Intercept**;
- **CoefficientOfDetermination**: the coefficient of determination (r²). Compares estimated and actual y-values, and ranges in value from 0 to 1: the higher the value, the higher the correlation in the sample;
- **StandardError**: the standard error for the y estimate;
- **FStatistic**: the F statistic, or the F-observed value. Use the F statistic to determine whether the observed relationship between the dependent and independent variables occurs by chance;
- **DegreesOfFreedom**: the degrees of freedom. Use this value to help you find F-critical values in a statistical table, and determine a confidence level for the model;
- **RegressionSumOfSquares**: the regression sum of squares;
- **ResidualSumOfSquares**: the residual sum of squares.

## Remarks

\<columnY> and the \<columnX>’s must all belong to the same table.

## Example 1

The following DAX query:

```dax
EVALUATE LINEST(
	'FactInternetSales'[SalesAmount],
	'FactInternetSales'[TotalProductCost]
)
```

Returns a single-row table with ten columns:

|Slope1|Intercept|StandardErrorSlope1|StandardErrorIntercept|CoefficientOfDetermination|
|-----|-----|-----|-----|-----|
|1.67703250456677|6.34550460373026|0.000448675725548806|0.279131821917317|0.995695557281456|

|StandardError|FStatistic|DegreesOfFreedom|RegressionSumOfSquares|ResidualSumOfSquares|
|-----|-----|-----|-----|-----|
|60.9171030357485|13970688.6139993|60396|51843736761.658|224123120.339218|

- **Slope1** and **Intercept**: the coefficients of the calculated linear model;
- **StandardErrorSlope1** and **StandardErrorIntercept**: the standard error values for the coefficients above;
- **CoefficientOfDetermination**, **StandardError**, **FStatistic**, **DegreesOfFreedom**, **RegressionSumOfSquares** and **ResidualSumOfSquares**: regression statistics about the model.

For a given internet sale, this model predicts the sale amount by the following formula:

```
SalesAmount = Slope1 * TotalProductCost + Intercept
```

## Example 2

The following DAX query:

```dax
EVALUATE LINEST(
	'DimCustomer'[TotalSalesAmount],
	'DimCustomer'[YearlyIncome],
    'DimCustomer'[TotalChildren],
	'DimCustomer'[BirthDate]
)
```

Returns a single-row table with fourteen columns:

- Slope1
- Slope2
- Slope3
- Intercept
- StandardErrorSlope1
- StandardErrorSlope2
- StandardErrorSlope3
- StandardErrorIntercept
- CoefficientOfDetermination
- StandardError
- FStatistic
- DegreesOfFreedom
- RegressionSumOfSquares
- ResidualSumOfSquares

For a given customer, this model predicts total sales by the following formula (the birth date is automatically converted to a number):

```
TotalSalesAmount = Slope1 * YearlyIncome + Slope2 * TotalChildren + Slope3 * BirthDate + Intercept
```

## See also

[LINESTX](linestx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
