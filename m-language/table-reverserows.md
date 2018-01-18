---
title: "Table.ReverseRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9567525e-c41f-444b-82f9-13961b1e62cd
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReverseRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with the rows in reverse order.  
  
```  
Table.ReverseRows(table as table) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
  
## <a name="__toc360789526"></a>Remarks  
  
-   Table.ReverseRows is similar to List.Reverse but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```  
Table.ReverseRows(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
))  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|4|Ringo|232-1550|  
|3|Paul|543-7890|  
|2|Jim|987-6543|  
|1|Bob|123-4567|  
  
