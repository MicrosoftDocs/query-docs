---
title: "Record.FromList | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b682c77d-7d69-4dcb-9d5f-008f4d35f5b3
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.FromList
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record from a list of field values and a set of field names.  
  
```  
Record.FromList(list as list, fields as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The list of values in the record to check.|  
|fields|The set of fields corresponding to the values. The fields can be specific either by a list of text values or a record type.|  
  
## <a name="__toc360789944"></a>Remarks  
  
-   An Expression.Error is thrown if the fields are not unique.  
  
## Examples  
  
```  
Record.FromList  
  
(  
  
    {1, "Bob", "123-4567"},  
  
    type [CustomerID = number, Name = text, Phone = number]  
  
)  
  
equals [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
