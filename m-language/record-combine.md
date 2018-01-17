---
title: "Record.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cb2b0fb3-e172-4c52-a8d3-1620030851a8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.Combine
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Combines the records in a list.  
  
```  
Record.Combine(list as list) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The list of records to combine.|  
  
## <a name="__toc360789157"></a>Remarks  
If the list contains non-record values, an error is returned.  
  
## <a name="__goback"></a>Example  
  
```  
Record.Combine({ [CustomerID =1], [Name ="Bob"] , [Phone =  "123-4567"] })  
```  
  
```  
equals [CustomerID=1, Name="Bob", Phone="123-4567"]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
