---
title: "Table.Contains | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cb1319b1-6036-45ed-83b1-8dbdd66768a0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Contains
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Determines whether the a record appears as a row in the table.  
  
```  
Table.Contains(table as table, row as record, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|row|The row to check for.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789665"></a>Remarks  
  
-   Table.Contains is similar to List.Contains but requires a table as input.  
  
## Example  
  
```  
Table.Contains(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),  
  
    [Name="Bob"])  
  
equals true  
```  
