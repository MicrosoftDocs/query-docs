---
title: "SUBSTITUTEWITHINDEX Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SUBSTITUTEWITHINDEX Function (DAX)
  
Returns a table which represents a left semijoin of the two tables supplied as arguments. The semijoin is performed by using common columns, determined by common column names and common data type . The columns being joined on are replaced with a single column in the returned table which is of type integer and contains an index. The index is a reference into the right join table given a specified sort order.  
  
Columns in the right/second table supplied which do not exist in the left/first table supplied are not included in the returned table and are not used to join on.  
  
The index starts at 0 (0-based) and is incremented by one for each additional row in the right/second join table supplied. The index is based on the sort order specified for the right/second join table.  
  
## Syntax  
  
```  
SUBSTITUTEWITHINDEX(<table>, <indexColumnName>, <indexColumnsTable>, [<orderBy_expression>, [<order>][, <orderBy_expression>, [<order>]]…])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table to be filtered by performing a left semijoin with the table specified as the third argument (indexColumnsTable). This is the table on the left side of the left semijoin so the table returned includes the same columns as this table except that all common columns of the two tables will be replaced with a single index column in the table returned.|  
|indexColumnName|A string which specifies the name of the index column which is replacing all the common columns in the two tables supplied as arguments to this function.|  
|indexColumnsTable|The second table for the left semijoin. This is the table on the right side of the left semijoin. Only values present in this table will be returned by the function. Also, the columns of this table (based on column names) will be replaced with a single index column in the table returned by this function.|  
|orderBy_expression|Any DAX expression where the result value is used to specify the desired sort order of the indexColumnsTable table for generating correct index values. The sort order specified for the indexColumnsTable table defines the index of each row in the table and that index is used in the table returned to represent combinations of values in the indexColumnsTable as they appear in the table supplied as the first argument to this function.|  
|order|(Optional) A value that specifies how to sort orderBy_expression values, ascending or descending:<br /><br />Value: **Desc**. Alternative value:  **0**(zero)/**FALSE**. Sorts in descending order of values of orderBy_expression. This is the default value when order parameter is omitted.<br /><br />Value: **ASC**. Alternative value:  **1**/**TRUE**. Ranks in ascending order of orderBy_expression.|  
  
## Return Value  
A table which includes only those values present in the indexColumnsTable table and which has an index column instead of all columns present (by name) in the indexColumnsTable table.  
  
## Remarks  
This function does not guarantee any result sort order.  
  
