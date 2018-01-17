---
title: "Table.HasColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 386c3bfe-acf7-48cc-b5a0-bd2daab9c7af
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.HasColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns true if a table has the specified column or columns.  
  
```  
Table.HasColumns(table as table, columns as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|columns|The columns to check for as a text value or a list of text values.|  
  
## <a name="__toc360793125"></a>Remarks  
  
-   **Table.HasColumns** is similar to **Record.HasFields** but requires a table as input.  
  
## Examples  
  
```  
Table.HasColumns(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"],  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),"Name")  
  
equals true  
```  
