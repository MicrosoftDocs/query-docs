---
title: "Table.ReplaceMatchingRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Table.ReplaceMatchingRows

  
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
  
