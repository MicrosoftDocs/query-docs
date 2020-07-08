---
title: "CURRENCY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CURRENCY

Evaluates the argument and returns the result as currency data type.  
  
## Syntax  
  
```dax
CURRENCY(<value>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|value|Any DAX expression that returns a single scalar value where the expression is to be evaluated exactly once before all other operations. |  

## Return value

The value of the expression evaluated and returned as a currency type value.  
  
## Remarks  
  
- The CURRENCY function rounds up the 5th significant decimal, in value, to return the 4th decimal digit; rounding up occurs if the 5th significant decimal is equal or larger than 5. For example, if value is 3.6666666666666 then converting to currency returns $3.6667; however, if value is 3.0123456789 then converting to currency returns $3.0123.  
  
- If the data type of the expression is TrueFalse then CURRENCY( &lt;TrueFalse&gt;) will return $1.0000 for True values and $0.0000 for False values.  
  
- If the data type of the expression is Text then CURRENCY(&lt;Text&gt;) will try to convert text to a number; if conversion succeeds the number will be converted to currency, otherwise an error is returned.  
  
- If the data type of the expression is DateTime then CURRENCY(&lt;DateTime&gt;) will convert the datetime value to a number and that number to currency. DateTime values have an integer part that represents the number of days between the given date and 1900-03-01 and a fraction that represents the fraction of a day (where 12 hours or noon is 0.5 day). If the value of the expression is not a proper DateTime value an error is returned.  
  
## Example

Convert number 1234.56 to currency data type.  
  
```dax
= CURRENCY(1234.56)  
```

Returns the value $1234.5600.
