---
title: "Table.FromPartitions | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromPartitions

  
## About  
Returns a table that is the result of combining a set of partitioned tables into new columns. The type of the column can optionally be specified, the default is any.  
  
```  
Table.FromPartitions ( partitionColumn as text, partitions as list, optional partitionColumnType as nullable type) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|partitionColumn|The name of the column where the values from the paritions will added.|  
|partitions|The list of partitions to combine, specificed in  {value, table} pairs.|  
|Optional partitionColumnType|The type of the resulting column (default is any).|  
  
## Example  
  
```  
Table.FromPartitions("Year",  
  
{{1994, Table.FromPartitions("Month", {  
  
    {"Jan", Table.FromPartitions("Day", {  
  
        {1, #table({"Column1"},{{"Column1 Value 1"}})},  
  
        {2, #table({"Column1"},{{"Column1 Value 2"}})}})},  
  
        {"Feb", Table.FromPartitions("Day",  
  
        {{3, #table({"Column1"},{{"Column1 Value 3"}})},  
  
        {4,  #table({"Column1"},{{"Column1 Value 4"}  
  
})}})}})}})  
  
equals  
```  
  
|Column1|Day|Month|Year|  
|-----------|-------|---------|--------|  
|Column1 Value 1|1|Jan|1994|  
|Column1 Value 2|2|Jan|1994|  
|Column1 Value 3|3|Feb|1994|  
|Column1 Value 4|4|Feb|1994|  
  
