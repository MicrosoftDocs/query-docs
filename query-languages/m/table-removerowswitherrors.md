---
title: "Table.RemoveRowsWithErrors | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.RemoveRowsWithErrors

  
## About  
Returns a table with all rows removed from the table that contain an error in at least one of the cells in a row.  
  
```  
Table.RemoveRowsWithErrors(table as table,  optional columns as nullable list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional columns|Only cells in the column list are inspected for errors.|  
  
## <a name="__toc360789515"></a>Remarks  
  
-   Only errors detected by directly accessing the cell are considered. Errors nested more deeply, such as a structured value in a cell, are ignored.  
  
## Example  
  
```  
Table.RemoveRowsWithErrors(  
  
    Table.FromRecords({[Column1=...],[Column1=2], [Column1=3]}))  
  
equals  
```  
  
|Column1|  
|-----------|  
|2|  
|3|  
  
