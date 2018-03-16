---
title: "LASTNONBLANK Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.LASTNONBLANK.f1"
helpviewer_keywords: 
  - "LASTNONBLANK function"
ms.assetid: 263e764b-e6e4-4b87-9ec4-0c40255abf0a
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# LASTNONBLANK Function (DAX)
Returns the last value in the column, **column**, filtered by the current context, where the expression is not blank.  
  
## Syntax  
  
```  
LASTNONBLANK(<column>,<expression>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**column**|A column expression.|  
|**expression**|An expression evaluated for blanks for each value of **column**.|  
  
## Property Value/Return Value  
A table containing a single column and single row with the computed last value.  
  
## Remarks  
The **column** argument can be any of the following:  
  
-   A reference to any column.  
  
-   A table with a single column.  
  
-   A Boolean expression that defines a single-column table  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This function is typically used to return the last value of a column for which the expression is not blank. For example, you could get the last value for which there were sales of a product.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## See Also  
[FIRSTNONBLANK Function &#40;DAX&#41;](firstnonblank-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
[DAX Function Reference](dax-function-reference.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
