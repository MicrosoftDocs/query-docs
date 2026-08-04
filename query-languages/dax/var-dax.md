---
description: "Learn more about: VAR"
title: "VAR keyword (DAX)"
ms.topic: reference
ms.date: 07/08/2026
ms.custom: ExampleTypeAW2020
---
# VAR

Stores the result of an expression as a named variable, which you can then pass as an argument to other measure expressions. After DAX calculates the values for a variable expression, those values don't change, even if you reference the variable in another expression.

## Syntax

```dax
VAR <name> = <expression>
```

### Parameters

|Term|Definition|
|--------|--------------|
|`name`|The name of the variable (identifier).<br />Delimiters aren't supported. For example, 'varName' or [varName] results in an error.<br />Supported character set: a-z, A-Z, 0-9.<br />   0-9 aren't valid as first character.<br />__ (double underscore) is allowed as a prefix to the identifier name.<br />No other special characters are supported.<br />Reserved keywords aren't allowed.<br />Names of existing tables aren't allowed.<br />Empty spaces aren't allowed.|
|`expression`|A DAX expression that returns a scalar or table value.|

## Return value

A named variable containing the result of the expression argument. 

## Remarks

- An expression passed as an argument to VAR can contain another VAR declaration.

- When you reference a variable:
  - Measures can't refer to variables defined outside the measure expression, but can refer to functional scope variables defined within the expression.
  - Variables can refer to measures.
  - Variables can refer to previously defined variables.
  - You can't reference columns in table variables by using TableName[ColumnName] syntax.

- For best practices when using VAR, see [Use variables to improve your DAX formulas](best-practices/dax-variables.md).

- To learn more about how VAR is used within a DAX Query, see [DAX queries](dax-queries.md).

## Example

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

To calculate a percentage of year-over-year growth without using a variable, you could create three separate measures. This first measure calculates Sum of Sales Amount:

```dax
Sum of Sales Amount =
SUM ( Sales[Sales Amount] )
```

A second measure calculates the sales amount for the previous year:

```dax
Sales Amount PreviousYear =
CALCULATE ( [Sum of Sales Amount], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
```

You can then create a third measure that combines the other two measures to calculate a growth percentage. Notice that Sum of SalesAmount is used in two places: first to check whether a sale exists, then again to calculate a percentage.

```dax
Sum of SalesAmount YoY%: =
IF (
    [Sum of Sales Amount] && [Sales Amount PreviousYear],
    DIVIDE (
        ( [Sum of Sales Amount] - [Sales Amount PreviousYear] ),
        [Sales Amount PreviousYear]
    )
)
```

By using a variable, you can create a single measure that calculates the same result:

```dax
YoY% =
VAR Sales =
    SUM ( Sales[Sales Amount] )
VAR SalesLastYear =
    CALCULATE ( SUM ( Sales[Sales Amount] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
RETURN
    IF ( Sales && SalesLastYear, DIVIDE ( Sales - SalesLastYear, SalesLastYear ) )
```

By using a variable, you can get the same outcome in a more readable way. And because the result of the expression is stored in the variable, the measure's performance improves significantly because DAX doesn't recalculate it each time it's used.

## Related content

- [Use variables to improve your DAX formulas](best-practices/dax-variables.md)
- [DAX queries](dax-queries.md)
