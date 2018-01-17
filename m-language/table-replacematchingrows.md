---
title: "Table.ReplaceMatchingRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f9e23a99-7239-497c-b37c-344fe50c4712
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReplaceMatchingRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces specific rows from a table with the new rows.  
  
```  
Table.ReplaceMatchingRows(table as table, replacements as list, optional equationCriteria as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|replacements|The List of replacement rows.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789696"></a>Remarks  
  
-   Table.ReplaceMatchingRows is similar to List.ReplaceMatchingRows but requires a table as input.  
  
-   The new rows must be compatible with the type of the table .  
  
## Example  
  
```  
Table.ReplaceMatchingRows(  
  
Table.FromRecords(  
  
{  
  
 [Column1 = 1, Column2 = 2],  
  
 [Column1 = 2, Column2 = 3],  
  
 [Column1 = 3, Column2 = 4],  
  
 [Column1 = 1, Column2 = 2]  
  
}),{  
  
{[Column1 = 1, Column2 = 2],  
  
 [Column1 = -1, Column2 = -2]},  
  
{[Column1  = 2, Column2 = 3],  
  
 [Column1  = -2, Column2 = -3]} })  
```  
  
|Column1|Column2|  
|-----------|-----------|  
|-1|-2|  
|-2|-3|  
|3|4|  
|-1|-2|  
  
