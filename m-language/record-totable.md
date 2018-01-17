---
title: "Record.ToTable | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d87a9ac4-ce93-4dd3-b84a-bca0ac65c481
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.ToTable
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table of records containing field names and values from an input record.  
  
```  
Record.ToTable(record as record) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to convert.|  
  
## <a name="__toc360789191"></a>Remarks  
  
-   The type of the return value of this function is {[Name = text, Value = any ]}.  
  
## Example  
  
```  
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] )  
  
equals  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
