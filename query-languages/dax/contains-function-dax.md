---
title: "CONTAINS Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.CONTAINS.f1"
helpviewer_keywords: 
  - "CONTAINS Function (DAX)"
ms.assetid: 7ebc0b4c-4988-490f-9983-8073e5d4527b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# CONTAINS Function (DAX)
Returns true if values for all referred columns exist, or are contained, in those columns; otherwise, the function returns false.  
  
## Syntax  
  
```  
CONTAINS(<table>, <columnName>, <value>[, <columnName>, <value>]…)  
```  
  
#### Parameters  
table  
Any DAX expression that returns a table of data.  
  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
value  
Any DAX expression that returns a single scalar value, that is to be sought in *columnName*. The expression is to be evaluated exactly once and before it is passed to the argument list.  
  
## Return Value  
A value of **TRUE** if each specified *value* can be found in the corresponding *columnName*, or are contained, in those columns; otherwise, the function returns **FALSE**.  
  
## Remarks  
  
-   The arguments *columnName* and *value* must come in pairs; otherwise an error is returned.  
  
-   *columnName* must belong to the specified *table*, or to a table that is related to *table*.  
  
-   If *columnName* refers to a column in a related table then it must be fully qualified; otherwise, an error is returned.  
  
## Example  
The following example creates a calculated measure that tells you whether there were any Internet sales of the product 214 and to customer 11185 at the same time.  
  
```  
=CONTAINS(InternetSales, [ProductKey], 214, [CustomerKey], 11185)  
```  
