---
title: "ROW Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ROW.f1"
helpviewer_keywords: 
  - "ROW Function (DAX)"
ms.assetid: 8a26befc-e513-46ed-81df-ada827db65fc
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ROW Function (DAX)
Returns a table with a single row containing values that result from the expressions given to each column.  
  
## Syntax  
  
```  
ROW(<name>, <expression>[[,<name>, <expression>]…])  
```  
  
#### Parameters  
*name*  
The name given to the column, enclosed in double quotes.  
  
*expression*  
Any DAX expression that returns a single scalar value to populate. *name*.  
  
## Return Value  
A single row table  
  
## Remarks  
Arguments must always come in pairs of *name* and *expression*.  
  
## Example  
The following example returns a single row table with the total sales for internet and resellers channels.  
  
```  
ROW("Internet Total Sales (USD)", SUM(InternetSales_USD[SalesAmount_USD]),  
         "Resellers Total Sales (USD)", SUM(ResellerSales_USD[SalesAmount_USD]))  
```  
The code is split in two lines for readability purposes  
  
