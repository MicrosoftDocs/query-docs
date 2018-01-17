---
title: "Table.RenameColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 74b26a6f-d7fa-4ed8-a143-2e0c450b1ebc
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.RenameColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with the columns renamed as specified.  
  
```  
Table.RenameColumns(table as table, renames as list, optional missingField as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|renames|The list of values to rename to.|  
|optional missingField|The default value of missingField is **MissingField.Error**. For more information, see Parameter Values.|  
  
## <a name="__toc360789580"></a>Remarks  
  
-   Table.RenameColumns is similar to Record.RenameFields applied to every row in a table.  
  
## Examples  
  
```  
Table.RenameColumns(Table.FromRecords({  
  
    [CustomerNum=1, Name="Bob", Phone = "123-4567"]}),  
  
    {"CustomerNum", "CustomerID"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
  
```  
Table.RenameColumns(Table.FromRecords({  
  
    [CustomerID=1, Name="Bob", Phone = "123-4567"]}), {"NewCol", "NewColumn"}, MissingField.UseNull)  
```  
  
|CustomerID|Name|Phone|NewColumn|  
|--------------|--------|---------|-------------|  
|1|Bob|123-4567|null|  
  
