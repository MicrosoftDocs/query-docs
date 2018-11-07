---
title: "SUBSTITUTE Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SUBSTITUTE Function (DAX)
Replaces existing text with new text in a text string.  
  
## Syntax  
  
```dax
SUBSTITUTE(<text>, <old_text>, <new_text>, <instance_num>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text in which you want to substitute characters, or a reference to a column containing text.|  
|old_text|The existing text that you want to replace.|  
|new_text|The text you want to replace **old_text** with.|  
|instance_num|(optional) The occurrence of **old_text** you want to replace. If omitted, every instance of **old_text** is replaced|  
  
## Property Value/Return value  
A string of text.  
  
## Remarks  
Use the SUBSTITUTE function when you want to replace specific text in a text string; use the REPLACE function when you want to replace any text of variable length that occurs in a specific location in a text string.  
  
The SUBSTITUTE function is case-sensitive. If case does not match between **text** and **old_text**, SUBSTITUTE will not replace the text.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example: Substitution within a String  
  
### Description  
The following formula creates a copy of the column [Product Code] that substitutes the new product code **NW** for the old product code **PA** wherever it occurs in the column.  
  
### Code  
  
```dax
=SUBSTITUTE([Product Code], "NW", "PA")  
```
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[REPLACE Function &#40;DAX&#41;](replace-function-dax.md)  
  
