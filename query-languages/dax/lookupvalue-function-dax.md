---
title: "LOOKUPVALUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/24/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# LOOKUPVALUE

Returns the value for the row that meets all criteria specified by search conditions. The function can apply one or more search conditions.

## Syntax

```dax
LOOKUPVALUE(<result_columnName>, <search_columnName>, <search_value>[, <search2_columnName>, <search2_value>]…[, <alternateResult>])
```

### Parameters

|Term|Definition|
|--------|--------------|
| result_columnName  |  The name of an existing column that contains the value you want to return. The column reference must be fully qualified, which means it must include the table name. It cannot be an expression. |
| search_columnName  | The name of an existing column. It can be in the same table as result_columnName or in a related table. The column reference must be fully qualified, which means it must include the table name. It cannot be an expression. |
| search_value | A scalar expression. It cannot refer to any column in the same table being searched. |
| alternateResult | (Optional) The value returned when the context for result_columnName has been filtered down to zero or more than one distinct value. When not provided, the function returns BLANK when result_columnName is filtered down to zero value or an error when more than one distinct value. |

## Return value

The value of **result_column** at the row where all pairs of **search_column** and **search_value** have an exact match.

If there's no match that satisfies all the search values, BLANK or **alternateResult** (if supplied) is returned. In other words, the function won't return a lookup value if only some of the criteria match.

If multiple rows match the search values and in all cases **result_column** values are identical, then that value is returned. However, if **result_column** returns different values, an error or **alternateResult** (if supplied) is returned.

## Remarks

If there's a one-to-many relationship path between the result and search tables, it may be possible to use the RELATED function. In this case, the [RELATED](related-function-dax.md) function is likely to perform better.

## Example

The following **Sales Territory** table rule (for row-level security) enforces a filter restricting data access to rows of the report user's region. It uses the LOOKUPVALUE function to lookup the region from the **Employee** table.

Notice that the [USERNAME](username-function-dax.md) function, which retrieves the user name of the authenticated user, is used to search the **Employee** table for a match on email address.

```dax
[Region] = LOOKUPVALUE(Employee[Region], Employee[Email], USERNAME())
```

## See also

- [RELATED function (DAX)](related-function-dax.md)
