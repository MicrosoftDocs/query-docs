---
title: "SEARCH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SEARCH

Returns the number of the character at which a specific character or text string is first found, reading left to right. Search is case-insensitive and accent sensitive.  
  
## Syntax  
  
```dax
SEARCH(<find_text>, <within_text>[, [<start_num>][, <NotFoundValue>]])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|find_text|The text that you want to find.<br /><br />You can use wildcard characters — the question mark (?) and asterisk (\*) — in **find_text**. A question mark matches any single character; an asterisk matches any sequence of characters. If you want to find an actual question mark or asterisk, type a tilde (~) before the character.|  
|within_text|The text in which you want to search for **find_text**, or a column containing text.|  
|start_num|(optional) The character position in **within_text** at which you want to start searching. If omitted, 1.|  
|NotFoundValue|(optional) The value that should be returned when the operation does not find a matching substring, typically 0, -1, or BLANK().|  
  
## Return value

The number of the starting position of the first text string from the first character of the second text string.  
  
## Remarks  
  
- The search function is case insensitive. Searching for "N" will find the first occurrence of 'N' or 'n'.  

- The search function is accent sensitive. Searching for "á" will find the first occurrence of 'á' but no occurrences of 'a', 'à', or the capitalized versions 'A', 'Á'.  

- By using this function, you can locate one text string within a second text string, and return the position where the first string starts.  

- You can use the SEARCH function to determine the location of a character or text string within another text string, and then use the MID function to return the text, or use the REPLACE function to change the text.  

- If the **find_text** cannot be found in **within_text**, the formula returns an error. This behavior is like Excel, which returns #VALUE if the substring is not found. Nulls in **within_text** will be interpreted as an empty string in this context.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example: Search within a String  

The following formula finds the position of the letter "n" in the word "printer".  
  
```dax
= SEARCH("n","printer")  
```

The formula returns 4 because "n" is the fourth character in the word "printer."  
  
## Example: Search within a Column  

You can use a column reference as an argument to SEARCH. The following formula finds the position of the character "-" (hyphen) in the column, [PostalCode].   
  
```dax
= SEARCH("-",[PostalCode])  
```

The return result is a column of numbers, indicating the index position of the hyphen.  
  
## Example: Error-Handling with SEARCH  

The formula in the preceding example will fail if the search string is not found in every row of the source column. Therefore, the next example demonstrates how to use IFERROR with the SEARCH function, to ensure that a valid result is returned for every row.  
  
The following formula finds the position of the character "-" within the column, and returns -1 if the string is not found.  
  
```dax
= IFERROR(SEARCH("-",[PostalCode]),-1)  
```

The data type of the value that you use as an error output must match the data type of the non-error output type. In this case, you provide a numeric value to be output in case of an error because SEARCH returns an integer value. However, you could also return a blank (empty string) by using `BLANK()` as the second argument to IFERROR.  
  
## See also

[MID](mid-function-dax.md)  
[REPLACE](replace-function-dax.md)  
[Text functions](text-functions-dax.md)  
