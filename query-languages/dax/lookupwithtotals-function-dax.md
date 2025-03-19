---
description: "Learn more about: LOOKUPWITHTOTALS"
title: "LOOKUPWITHTOTALS function (DAX) | Microsoft Docs"
---
# LOOKUPWITHTOTALS

[!INCLUDE[applies-to-visual-calculations](includes/applies-to-visual-calculations.md)]

Returns the value from a cell in the visual matrix using absolute navigation. Filters can be provided for any axis on the visual matrix. Any omitted filters are treated as referring to the total. If no single value can be determined, an error is returned.

## Syntax

```dax
LOOKUPWITHTOTALS(<expression>, <colref>, <expression>[, <colref>, <expression>]...)
```

### Parameters

|Term|Definition|
|--------|--------------|
|expression| The expression to evaluate |
|colref|(Optional) The column to be filtered.|
|expression|(Optional) The value to filter.|

## Return value

The value of **expression** after filters are applied.

If there isn't a match, an error is returned.

If multiple rows match the filters, an error is returned.

## Example 1

In this example, LOOKUPWITHTOTALS retrieves the sum of sales for Fiscal Year 2018.
The first argument could be a column or a scalar expression.
Please note that in the example below, Lookupwithtotals retrieves values from FY2018 and disregards the quarter. On the other hand, Lookup applies filters for each quarter, resulting in row-specific changes 


```dax
LOOKUPWITHTOTALExample1 = LOOKUPWITHTOTALS([Sales Amount], [Fiscal Year], "FY2018")

LookupExample1 = LOOKUP([Sales Amount], [Fiscal Year], "FY2018")
```

The screenshot below shows the matrix with two visual calculations.

![lookupwithTotals example 1](media/dax-queries/dax-visualcalc-lookupwithtotals-example1.png)

## Example 2
In this example, LookupWithTotalExample2 retrieves the sum of sales for Bikes Category. Notices that it get total grain for other dimension. In other words, it is not filtered. It's useful when we want to do comparison since lookupwithtoal result is locked to a certain value.

```dax
LookupWithTotalExample2 = lookupWithTotals([Sales Amount], [Category], "Bikes")
```

![lookupwithTotals example 2](media/dax-queries/dax-visualcalc-lookupwithtotals-example2.png)

## Related content

[Lookup](lookup-function-dax.md)
