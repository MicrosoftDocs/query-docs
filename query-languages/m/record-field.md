---
title: "Record.Field | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.Field

  
## About  
Returns the value of the given field.  This function can be used to dynamically create field lookup syntax for a given record. In that way it is a dynamic verison of the record[field] syntax.  
  
```  
Record.Field(record as record, field as text) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
|field|The field to obain the value for.|  
  
## <a name="__goback"></a>Example  
  
```  
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID") equals 1  
```  
