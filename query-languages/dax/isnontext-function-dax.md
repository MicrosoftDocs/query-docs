---
description: "Learn more about: ISNONTEXT"
title: "ISNONTEXT function (DAX)"
---
# ISNONTEXT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks if a value is not text (blank cells are not text), and returns `TRUE` or `FALSE`.  
  
## Syntax  
  
```dax
ISNONTEXT(<value>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`value`|The value you want to check.|  
  
## Return value

`TRUE` if the value is not text or blank; `FALSE` if the value is text.  
  
## Remarks

- An empty string is considered text.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following examples show the behavior of the ISNONTEXT function.  
  
```dax
//RETURNS: Is Non-Text  
= IF(ISNONTEXT(1), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Non-Text  
= IF(ISNONTEXT(BLANK()), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Text  
= IF(ISNONTEXT(""), "Is Non-Text", "Is Text")  
```
  
## Related content

[Information functions](information-functions-dax.md)  
