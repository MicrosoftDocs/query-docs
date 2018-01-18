---
title: "MID Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.MID.f1"
helpviewer_keywords: 
  - "MID function"
ms.assetid: 69ed708a-ee0c-4327-9806-f8a0c9afa54d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MID Function (DAX)
Returns a string of characters from the middle of a text string, given a starting position and length.  
  
## Syntax  
  
```  
MID(<text>, <start_num>, <num_chars>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text string from which you want to extract the characters, or a column that contains text.|  
|**start_num**|The position of the first character you want to extract. Positions start at 1.|  
|**num_chars**|The number of characters to return.|  
  
## Property Value/Return Value  
A string of text of the specified length.  
  
## Remarks  
Whereas Microsoft Excel has different functions for working with single-byte and double-byte characters languages, DAX uses Unicode and stores all characters with the same length.  
  
## Example  
The following examples return the same results, the first 5 letters of the column, [ResellerName]. The first example uses the fully qualified name of the column and specifies the starting point; the second example omits the table name and the parameter, **num_chars**.  
  
```  
=MID('Reseller'[ResellerName],5,1))  
=MID([ResellerName,5])  
```  
The results are the same if you use the following formula:  
  
`=LEFT([ResellerName],5)`  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
