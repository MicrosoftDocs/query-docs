---
description: "Learn more about: EXACT"
title: "EXACT function (DAX)"
---
# EXACT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Compares two text strings and returns `TRUE` if they are exactly the same, otherwise returns `FALSE`. EXACT is case-sensitive but ignores formatting differences. EXACT is case-sensitive
  
## Syntax  
  
```dax
EXACT(<text1>,<text2>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`text1`|The first text string or column that contains text.|  
|`text2`|The second text string or column that contains text.|  
  
## Return value

True or False. (Boolean)  
  
## Example

The following formula used in a calculated column in the Product table checks the value of Product for the current row against the value of Model for the current row, and returns True if they are the same, and returns False if they are different.  

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
= EXACT([Product], [Model])  
```
  
## Related content

[Text functions](text-functions-dax.md)  
