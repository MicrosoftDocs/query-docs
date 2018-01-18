---
title: "Table.Column | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f31d7bcd-a3b0-4336-8c85-513eb24bee8d
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Column
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the values from a column in a table.  
  
```  
Table.Column(table as table, column as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|column|The column to check.|  
  
## <a name="__toc360789550"></a>Remarks  
  
-   **Table.Column** is similar to **Record.Field** but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```  
Table.Column(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Name")  
  
equals {"Bob", "Jim", "Paul", "Ringo"}  
```  
