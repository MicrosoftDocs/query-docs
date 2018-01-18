---
title: "CEILING Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.CEILING.f1"
helpviewer_keywords: 
  - "CEILING function"
ms.assetid: 5d76fc78-8a1e-4dbb-a2fc-2feeb0db902e
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# CEILING Function (DAX)
Rounds a number up, to the nearest integer or to the nearest multiple of significance.  
  
## Syntax  
  
```  
CEILING(<number>, <significance>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to round, or a reference to a column that contains numbers.|  
|**significance**|The multiple of significance to which you want to round. For example, to round to the nearest integer, type 1.|  
  
## Return Value  
A number rounded as specified.  
  
## Remarks  
There are two CEILING functions in DAX, with the following differences:  
  
-   The CEILING function emulates the behavior of the CEILING function in Excel.  
  
-   The ISO.CEILING function follows the ISO-defined behavior for determining the ceiling value.  
  
The two functions return the same value for positive numbers, but different values for negative numbers.  When using a positive multiple of significance, both CEILING and ISO.CEILING round negative numbers upward (toward positive infinity).  When using a negative multiple of significance, CEILING rounds negative numbers downward (toward negative infinity), while ISO.CEILING rounds negative numbers upward (toward positive infinity).  
  
The return type is usually of the same type of the significant argument, with the following exceptions:  
  
-   If the number argument type is currency, the return type is currency.  
  
-   If the significance argument type is Boolean, the return type is integer.  
  
-   If the significance argument type is non-numeric, the return type is real.  
  
## Example  
The following formula returns 4.45. This might be useful if you want to avoid using smaller units in your pricing. If an existing product is priced at $4.42, you can use CEILING to round prices up to the nearest unit of five cents.  
  
```  
=CEILING(4.42,0.05)  
```  
  
## Example  
The following formula returns similar results as the previous example, but uses numeric values stored in the column, **ProductPrice**.  
  
```  
=CEILING([ProductPrice],0.05)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[FLOOR Function &#40;DAX&#41;](../DAX/floor-function-dax.md)  
[ISO.CEILING Function &#40;DAX&#41;](../DAX/iso-ceiling-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
  
