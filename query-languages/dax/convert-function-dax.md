---
description: "Learn more about: CONVERT"
title: "CONVERT function (DAX)"
---
# CONVERT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts an expression of one data type to another.
  
## Syntax  
  
```dax
CONVERT(<Expression>, <Datatype>)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|`Expression`|Any valid expression.|  
|`Datatype`|An enumeration that includes: INTEGER(Whole Number), DOUBLE(Decimal Number), STRING(Text), BOOLEAN(True/False), CURRENCY(Fixed Decimal Number), DATETIME(Date, Time, etc).|  
  
## Return value

Returns the value of \<Expression>, translated to \<Datatype>.
  
## Remarks  

- The function returns an error when a value cannot be converted to the specified data type.

- DAX calculated columns must be of a single data type. Since MEDIAN and MEDIANX functions over an integer column return mixed data types, either integer or double, the following calculated column expression will return an error as a result: `MedianNumberCarsOwned = MEDIAN(DimCustomer[NumberCarsOwned])`.
- To avoid mixed data types, change the expression to always return the double data type, for example:  
    `MedianNumberCarsOwned = MEDIANX(DimCustomer, CONVERT([NumberCarsOwned], DOUBLE))`.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  

DAX query

```dax
EVALUATE { CONVERT(DATE(1900, 1, 1), INTEGER) }  
```

Returns

|[Value]  |
|---------|
|2     |
