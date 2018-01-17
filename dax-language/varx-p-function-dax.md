---
title: "VARX.P Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.VARX.P.f1"
helpviewer_keywords: 
  - "VARX.P Function (DAX)"
ms.assetid: c6fc739d-e51d-44d7-9d4d-e03283f0f435
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# VARX.P Function (DAX)
Returns the variance of the entire population.  
  
## Syntax  
  
```  
VARX.P(<table>, <expression>)  
```  
  
#### Parameters  
*table*  
Any DAX expression that returns a table of data.  
  
*expression*  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
## Return Value  
A number with the variance of the entire population.  
  
## Exceptions  
  
## Remarks  
  
1.  VARX.P evaluates &lt;expression&gt; for each row of &lt;table&gt; and returns the variance of &lt;expression&gt; assuming that &lt;table&gt; refers to the entire population.. If &lt;table&gt; represents a sample of the population, then compute the variance by using VARX.S.  
  
2.  VARX.P uses the following formula:  
  
    ∑(x - x̃)²/n  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a calculated column that calculates the variance of the unit price per product, when the formula is used in the Product table  
  
```  
=VARX.P(InternetSales_USD, InternetSales_USD[UnitPrice_USD] –(InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```  
