---
description: "Learn more about: SAMPLE"
title: "SAMPLE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SAMPLE

Returns a sample of N rows from the specified table.  
  
## Syntax  
  
```dax
SAMPLE(<n_value>, <table>, <orderBy_expression>, [<order>[, <orderBy_expression>, [<order>]]…])  
```
  
### Parameters  

|Term|Definition|  
|---------|---------|
|n_value       |  The number of rows to return. It is any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context). If a non-integer value (or expression) is entered, the result is cast as an integer.         |
|table     |   Any DAX expression that returns a table of data from where to extract the 'n' sample rows.       |
|orderBy_expression      |   (Optional) Any scalar DAX expression where the result value is evaluated for each row of *table*.        |
|order       |  (Optional) A value that specifies how to sort *orderBy_expression* values, ascending or descending: 0 (zero), sorts in descending order of values of *order_by*. 1, ranks in ascending order of *order_by*.     |
  
## Return value

A table consisting of a sample of N rows of *table* or an empty table if *n_value* is 0 (zero) or less. If OrderBy arguments are provided, the sample will be stable and deterministic, returning the first row, the last row, and evenly distributed rows between them. If no ordering is specified, the sample will be random, not stable, and not deterministic.  
  
## Remarks  
  
- If n_value is 0 (zero) or less then SAMPLE returns an empty table.  

- In order to avoid duplicate values in the sample, the table provided as the second argument should be grouped by the column used for sorting.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
