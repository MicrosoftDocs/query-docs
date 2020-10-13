---
title: "LOOKUPVALUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 10/13/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# LOOKUPVALUE

Returns the value for the row that meets all criteria specified by search conditions. The function can apply one or more search conditions.

## Syntax

```dax
LOOKUPVALUE(
    <result_columnName>,
    <search_columnName>,
    <search_value>
    [, <search2_columnName>, <search2_value>]…
    [, <alternateResult>]
)
```

### Parameters

|Term|Definition|
|--------|--------------|
| result_columnName  |  The name of an existing column that contains the value you want to return.  It cannot be an expression. |
| search_columnName  | The name of an existing column. It can be in the same table as result_columnName or in a related table. It cannot be an expression. |
| search_value | A scalar expression. |
| alternateResult | (Optional) The value returned when the context for result_columnName has been filtered down to zero or more than one distinct value. When not provided, the function returns BLANK when result_columnName is filtered down to zero value or an error when more than one distinct value. |

## Return value

The value of **result_column** at the row where all pairs of **search_column** and **search_value** have an exact match.

If there's no match that satisfies all the search values, BLANK or **alternateResult** (if supplied) is returned. In other words, the function won't return a lookup value if only some of the criteria match.

If multiple rows match the search values and in all cases **result_column** values are identical, then that value is returned. However, if **result_column** returns different values, an error or **alternateResult** (if supplied) is returned.

## Remarks

- If there's a one-to-many relationship path between the result and search tables, it may be possible to use the RELATED function. In this case, the [RELATED](related-function-dax.md) function is likely to perform better.

- The **search_value** and **alternateResult** parameters are evaluated before the function iterates through the rows of the search table.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

The following **Sales** table calculated column definition uses the LOOKUPVALUE function to return channel values from the Sales Order table.

```dax
CHANNEL = LOOKUPVALUE('Sales Order'[Channel],'Sales Order'[SalesOrderLineKey],[SalesOrderLineKey])
```

However, in this case, because there's a relationship between the **Product** and **Sales** tables, it's more efficient to use the RELATED function.

```dax
CHANNEL = RELATED('Sales Order'[Channel])
```

## See also

[RELATED function (DAX)](related-function-dax.md)  
[Information functions](information-functions-dax.md)  
