---
description: "Learn more about: LINESTX"
title: "LINESTX function (DAX) | Microsoft Docs"
author: masanto-msft
ms.author: masanto
---

# LINESTX

Uses the Least Squares method to calculate a straight line that best fits the given data, then returns a table describing the line. The data result from expressions evaluated for each row in a table. The equation for the line is of the form: y = **Slope1**\*x1 + **Slope2**\*x2 + ... + **Intercept**.

## Syntax

```dax
LINESTX ( <table>, <expressionY>, <expressionX>[, …][, <const>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|table|The table containing the rows for which the expressions will be evaluated.|
|expressionY|The expression to be evaluated for each row of the table, to obtain the known y-values. Must have scalar type. |
|expressionX|The expressions to be evaluated for each row of the table, to obtain the known x-values. Must have scalar type. At least one must be provided.|
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

## Example 1

The following DAX query:

```dax
DEFINE VAR TotalSalesByRegion = SUMMARIZECOLUMNS(
    'Sales Territory'[Sales Territory Key],
    'Sales Territory'[Population],
    "Total Sales", SUM(Sales[Sales Amount])
)
EVALUATE LINESTX(
    'TotalSalesByRegion',
    [Total Sales],
    [Population]
)
```

Returns a single-row table with ten columns:

|Slope1|Intercept|StandardErrorSlope1|StandardErrorIntercept|CoefficientOfDetermination|
|-----|-----|-----|-----|-----|
|6.42271517588|-410592.76216|0.24959467764561|307826.343996223|0.973535860750193|

|StandardError|FStatistic|DegreesOfFreedom|RegressionSumOfSquares|ResidualSumOfSquares|
|-----|-----|-----|-----|-----|
|630758.1747292|662.165707642|18|263446517001130|7161405749781.07|

- **Slope1** and **Intercept**: the coefficients of the calculated linear model;
- **StandardErrorSlope1** and **StandardErrorIntercept**: the standard error values for the coefficients above;
- **CoefficientOfDetermination**, **StandardError**, **FStatistic**, **DegreesOfFreedom**, **RegressionSumOfSquares** and **ResidualSumOfSquares**: regression statistics about the model.

For a given sales territory, this model predicts total sales by the following formula:

```
Total Sales = Slope1 * Population + Intercept
```

## Example 2

The following DAX query:

```dax
DEFINE VAR TotalSalesByCustomer = SUMMARIZECOLUMNS(
    'Customer'[Customer ID],
    'Customer'[Age],
    'Customer'[NumOfChildren],
    "Total Sales", SUM(Sales[Sales Amount])
)
EVALUATE LINESTX(
    'TotalSalesByCustomer',
    [Total Sales],
    [Age],
    [NumOfChildren]
)
```

Returns a single-row table with twelve columns:

|Slope1|Slope2|Intercept|StandardErrorSlope1|
|--|--|--|--|
|69.0435458093763|33.005949841721|-871.118539339539|0.872588875481658|

|StandardErrorSlope2|StandardErrorIntercept|CoefficientOfDetermination|StandardError|
|--|--|--|--|
|6.21158863903435|26.726292527427|0.984892920482022|68.5715034014342|

|FStatistic|DegreesOfFreedom|RegressionSumOfSquares|ResidualSumOfSquares|
|--|--|--|--|
|3161.91535144391|97|29734974.9782379|456098.954637092|

For a given customer, this model predicts total sales by the following formula:

```
Total Sales = Slope1 * Age + Slope2 * NumOfChildren + Intercept
```

## Related content

[LINEST](linest-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
