---
title: "ADDMISSINGITEMS Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ADDMISSINGITEMS Function (DAX)
  
Adds combinations of items from multiple columns to a table if they do not already exist. The determination of which item combinations to add is based on referencing source columns which contain all the possible values for the columns.  
  
To determine the combinations of items from different columns to evaluate: AutoExist is applied for columns within the same table while CrossJoin is applied across different tables.  
  
The ADDMISSINGITEMS function will return BLANK values for the IsSubtotal columns of blank rows it adds.  
  
## Syntax  
  
```dax
ADDMISSINGITEMS(<showAllColumn>[, <showAllColumn>]…, <table>, <groupingColumn>[, <groupingColumn>]…[, filterTable]…)  
```
  
```dax
ADDMISSINGITEMS(<showAllColumn>[, <showAllColumn>]…, <table>, [ROLLUPISSUBTOTAL(]<groupingColumn>[, <isSubtotal_columnName>][, <groupingColumn>][, <isSubtotal_columnName>]…[)], [, filterTable]…)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**showAllColumn**|A column for which to return items with no data for the measures used.|  
|**table**|A table containing all items with data (NON EMPTY) for the measures used.|  
|**groupingColumn**|A column which is used to group by in the supplied table argument.|  
|**isSubtotal_columnName**|A Boolean column in the supplied table argument which contains ISSUBTOTAL values for the corresponding groupingColumn column.|  
|**filterTable**|A table representing filters to include in the logic for determining whether to add specific combinations of items with no data. Used to avoid having ADDMISSINGITEMS add in item combinations which are not present because they were removed by a filter.|  
  
## ADDMISSINGITEMS with ROLLUPGROUP  
ROLLUPGROUP is used inside the ROLLUPISSUBTOTAL function to reflect ROLLUPGROUPs present in the supplied table argument.  
  
**Restrictions**  
  
-   If ROLLUPISSUBTOTAL was used to define the supplied table argument (or the equivalent rows and ISSUBTOTAL columns were added by some other means), ROLLUPISSUBTOTAL must be used with the same arguments within ADDMISSINGITEMS. This is also true for ROLLUPGROUP if it was used with ROLLUPISSUBTOTAL to define the supplied table argument.  
  
-   The ADDMISSINGITEMS function requires that, if ROLLUPISSUBTOTAL was used to define the supplied table argument, ISSUBTOTAL columns corresponding to each group by column, or ROLLUPGROUP, are present in the supplied table argument. Also, the names of the ISSUBTOTAL columns must be supplied in the ROLLUPISSUBTOTAL function inside ADDMISSINGITEMS and they must match names of Boolean columns in the supplied table argument. This enables the ADDMISSINGITEMS function to identify BLANK values stemming from the fact that a row is a subtotal row from other BLANK values.  
  
-   If ROLLUPGROUP was used with ROLLUPISSUBTOTAL to define the supplied table argument, exactly one ISSUBTOTAL column name must be supplied per ROLLUPGROUP and it must match the corresponding ISSUBTOTAL column name in the supplied table argument.  
  
## Example  
Add blank rows for columns with "show items with no data" turned on. The ADDMISSINGITEMS function will return NULLs/BLANKs for the IsSubtotal columns of blank rows it adds.  
  
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

Example with ROLLUPGROUP  
  
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
