---
title: "Table.RemoveRowsWithErrors | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b1f6452f-6810-40b0-9396-d1254b9c7e67
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.RemoveRowsWithErrors
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
