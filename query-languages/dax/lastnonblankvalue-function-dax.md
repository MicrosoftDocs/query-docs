---
description: "Learn more about: LASTNONBLANKVALUE"
title: "LASTNONBLANKVALUE function (DAX) | Microsoft Docs"
---
# LASTNONBLANKVALUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates an expression filtered by the sorted values of a column and returns the last value of the expression that is not blank.
  
## Syntax  
  
```dax
LASTNONBLANKVALUE(<column>, <expression>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column or an expression that returns a single-column table.|  
|expression|An expression evaluated for each value of \<column>.|
  
## Return value  

The last non-blank value of \<expression> corresponding to the sorted values of \<column>.
  
## Remarks  

- The column argument can be any of the following:
  - A reference to any column.
  - A table with a single column.

- This function is different from LASTNONBLANK in that the \<column> is added to the filter context for the evaluation of \<expression>.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  

The following DAX query,

```dax
EVALUATE
SUMMARIZECOLUMNS(
  DimProduct[Class],
  "LNBV",
  LASTNONBLANKVALUE(
    DimDate[Date],
    SUM(FactInternetSales[SalesAmount])
   )
)
```

Returns,

|DimProduct[Class]|[LNBV]|
|-----------|---------------|----------|  
|L|132.44|
|H|137.6|
|M|84.97|
||2288.6|
