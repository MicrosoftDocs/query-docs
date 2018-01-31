---
title: "STDEVX.S Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.STDEVX.S.f1"
helpviewer_keywords: 
  - "STDEVX.S Function (DAX)"
ms.assetid: d1524ed0-9377-4d4c-a17f-521c1d3e7bf6
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# STDEVX.S Function (DAX)
Returns the standard deviation of a sample population.  
  
## Syntax  
  
```  
STDEVX.S(<table>, <expression>)  
```  
  
#### Parameters  
table  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
expression  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
## Return Value  
A number with the standard deviation of a sample population.  
  
## Exceptions  
  
## Remarks  
  
1.  STDEVX.S evaluates *expression* for each row of *table* and returns the standard deviation of *expression* assuming that *table* refers to a sample of the population. If *table* represents the entire population, then compute the standard deviation by using STDEVX.P.  
  
2.  STDEVX.S uses the following formula:  
  
    √[∑(x - x̃)²/(n-1)]  
  
    where x̃ is the average value of x for the entire population  
  
    and n is the population size  
  
3.  Blank rows are filtered out from *columnName* and not considered in the calculations.  
  
4.  An error is returned if *columnName* contains less than 2 non-blank rows.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example shows the formula for a calculated column that estimates the standard deviation of the unit price per product for a sample population, when the formula is used in the Product table.  
  
```  
=STDEVX.S(RELATEDTABLE(InternetSales_USD), InternetSales_USD[UnitPrice_USD] – (InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))  
```  
