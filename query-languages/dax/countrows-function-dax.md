---
description: "Learn more about: COUNTROWS"
title: "COUNTROWS function (DAX)"
ms.topic: reference
---
# COUNTROWS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

The COUNTROWS function counts the number of rows in the specified table, or in a table defined by an expression.

## Syntax

```dax
COUNTROWS([<table>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`|(Optional) The name of the table that contains the rows to be counted, or an expression that returns a table. When not provided, the default value is the home table of the current expression. |

## Return value

A whole number.

## Remarks

- This function can be used to count the number of rows in a base table, but more often is used to count the number of rows that result from filtering a table, or applying context to a table.

- When the table argument contains no rows, the function returns BLANK.

- To learn more about best practices when using COUNT and COUNTROWS, see [Use COUNTROWS instead of COUNT in DAX](best-practices/dax-countrows.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following example shows how to count the number of rows in the table Orders. The expected result is 52761.

```dax
= COUNTROWS('Orders')
```

## Example 2

The following example demonstrates how to use COUNTROWS with a row context. In this scenario, there are two sets of data that are related by order number. The table Reseller contains one row for each reseller; the table ResellerSales contains multiple rows for each order, each row containing one order for a particular reseller. The tables are connected by a relationship on the column, ResellerKey.

The formula gets the value of ResellerKey and then counts the number of rows in the related table that have the same reseller ID. The result is output in the column, **CalculatedColumn1**.

```dax
= COUNTROWS(RELATEDTABLE(ResellerSales))
```

The following table shows a portion of the expected results:

|ResellerKey|CalculatedColumn1|
|---------------|---------------------|
|1|73|
|2|70|
|3|394|

## Related content

- [COUNT function](count-function-dax.md)
- [COUNTA function](counta-function-dax.md)
- [COUNTAX function](countax-function-dax.md)
- [COUNTX function](countx-function-dax.md)
- [Statistical functions](statistical-functions-dax.md)
