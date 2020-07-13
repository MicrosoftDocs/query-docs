---
title: "FIXED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# FIXED

Rounds a number to the specified number of decimals and returns the result as text. You can specify that the result be returned with or without commas.  
  
## Syntax  
  
```dax
FIXED(<number>, <decimals>, <no_commas>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number you want to round and convert to text, or a column containing a number.|  
|decimals|(optional) The number of digits to the right of the decimal point; if omitted, 2.|  
|no_commas|(optional) A logical value: if 1, do not display commas in the returned text; if 0 or omitted, display commas in the returned text.|  
  
## Return value

A number represented as text.  
  
## Remarks

- If the value used for the **decimals** parameter is negative, **number** is rounded to the left of the decimal point.  
  
- If you omit **decimals**, it is assumed to be 2.  
  
- If **no_commas** is 0 or is omitted, then the returned text includes commas as usual.  
  
- The major difference between formatting a cell containing a number by using a command and formatting a number directly with the FIXED function is that FIXED converts its result to text. A number formatted with a command from the formatting menu is still a number.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example gets the numeric value for the current row in column, PctCost, and returns it as text with 4 decimal places and no commas.  
  
```dax
= FIXED([PctCost],3,1)  
```

Numbers can never have more than 15 significant digits, but decimals can be as large as 127.  
  
## See also

[Text functions](text-functions-dax.md)  
[Math and Trig functions](math-and-trig-functions-dax.md)
