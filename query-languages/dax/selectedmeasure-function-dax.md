---
description: "Learn more about: SELECTEDMEASURE"
title: "SELECTEDMEASURE function (DAX)"
---
# SELECTEDMEASURE

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Used by expressions for calculation items or dynamic format strings to reference the measure that is in context.
  
## Syntax  
  
```dax
SELECTEDMEASURE()
```
  
### Parameters  
  
None  
  
## Return value  

A reference to the measure that is currently in context when the calculation item or format string is evaluated.

## Remarks

- Can only be referenced in the expression for a calculation item or format string.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  

The following calculation item expression calculates the year-to-date for whatever the measure is in context.
  
```dax
CALCULATE(SELECTEDMEASURE(), DATESYTD(DimDate[Date]))
```

The following expression can be used to dynamically adjust the format string of a measure based upon whether a value is the hundreds, thousands, or millions.

```dax
SWITCH(
TRUE(),
SELECTEDMEASURE() < 1000,"$#,##0",            //Values less than 1000 have no text after them
SELECTEDMEASURE() < 1000000, "$#,##0,.0 K",   //Values between 1000 and 1000000 are formatted as #.## K
"$#,##0,,.0 M"                                //Values greater than 1000000 are formatted as #.## M
)
```
  
## Related content

[SELECTEDMEASURENAME](selectedmeasurename-function-dax.md)  
[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md)   
