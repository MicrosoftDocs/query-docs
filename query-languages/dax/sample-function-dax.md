---
title: "SAMPLE Function (DAX) | Microsoft Docs"
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
ms.assetid: 44678922-9ee2-4e80-9bb8-6d5975d9d84a
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SAMPLE Function (DAX)
Returns a sample of N rows from the specified table.  
  
## Syntax  
  
```  
SAMPLE(<n_value>, <table>, <orderBy_expression>, [<order>[, <orderBy_expression>, [<order>]]…])  
```  
  
#### Parameters  
n_value  
The number of rows to return. It is any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context). If a non-integer value (or expression) is entered, the result is cast as an integer.  
  
table  
Any DAX expression that returns a table of data from where to extract the ‘n’ sample rows.  
  
orderBy_expression  
(Optional) Any scalar DAX expression where the result value is evaluated for each row of *table*.  
  
order  
(Optional) A value that specifies how to sort *orderBy_expression* values, ascending or descending:  
  
||||  
|-|-|-|  
|**value**|**alternate value**|**Description**|  
|0 (zero)|FALSE|Sorts in descending order of values of *order_by*.<br /><br />This is the default value when *order* parameter is omitted.|  
|1|TRUE|Ranks in ascending order of *order_by*.|  
  
## Return Value  
A table consisting of a sample of N rows of *table* or an empty table if *n_value* is 0 (zero) or less. If OrderBy arguments are provided, the sample will be stable and deterministic, returning the first row, the last row, and evenly distributed rows between them. If no ordering is specified, the sample will be random, not stable, and not deterministic.  
  
## Remarks  
  
-   If n_value is 0 (zero) or less then SAMPLE returns an empty table.  
  
-   In order to avoid duplicate values in the sample, the table provided as the second argument should be grouped by the column used for sorting.  
  
