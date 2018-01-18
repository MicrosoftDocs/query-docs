---
title: "COUNT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.COUNT.f1"
helpviewer_keywords: 
  - "COUNT function"
ms.assetid: a1eec235-9117-4468-8312-3640b555706a
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# COUNT Function (DAX)
The COUNT function counts the number of cells in a column that contain numbers.  
  
## Syntax  
  
```  
COUNT(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column that contains the numbers to be counted|  
  
## Return Value  
A whole number.  
  
## Remarks  
The only argument allowed to this function is a column. The COUNT function counts rows that contain the following kinds of values:  
  
-   Numbers  
  
-   Dates  

-   Strings
  
If the row contains text that cannot be translated into a number, the row is not counted.  
  
When the function finds no rows to count, it returns a blank.  When there are rows, but none of them meet the specified criteria, then the function returns 0.  
  
## Example  
The following example shows how to count the number of numeric values in the column, ShipDate.  
  
```  
=COUNT([ShipDate])  
```  
To count logical values or text, use the COUNTA or COUNTAX functions.  
  
## See Also  
[COUNT Function &#40;DAX&#41;](../DAX/count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](../DAX/counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](../DAX/countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](../DAX/countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
