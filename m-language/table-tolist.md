---
title: "Table.ToList | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 163f3753-abd6-4d9e-bf82-408b86a554b1
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ToList
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table into a list by applying the specified combining function to each row of values in a table.  
  
```  
Table.ToList(table as table,  optional combiner as nullable function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
|optional combiner|The combiner function is applied to each row in the table to produce a single value for the row.|  
  
## <a name="__goback"></a>Example  
  
```  
let  
  
    input = Table.FromRows({  
  
    {Number.ToText(1),"Bob", "123-4567" },  
  
    {Number.ToText(2), "Jim", "987-6543" },  
  
    {Number.ToText(3), "Paul", "543-7890" }})  
  
in  
  
    Table.ToList(input, Combiner.CombineTextByDelimiter(","))  
  
equals  
  
{  
  
    "1,Bob,123-4567",  
  
    "2,Jim,987-6543",  
  
    "3,Paul,543-7890"  
  
}  
```  
