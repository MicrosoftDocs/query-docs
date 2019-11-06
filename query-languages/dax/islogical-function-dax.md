---
title: "ISLOGICAL function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISLOGICAL
Checks whether a value is a logical value, (TRUE or FALSE), and returns TRUE or FALSE.  
  
## Syntax  
  
```dax
ISLOGICAL(<value>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|value|The value that you want to test.|  
  
## Property Value/Return value  
TRUE if the value is a logical value; FALSE if any value other than TRUE OR FALSE.  
  
## Example  
The following three samples show the behavior of ISLOGICAL.  
  
```dax
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(true), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(false), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is different type  
=IF(ISLOGICAL(25), "Is Boolean type or Logical", "Is different type")  
```
  
## See also  
[Information functions &#40;DAX&#41;](information-functions-dax.md)  
  
