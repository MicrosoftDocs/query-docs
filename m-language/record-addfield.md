---
title: "Record.AddField | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c3b29fd9-ee68-44e6-9d43-4547d9f66a74
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.AddField
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Adds a field from a field name and value.  
  
```  
Record.AddField (record as record, fieldName as text, value as any,optional delayed as nullable logical) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|fieldName|The value to name the field.|  
|value|The value to add to the field.|  
|optional delayed|Indicates whether the field value or a function that computes the field value.|  
  
## Example  
  
```  
Record.AddField( [CustomerID = 1, Name = "Bob", Phone = "123-4567"] , "Address", "123 Main St.")  
```  
  
```  
equals [CustomerID=1, Name= "Bob", Phone="123-4567", Address="123 Main St."]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Phone|123-4567|  
|Address|123 Main St.|  
  
