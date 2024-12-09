---
description: "Learn more about: ISLOGICAL"
title: "ISLOGICAL function (DAX)"
---
# ISLOGICAL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a logical value, (`TRUE` or `FALSE`), and returns `TRUE` or `FALSE`.  
  
## Syntax  
  
```dax
ISLOGICAL(<value>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`value`|The value that you want to test.|  
  
## Return value

`TRUE` if the value is a logical value; `FALSE` if any value other than `TRUE` OR `FALSE`.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following three samples show the behavior of ISLOGICAL.  
  
```dax
//RETURNS: Is Boolean type or Logical  
= IF(ISLOGICAL(true), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is Boolean type or Logical  
= IF(ISLOGICAL(false), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is different type  
= IF(ISLOGICAL(25), "Is Boolean type or Logical", "Is different type")  
```
  
## Related content

[Information functions](information-functions-dax.md)  
