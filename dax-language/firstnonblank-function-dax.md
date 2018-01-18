---
title: "FIRSTNONBLANK Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FIRSTNONBLANK.f1"
helpviewer_keywords: 
  - "FIRSTNONBLANK function"
ms.assetid: 05e98021-0694-401e-b1ed-e7c0ca32bcbe
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# FIRSTNONBLANK Function (DAX)
Returns the first value in the column, **column**, filtered by the current context, where the expression is not blank.  
  
## Syntax  
  
```  
FIRSTNONBLANK(<column>,<expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|A column expression.|  
|**expression**|An expression evaluated for blanks for each value of **column**.|  
  
## Property Value/Return Value  
A table containing a single column and single row with the computed first value.  
  
## Remarks  
The **column** argument can be any of the following:  
  
-   A reference to any column.  
  
-   A table with a single column.  
  
-   A Boolean expression that defines a single-column table .  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](../DAX/calculate-function-dax.md).  
  
This function is typically used to return the first value of a column for which the expression is not blank. For example, you could get the last value for which there were sales of a product.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## See Also  
[LASTNONBLANK Function &#40;DAX&#41;](../DAX/lastnonblank-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
[DAX Function Reference](../DAX/dax-function-reference.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
