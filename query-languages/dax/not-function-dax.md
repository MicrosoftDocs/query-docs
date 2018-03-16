---
title: "NOT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.NOT.f1"
helpviewer_keywords: 
  - "NOT function"
  - "logical values"
ms.assetid: cf1bd3ef-b026-43de-85bd-5873d1eb822d
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# NOT Function (DAX)
Changes FALSE to TRUE, or TRUE to FALSE.  
  
## Syntax  
  
```  
NOT(<logical>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**logical**|A value or expression that can be evaluated to TRUE or FALSE.|  
  
## Return Value  
TRUE OR FALSE.  
  
## Example  
The following example retrieves values from the calculated column that was created to illustrate the IF function. For that example, the calculated column was named using the default name, **Calculated Column1**, and contains the following formula: `=IF([Orders]<300,"true","false")`  
  
The formula checks the value in the column, [Orders], and returns "true" if the number of orders is under 300.  
  
Now create a new calculated column, **Calculated Column2**, and type the following formula.  
  
```  
=NOT([CalculatedColumn1])  
```  
For each row in **Calculated Column1**, the values "true" and "false" are interpreted as the logical values TRUE or FALSE, and the NOT function returns the logical opposite of that value.  
  
## See Also  
[TRUE Function &#40;DAX&#41;](true-function-dax.md)  
[FALSE Function &#40;DAX&#41;](false-function-dax.md)  
[IF Function &#40;DAX&#41;](if-function-dax.md)  
[DAX Function Reference](dax-function-reference.md)  
  
