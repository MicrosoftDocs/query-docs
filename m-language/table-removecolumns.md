---
title: "Table.RemoveColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.RemoveColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
