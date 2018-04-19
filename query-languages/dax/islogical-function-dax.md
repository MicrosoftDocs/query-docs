---
title: "ISLOGICAL Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISLOGICAL Function (DAX)
Checks whether a value is a logical value, (TRUE or FALSE), and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISLOGICAL(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value that you want to test.|  
  
## Property Value/Return Value  
TRUE if the value is a logical value; FALSE if any value other than TRUE OR FALSE.  
  
## Example  
The following three samples show the behavior of ISLOGICAL.  
  
```  
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(true), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(false), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is different type  
=IF(ISLOGICAL(25), "Is Boolean type or Logical", "Is different type")  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
  
