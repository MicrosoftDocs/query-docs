---
title: "Record.FromList | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Record.FromList

  
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
  
