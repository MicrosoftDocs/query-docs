---
title: "MROUND Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.MROUND.f1"
helpviewer_keywords: 
  - "rounding"
  - "MROUND function"
ms.assetid: 6df752f1-edb9-4542-a180-a813595cc765
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MROUND Function (DAX)
Returns a number rounded to the desired multiple.  
  
## Syntax  
  
```  
MROUND(<number>, <multiple>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number to round.|  
|**multiple**|The multiple of significance to which you want to round the number.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
MROUND rounds up, away from zero, if the remainder of dividing **number** by the specified **multiple** is greater than or equal to half the value of **multiple**.  
  
## Example: Decimal Places  
  
### Description  
The following expression rounds 1.3 to the nearest multiple of .2. The expected result is 1.4.  
  
### Code  
  
```  
=MROUND(1.3,0.2)  
```  
  
## Example: Negative Numbers  
  
### Description  
The following expression rounds -10 to the nearest multiple of -3. The expected result is -9.  
  
### Code  
  
```  
=MROUND(-10,-3)  
```  
  
## Example: Error  
  
### Description  
The following expression returns an error, because the numbers have different signs.  
  
### Code  
  
```  
=MROUND(5,-2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](../DAX/round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](../DAX/rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](../DAX/mround-function-dax.md)  
[INT Function &#40;DAX&#41;](../DAX/int-function-dax.md)  
  
