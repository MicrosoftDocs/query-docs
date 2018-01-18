---
title: "Table.RemoveLastN | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 17107667-064a-4a40-a8b5-396f076b6e75
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.RemoveLastN
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with the specified number of rows removed from the table starting at the last row. The number of rows removed depends on the optional countOrCondition parameter.  
  
```  
Table.RemoveLastN( table as table, optional countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to remove rows from.|  
|optional countOrCondition|Optional number of rows or condition to remove rows, default is 1|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   If countOrCondidtion is omitted only the first row is removed  
  
-   If countOrCondidtion is a number, that many rows (starting from the top) will be removed)  
  
-   If countOrCondidtion is a condition, the rows that meet the condition will be removed until a rows does not meet the condition  
  
## Example  
  
```  
Table.RemoveLastN(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
```  
Table.RemoveLastN(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), each _ [CustomerID] > 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
