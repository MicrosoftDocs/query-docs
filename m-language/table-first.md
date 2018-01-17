---
title: "Table.First | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 78f754bf-a859-47d8-8695-d4a6a54eaa55
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.First
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the first row from a table.  
  
```  
Table.First(table as table, optional default as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|optional default|Optional default value.|  
  
## <a name="__toc360789480"></a>Remarks  
  
-   If the table is empty, **Table.First** returns null.  
  
## Example  
  
```  
Table.First(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]  
  
}))  
```  
  
|Name|Value|  
|--------|---------|  
|CustomerID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
