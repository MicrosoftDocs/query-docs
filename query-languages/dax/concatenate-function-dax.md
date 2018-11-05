---
title: "CONCATENATE Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# CONCATENATE Function (DAX)
Joins two text strings into one text string.  
  
## Syntax  
  
```dax
CONCATENATE(<text1>, <text2>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text1**, **text2**|The text strings to be joined into a single text string. Strings can include text or numbers.<br /><br />You can also use column references.|  
  
## Return Value  
The concatenated string.  
  
## Remarks  
The CONCATENATE function joins two text strings into one text string. The joined items can be text, numbers or Boolean values represented as text, or a combination of those items. You can also use a column reference if the column contains appropriate values.  
  
The CONCATENATE function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to concatenate multiple columns, you can create a series of calculations or, better, use the concatenation operator (**&amp;**) to join all of them in a simpler expression.  
  
If you want to use text strings directly, rather than using a column reference, you must enclose each string in double quotation marks.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example: Concatenation of Literals  
  
### Description  
The sample formula creates a new string value by combining two string values that you provide as arguments.  
  
### Code  
`=CONCATENATE("Hello ", "World")`  
  
## Example: Concatenation of Strings in Columns  
  
### Description  
The sample formula returns the customer's full name as listed in a phone book. Note how a nested function is used as the second argument. This is one way to concatenate multiple strings, when you have more than two values that you want to use as arguments.  
  
### Code  
`=CONCATENATE(Customer[LastName], CONCATENATE(", ", Customer[FirstName]))`  
  
## Example: Conditional Concatenation of Strings in Columns  
  
### Description  
The sample formula creates a new calculated column in the Customer table with the full customer name as a combination of first name, middle initial, and last name. If there is no middle name, the last name comes directly after the first name. If there is a middle name, only the first letter of the middle name is used and the initial letter is followed by a period.  
  
### Code  
`=CONCATENATE( [FirstName]&" ", CONCATENATE( IF( LEN([MiddleName])>1, LEFT([MiddleName],1)&" ", ""), [LastName]))`  
  
### Comments  
This formula uses nested CONCATENATE and IF functions, together with the ampersand (&amp;) operator, to conditionally concatenate three string values and add spaces as separators.  
  
## Example: Concatenation of Columns with Different Data Types  
The following example demonstrates how to concatenate values in columns that have different data types. If the value that you are concatenating is numeric, the value will be implicitly converted to text. If both values are numeric, both values will be cast to text and concatenated as if they were strings.  
  
|Product description|Product abbreviation (column 1 of composite key)|Product number (column 2 of composite key)|New generated key column|  
|-----------------------|----------------------------------------------------|----------------------------------------------|----------------------------|  
|Mountain bike|MTN|40|MTN40|  
|Mountain bike|MTN|42|MTN42|  
  
### Code  
  
```dax
=CONCATENATE('Products'[Product abbreviation],'Products'[Product number])  
```
  
### Comments  
The CONCATENATE function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to add more arguments, you can use the ampersand (&amp;) operator. For example, the following formula produces the results, MTN-40 and MTN-42.  
  
```dax
=[Product abbreviation] & "-" & [Product number]  
```
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
