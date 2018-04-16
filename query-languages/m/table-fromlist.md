---
title: "Table.FromList | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromList

  
## About  
Converts a list into a table by applying the specified splitting function to each item in the list.  
  
```  
Table.FromList(list as list, optional splitter as nullable function, optional columns as any, optional default as any, optional extraValues as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to convert.|  
|optional splitter|Splitter function.|  
|optional columns|A list of text values specifying the column names of the resulting table.|  
|optional default|A default can be provided to be used for missing values in the table.|  
|optional extraValues|Extra values for each item in the list.|  
  
## Example  
  
```  
Table.FromList(  
  
    {[CustomerID =1, Name ="Bob", Phone = "123-4567"] ,  
  
    [CustomerID =2, Name ="Jim", Phone = "987-6543"]},  
  
    Record.FieldValues, {"CustomerID", "Name", "Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
