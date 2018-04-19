---
title: "Table.FromRecords | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromRecords

  
## About  
Returns a table from a list of records.  
  
```  
Table.FromRecords(records as list, optional columns as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|records|The List to convert.|  
|optional columns|An optional list of column names, or a table type could be provided as the second argument, which much match names found in the records. Record fields which don’t appear in the list are ignored.|  
  
## <a name="__goback"></a>Examples  
  
```  
Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
