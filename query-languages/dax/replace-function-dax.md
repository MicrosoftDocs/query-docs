---
description: "Learn more about: REPLACE"
title: "REPLACE function (DAX) | Microsoft Docs"
---
# REPLACE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

REPLACE replaces part of a text string, based on the number of characters you specify, with a different text string.  
  
## Syntax  
  
```dax
REPLACE(<old_text>, <start_num>, <num_chars>, <new_text>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`old_text`|The string of text that contains the characters you want to replace, or a reference to a column that contains text.|  
|`start_num`|The position of the character in `old_text` that you want to replace with `new_text`.|  
|`num_chars`|The number of characters that you want to replace. **Warning:** If the argument, `num_chars`, is a blank or references a column that evaluates to a blank, the string for `new_text` is inserted at the position, `start_num`, without replacing any characters. This is the same behavior as in Excel.|  
|`new_text`|The replacement text for the specified characters in `old_text`.|  
  
## Return value

A text string.  
  
## Remarks

- Whereas Microsoft Excel has different functions for use with single-byte and double-byte character languages, DAX uses Unicode and therefore stores all characters as the same length.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following formula creates a new calculated column that replaces the first two characters of the product code in column, [ProductCode], with a new two-letter code, OB.  
  
```dax
= REPLACE('New Products'[Product Code],1,2,"OB")  
```
  
## Related content

[Text functions](text-functions-dax.md)  
[SUBSTITUTE function](substitute-function-dax.md)  
