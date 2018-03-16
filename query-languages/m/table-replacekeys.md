---
title: "Table.ReplaceKeys | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 54a1517c-5b16-466e-ad44-f239e5c1f37c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ReplaceKeys

  
## About  
Returns a new table with new key information set in the **keys** argument.  
  
```  
Table.ReplaceKeys(table as table, keys as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Table to modify.|  
|keys|A list with two fields: Columns and Primary. Columns is a list of columns that are keys. Primary is a primary key.|  
  
## Example  
  
```  
Table.ReplaceKeys(Table.FromRecords({[A={[B=1], [B=2]}, C=1]}), {[Columns = {"C"}, Primary = true]})  
```  
