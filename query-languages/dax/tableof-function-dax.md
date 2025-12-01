---
description: "Learn more about: TABLEOF"
title: "TABLEOF function (DAX)"
---
# TABLEOF

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a reference to the table associated with a specified column, measure, or calendar.

## Syntax

```dax
TABLEOF(<columnName>)
TABLEOF(<measureName>)
TABLEOF(<calendarReference>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`columnName`|The name of an existing column, using standard DAX syntax. It cannot be an expression.|
|`measureName`|The name of an existing measure.|
|`calendarReference`|A reference to a calendar.|

## Return value

A table reference.

## Remarks

- The `TABLEOF` function returns a table reference, not the table data itself.
- When passed a column name, it returns the table that contains that column.
- When passed a measure name, it returns the table where that measure is defined.
- When passed a calendar reference, it returns the table associated with that calendar.
- This function is useful in scenarios where you need to dynamically determine which table a column or measure belongs to.
- `TABLEOF` does not resolve columns from row context; it only resolves columns from the current filter context (base table).
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1 - Using TABLEOF with a column
```dax
EVALUATE ROW("RowCount", COUNTROWS(TABLEOF('DimCustomer'[CustomerKey])))
```

## Example 2 - Using TABLEOF with a measure
```dax
EVALUATE ROW("TableName", NAMEOF(TABLEOF([Total Sales])))
```

## Example 3 - Using TABLEOF in a user-defined function
```dax
DEFINE 
FUNCTION GetTableRowCount = (columnRef : anyref) => COUNTROWS(TABLEOF(columnRef))
EVALUATE 
ROW(
"FactResellerSalesCount", GetTableRowCount('FactResellerSales'[EmployeeKey]),
"DimCustomerCount", GetTableRowCount('DimCustomer'[CustomerKey])
)
```

## Related content
- [Information functions](information-functions-dax.md)
