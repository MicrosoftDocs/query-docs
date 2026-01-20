---
description: "Learn more about: LOOKUPWITHTOTALS"
title: "LOOKUPWITHTOTALS function (DAX) | Microsoft Docs"
ms.topic: reference
---
# LOOKUPWITHTOTALS

[!INCLUDE[applies-to-visual-calculations](includes/applies-to-visual-calculations.md)]

Returns the value or evaluates the expression from the visual matrix using absolute navigation. Filters can be provided for any axis on the visual matrix. Any omitted filters are treated as referring to the total. If no single value can be determined, an error is returned.

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

The **Lookupwithtotals** visual calculation retrieves values for **FY2018** and all quarters since no value for quarter was specified as an argument. On the other hand, the **Lookup** visual calculation takes into account the current context. Therefore, the results are different and the **Lookup** visual calculation returns the **Sales Amount** for **FY2018** for each quarter. This also explains why the results for the **Lookup** visual calculation are empty because there is no combination of **FY2019 Q1** to **FY2019 Q4** and **FY2018**.


```dax
LOOKUPWITHTOTALExample1 = LOOKUPWITHTOTALS([Sales Amount], [Fiscal Year], "FY2018")

LookupExample1 = LOOKUP([Sales Amount], [Fiscal Year], "FY2018")
```

The screenshot below shows the matrix with two visual calculations.

![lookupwithTotals example 1](media/dax-queries/dax-visualcalc-lookupwithtotals-example1.png)

## Example 2
In this example, **LookupWithTotalExample2** retrieves the sum of sales for Bikes Category. Notices that uses the total for other the dimensions since they were not specified. In other words, those dimensions are not filtered. It's useful when we want to do comparison since the result is locked to one value.

```dax
LookupWithTotalExample2 = lookupWithTotals([Sales Amount], [Category], "Bikes")
```

![lookupwithTotals example 2](media/dax-queries/dax-visualcalc-lookupwithtotals-example2.png)

## Related content

[Lookup](lookup-function-dax.md)
