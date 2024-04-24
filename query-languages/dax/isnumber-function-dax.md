---
description: "Learn more about: ISNUMBER"
title: "ISNUMBER function (DAX) | Microsoft Docs"
---
# ISNUMBER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a number, and returns TRUE or FALSE.  
  
## Syntax  
  
```dax
ISNUMBER(<value>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|value|The value you want to test.|  
  
## Return value

TRUE if the value is numeric; otherwise FALSE.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following three samples show the behavior of ISNUMBER.  
  
```dax
//RETURNS: Is number  
= IF(ISNUMBER(0), "Is number", "Is Not number")  
  
//RETURNS: Is number  
= IF(ISNUMBER(3.1E-1),"Is number", "Is Not number")  
  
//RETURNS: Is Not number  
= IF(ISNUMBER("123"), "Is number", "Is Not number")  
```
  
## Related content

[Information functions](information-functions-dax.md)  
