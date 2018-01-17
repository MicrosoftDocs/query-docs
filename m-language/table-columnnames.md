---
title: "Table.ColumnNames | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6172e7b3-b97d-4bd8-80cb-3431f2eb818c
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ColumnNames
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the names of columns from a table.  
  
```  
Table.ColumnNames(table as table) as {Text}  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## <a name="__toc360789554"></a>Remarks  
  
-   **Table.ColumnNames** is similar to **Record.FieldNames** but requires a table as input.  
  
## Example  
  
```  
Table.ColumnNames(Table.FromRecords(  
  
{  
  
  [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
  [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
  [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
  [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
))  
  
equals { "CustomerID", "Name", "Phone"}  
```  
