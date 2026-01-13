---
description: "Learn more about: DEPENDON"
title: "DEPENDON function (DAX) | Microsoft Docs"
ms.topic: reference
---
# DEPENDON

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Change the table expression to be dependent on outer columns, based on the table data.
  
## Syntax  
  
```dax
DEPENDON(<table expression>[, <column>[, <column>[,…]]])
```
  
### Parameters  
  
|Term|Definition|
|--------|--------------|
|table expression|Any table expression.|  
|column|Column in the table expression.|
  
## Return value

The first few columns will be remapped to be dependent on specified outer columns.
  
### Example

```dax
DEFINE TABLE VTable = SELECTCOLUMNS({"USA", "Canada", "Mexico"}, "Country", [Value])
EVALUATE SUMMARIZECOLUMNS( 
    VTable[Country],
    "Measure", SUMX(DEPENDON({("USA", 10), ("USA", 11), ("Canada", 12)}, VTable[Country]), [Value2])
)
```

This DEPENDON makes the first column depend on outer VTable[Country]. So the result table now returns table {10,11} if VTable[Country] == "USA" and returns {12} if VTable[Country] == "Canada". So the result should look like:

|VTable[Country]|Measure|  
|--------------||  
|USA|21|  
|Canada|12|

## Related content

[Filter functions](filter-functions-dax.md)  
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
