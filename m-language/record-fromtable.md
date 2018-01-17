---
title: "Record.FromTable | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 58064c8d-8097-4e01-a12c-76e2d559f907
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.FromTable
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record from a table of records containing field names and values.  
  
```  
Record.FromTable(list as table) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The Table to check.|  
  
## <a name="__toc360789195"></a>Remarks  
  
-   An Expression.Error is thrown if the fields are not unique.  
  
## <a name="__goback"></a>Example  
  
```  
let  
  
    input = Table.FromRows({{"OrderID",1} , {"CustomerID", 1}, {"Item", "Fishing rod"}, {"Price" , 100.00}}, {"Name", "Value"})  
  
in  
  
    Record.FromTable(input)  
  
equals [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
