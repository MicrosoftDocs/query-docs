---
description: "Learn more about: LEFT"
title: "LEFT function (DAX) | Microsoft Docs"
---
# LEFT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the specified number of characters from the start of a text string.  
  
## Syntax  
  
```dax
LEFT(<text>, <num_chars>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text string containing the characters you want to extract, or a reference to a column that contains text.|  
|num_chars|(optional) The number of characters you want LEFT to extract; if omitted, 1.|  
  
## Return value

A text string.  
  
## Remarks

- Whereas Microsoft Excel contains different functions for working with text in single-byte and double-byte character languages, DAX works with Unicode and stores all characters as the same length; therefore, a single function is enough.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example returns the first five characters of the company name in the column [ResellerName] and the first five letters of the geographical code in the column [GeographyKey] and concatenates them, to create an identifier.  
  
```dax
= CONCATENATE(LEFT('Reseller'[ResellerName],LEFT(GeographyKey,3))  
```

If the **num_chars** argument is a number that is larger than the number of characters available, the function returns the maximum characters available and does not raise an error. For example, the column [GeographyKey] contains numbers such as 1, 12 and 311; therefore the result also has variable length.  
  
## Related content

[Text functions](text-functions-dax.md)
