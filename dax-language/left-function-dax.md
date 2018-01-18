---
title: "LEFT Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.LEFT.f1"
helpviewer_keywords: 
  - "LEFT function"
ms.assetid: 9c622129-094e-4272-8e2b-368d048f7152
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# LEFT Function (DAX)
Returns the specified number of characters from the start of a text string.  
  
## Syntax  
  
```  
LEFT(<text>, <num_chars>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text string containing the characters you want to extract, or a reference to a column that contains text.|  
|**num_chars**|(optional) The number of characters you want LEFT to extract; if omitted, 1.|  
  
## Property Value/Return Value  
A text string.  
  
## Remarks  
Whereas Microsoft Excel contains different functions for working with text in single-byte and double-byte character languages, DAX works with Unicode and stores all characters as the same length; therefore, a single function is enough.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example returns the first five characters of the company name in the column [ResellerName] and the first five letters of the geographical code in the column [GeographyKey] and concatenates them, to create an identifier.  
  
```  
=CONCATENATE(LEFT('Reseller'[ResellerName],LEFT(GeographyKey,3))  
```  
If the **num_chars** argument is a number that is larger than the number of characters available, the function returns the maximum characters available and does not raise an error. For example, the column [GeographyKey] contains numbers such as 1, 12 and 311; therefore the result also has variable length.  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
