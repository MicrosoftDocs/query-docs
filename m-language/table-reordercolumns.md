---
title: "Table.ReorderColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b90ef3fa-2fe9-4fef-af65-2b0707e74154
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReorderColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with specific columns in an order relative to one another, without changing the order of the columns that aren?t specified.  
  
```  
Table.ReorderColumns(table as table, columnOrder as list, optional missingField as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|columnOrder|The list of columns to arrange in the specific order.|  
|optional missingField|The default value of missingField is **MissingField.Error**. For more information, see Parameter Values.|  
  
## <a name="__toc360789576"></a>Remarks  
  
-   Table.ReorderColumns is similar to Record.ReorderFields applied to every row in a table.  
  
-   Columns that are not specified will remain in the same location and the specified columns will be ordered around them.  
  
## Examples  
  
```  
Table.ReorderColumns(Table.FromRecords({[CustomerID=1, Phone = "123-4567", Name ="Bob"] }), {"Name","Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|CustomerID|Name|Phone|  
|1|Bob|123-4567|  
  
```  
Table.ReorderColumns(Table.FromRecords({  
  
    [CustomerID=1, Name = "Bob", Phone = "123-4567"]  
  
}), {"Address1", "Address2"}, MissingField.UseNull)  
  
Table.ReorderColumns(Table.FromRecords({  
  
    [CustomerID=1, Name = "Bob", Phone = "123-4567"]  
  
}), {"Address1", "Address2"}, MissingField.UseNull)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|ddress1|Address2|  
|1|Bob|123-4567|null|null|  
  
