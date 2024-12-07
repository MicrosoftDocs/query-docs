---
description: "Learn more about: LOOKUPVALUE"
title: "LOOKUPVALUE function (DAX) | Microsoft Docs"
---
# LOOKUPVALUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the value for the row that meets all criteria specified by one or more search conditions.

## Syntax

```dax
LOOKUPVALUE (
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
| `result_columnName`  |  The name of an existing column that contains the value you want to return.  It cannot be an expression. |
| `search_columnName`  | The name of an existing column. It can be in the same table as result_columnName or in a related table. It cannot be an expression. Multiple pairs of search_columnName and search_value can be specified. |
| `search_value` | The value to search for in search_columnName. Multiple pairs of search_columnName and search_value can be specified. |
| `alternateResult` | (Optional) The value returned when the context for result_columnName has been filtered down to zero or more than one distinct value. If not specified, the function returns BLANK when result_columnName is filtered down to zero values or an error when there is more than one distinct value in the context for result_columnName. |

## Return value

The value of `result_columnName` at the row where all pairs of `search_columnName` and `search_value` have an exact match.

If there isn't a match that satisfies all the search values, BLANK or `alternateResult` (if specified) is returned. In other words, the function doesn't return a lookup value if only some of the criteria match.

If multiple rows match the search values and the values in the `result_columnName` for these rows are identical, then that value is returned. However, if `result_columnName` returns different values, an error or `alternateResult` (if specified) is returned.

## Remarks

- If there is a relationship between the table that contains the result column and tables that contain the search columns, in most cases, using the [RELATED](related-function-dax.md) function instead of LOOKUPVALUE is more efficient and provides better performance.

- Multiple pairs of `search_columnName` and `search_value` can be specified.

- The `search_value` and `alternateResult` parameters are evaluated before the function iterates through the rows of the search table.

- Avoid using ISERROR or IFERROR functions to capture an error returned by LOOKUPVALUE. If some inputs to the function result in an error when a single output value cannot be determined, providing an `alternateResult` parameter is the most reliable and highest performing way to handle the error.

- The `alternateResult` parameter returns an error if specified in a Power Pivot calculated column.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

In this example, LOOKUPVALUE is used to search Average Rate for the currency used to pay for the order on the day the order was placed:

```dax
Exchange Rate = 
LOOKUPVALUE (
    'Currency Rate'[Average Rate],
    'Currency Rate'[CurrencyKey], [CurrencyKey],
    'Currency Rate'[DateKey], [OrderDateKey]
)

```

Both the Order Date and Currency are required to find the Average Rate for the correct date and currency. OrderDateKey and CurrencyKey are the keys used to look up the Average Rate in the Currency Rate table.

You can use the Exchange Rate to calculate the Sales Amount in local currency with:

```dax
Sales Amount Local Currency = [Sales Amount] * [Exchange Rate]

```

## Example 2

In this example, the following calculated column defined in the **Sales** table uses the LOOKUPVALUE function to return channel values from the **Sales Order** table.

```dax
CHANNEL = 
LOOKUPVALUE (
    'Sales Order'[Channel],
    'Sales Order'[SalesOrderLineKey],
    [SalesOrderLineKey]
)

```

However, in this case, because there is a relationship between the **Sales Order** and **Sales** tables, it's more efficient to use the [RELATED](related-function-dax.md) function.

```dax
CHANNEL = RELATED('Sales Order'[Channel])
```

## Related content

[RELATED function (DAX)](related-function-dax.md)  
[Information functions](information-functions-dax.md)  
