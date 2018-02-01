---
title: "Table.RemoveColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6265190e-2f58-4300-85b8-df88fc1a67d3
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.RemoveColumns

  
## About  
Returns a table without a specific column or columns.  
  
```  
Table.RemoveColumns(table as table, columns as any, optional missingField as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|columns|A text value or a list of text values with the names of the columns to remove. missingField is a number value provided to specify handling for missing fields.|  
|optional missingField|The default value of missingField is **MissingField.Error.** For more information, see Parameter Values.|  
  
## <a name="__toc360789572"></a>Remarks  
  
-   **Table.RemoveColumns** is similar to **Record.RemoveFields** applied to every row in a table.  
  
## Examples  
  
```  
Table.RemoveColumns(Table.FromRecords({[CustomerID=1, Name="Bob", Phone = "123-4567"]}), "Phone")  
```  
  
|CustomerID|Name|  
|--------------|--------|  
|1|Bob|  
  
