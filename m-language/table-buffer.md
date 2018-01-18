---
title: "Table.Buffer | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6ce1d7a9-e3fb-4cce-9af2-e219ae2ed53c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Buffer
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Buffers a table into memory, isolating it from external changes during evaluation.  
  
```  
Table.Buffer(table as table) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to buffer.|  
  
## <a name="__toc360789722"></a>Remarks  
  
-   Table.Buffer is similar to List.Buffer but requires a table as input.  
  
## Example  
  
```  
Table.Buffer(Sql.Database("localhost", "Northwind")[Customers]) equals Buffered copy of the Customers table  
```  
