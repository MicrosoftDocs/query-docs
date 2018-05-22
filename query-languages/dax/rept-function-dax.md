---
title: "REPT Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# REPT Function (DAX)
Repeats text a given number of times. Use REPT to fill a cell with a number of instances of a text string.  
  
## Syntax  
  
```  
REPT(<text>, <num_times>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want to repeat.|  
|**num_times**|A positive number specifying the number of times to repeat text.|  
  
## Property Value/Return Value  
A string containing the changes.  
  
## Remarks  
If **number_times** is 0 (zero), REPT returns a blank.  
  
If **number_times** is not an integer, it is truncated.  
  
The result of the REPT function cannot be longer than 32,767 characters, or REPT returns an error.  
  
## Example: Repeating Literal Strings  
  
### Description  
The following example returns the string, 85, repeated three times.  
  
### Code  
  
```  
=REPT("85",3)  
```  
  
## Example: Repeating Column Values  
  
### Description  
The following example returns the string in the column, [MyText], repeated for the number of times in the column, [MyNumber]. Because the formula extends for the entire column, the resulting string depends on the text and number value in each row.  
  
### Code  
  
```  
=REPT([MyText],[MyNumber])  
```  
  
### Comments  
  
|MyText|MyNumber|CalculatedColumn1|  
|----------|------------|---------------------|  
|Text|2|TextText|  
|Number|0||  
|85|3|858585|  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
