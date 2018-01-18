---
title: "Table.ToRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f2ab5209-6a7f-4878-9c27-27c7406a77b8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ToRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a nested list of row values from an input table.  
  
```  
Table.ToRows(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## Example  
  
```  
let  
  
    Source = Table.ToRows(Table.FromRecords({  
  
    [CustomerID =1, Name ="Bob", Phone = "123-4567"],  
  
    [CustomerID =2, Name ="Jim", Phone = "987-6543"],  
  
    [CustomerID =3, Name ="Paul", Phone = "543-7890"]  
  
}))  
  
in  
  
    Source  
  
equals  
  
{  
  
    {1, "Bob", "123-4567"},  
  
    {2, "Jim", "987-6543"},  
  
    {3,  "Paul", "543-7890"}  
  
}  
```  
