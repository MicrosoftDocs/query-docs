---
title: "ADDMISSINGITEMS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ADDMISSINGITEMS

Returns a table of columns if they do not already exist. The determination of which item combinations to add is based on referencing source columns which contain all the possible values for the columns. To determine the combinations of items from different columns to evaluate, AutoExist is applied for columns within the same table while [CROSSJOIN](crossjoin-function-dax.md) is applied across different tables.  
  
The ADDMISSINGITEMS function will return [BLANK](blank-function-dax.md) values for the [ISSUBTOTAL](issubtotal-function-dax.md) columns of blank rows it adds.  
  
## Syntax  
  
```dax
ADDMISSINGITEMS(<showAllColumn>[, <showAllColumn>]…, <table>, <groupingColumn>[, <groupingColumn>]…[, filterTable]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|showAllColumn|A column for which to return items with no data for the measures used.|  
|table|A table containing all items with data (NON EMPTY) for the measures used.|  
|groupingColumn|A column which is used to group by in the supplied table argument.|
|filterTable|A table representing filters to include in the logic for determining whether to add specific combinations of items with no data. Used to avoid having ADDMISSINGITEMS add in item combinations which are not present because they were removed by a filter.|  
  
## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## With ROLLUPGROUP

[ROLLUPGROUP](rollupgroup-function-dax.md) is used inside a [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) expression to reflect [ROLLUPGROUP](rollupgroup-function-dax.md)s present in the supplied table argument.  
  
If [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) is used to define the supplied table argument, or the equivalent rows and [ISSUBTOTAL](issubtotal-function-dax.md) columns were added by some other means, [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) must be used with the same arguments within ADDMISSINGITEMS. This is also true for [ROLLUPGROUP](rollupgroup-function-dax.md) if it's used with [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) to define the supplied table argument.  
  
ADDMISSINGITEMS requires if [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) is used to define the supplied table argument, [ISSUBTOTAL](issubtotal-function-dax.md) columns corresponding to each groupBy column or [ROLLUPGROUP](rollupgroup-function-dax.md) are present in the supplied table argument. Also, the names of the [ISSUBTOTAL](issubtotal-function-dax.md) columns must be supplied in the [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) expression inside the ADDMISSINGITEMS expression and they must match names of Boolean columns in the supplied table argument. This enables the ADDMISSINGITEMS function to identify blank values stemming from the fact that a row is a subtotal row from other [BLANK](blank-function-dax.md) values.  
  
If [ROLLUPGROUP](rollupgroup-function-dax.md) is used with [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) to define the supplied table argument, exactly one [ISSUBTOTAL](issubtotal-function-dax.md) column name must be supplied per [ROLLUPGROUP](rollupgroup-function-dax.md) and it must match the corresponding [ISSUBTOTAL](issubtotal-function-dax.md) column name in the supplied table argument.  
  
### Example with ROLLUPISSUBTOTAL

Add blank rows for columns with "show items with no data" turned on. The ADDMISSINGITEMS function will return NULLs/BLANKs for the [ISSUBTOTAL](issubtotal-function-dax.md) columns of blank rows it adds.  
  
```dax
VAR 'RowHeadersShowAll' =
CALCULATETABLE
(  
ADDMISSINGITEMS
(  
[Sales Territory Country],
[Sales Territory Region],
'RowHeadersInCrossTab',
ROLLUPISSUBTOTAL
(  
[Sales Territory Group],
[Subtotal for Sales Territory Group],
[Sales Territory Country],
[Subtotal for Sales Territory Country],
[Sales Territory Region],
[Subtotal for Sales Territory Region]
),
'RowHeaders'
),
'DateFilter','TerritoryFilter'
)  
```

### Example with ROLLUPGROUP  
  
```dax
VAR 'RowHeadersShowAll' =
CALCULATETABLE
(  
ADDMISSINGITEMS
(  
[Sales Territory Country],
[Sales Territory Region],
'RowHeadersInCrossTab',
ROLLUPISSUBTOTAL
(  
ROLLUPGROUP
(  
[Sales Territory Group],
[Sales Territory Country]
),
[Subtotal for Sales Territory Country],
[Sales Territory Region],
[Subtotal for Sales Territory Region]
),
'RowHeaders'
)  
```
