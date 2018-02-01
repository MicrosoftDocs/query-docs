---
title: "PRODUCTX Function (DAX) | Microsoft Docs"
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
ms.assetid: acdacdf8-87b2-4b9c-9c95-1cb8ec4c28a0
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# PRODUCTX Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Microsoft Power Pivot in Excel 2016 Preview editions, and Microsoft Power BI Designer Preview only. Information provided here is subject to change.  
  
Returns the product of an expression evaluated for each row in a table.  
  
To return the product of the numbers in a column, use [PRODUCT Function &#40;DAX&#41;](product-function-dax.md).  
  
## Syntax  
  
```  
PRODUCTX(<table>, <expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The PRODUCTX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the product, or an expression that evaluates to a column.  
  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
## Example  
The following computes the future value of an investment:  
  
```  
= [PresentValue] * PRODUCTX( AnnuityPeriods, 1+[FixedInterestRate] )  
```  
  
## See Also  
[PRODUCT Function &#40;DAX&#41;](product-function-dax.md)  
  
