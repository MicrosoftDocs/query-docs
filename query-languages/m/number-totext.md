---
title: "Number.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 02667f5d-ccf5-4cc2-b898-5b5b1c9b1b63
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.ToText

  
## About  
Returns a text value from a number value.  
  
```  
Number.ToText(number as number, optional format as nullable text, optional culture as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|Number value to convert to text.|  
|optional format|An optional text value used to format common numeric values.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## <a name="__toc360788713"></a>Format Settings  
  
|Setting|Name|Description|  
|-----------|--------|---------------|  
|D or d|Decimal|Formats the result as integer digits with an optional negative sign. The precision setting controls the number of digits in the output.|  
|E or e|Exponential<br /><br />(scientific)|Exponential notation. The precision setting controls the maximum number of decimal digits (default is 6).|  
|F or f|Fixed-point|Integral and decimal digits with optional negative sign.|  
|G or g|General|Most compact form of either fixed-point or scientific.|  
|N or n|Number|Integral and decimal digits, group separators, and a decimal separator with optional negative sign.|  
|P or p|Percent|Number multiplied by 100 and displayed with a percent symbol.|  
|R or r|Round-trip|Round-trip an identical number. The precision setting is ignored.|  
|X or x|Hexadecimal|A hexadecimal text value.|  
|Any other single character|Unknown<br /><br />setting|Throws **Expression.Error** error|  
  
Examples  
  
```  
Number.ToText(10, "D", "") equals 10  
  
Number.ToText(10, "E", "") equals 1.000000E+001  
  
Number.ToText(10, "F", "") equals 10.00  
  
Number.ToText(10, "G", "") equals 10  
  
Number.ToText(10, "N", "") equals 10.00  
  
Number.ToText(.10, "P", "") equals 10.00%  
```  
