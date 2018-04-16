---
title: "Table.AggregateTableColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.AggregateTableColumn

  
## About  
Aggregates tables nested in a specific column into multiple columns containing aggregate values for those tables.  
  
```  
Table.AggregateTableColumn(table as table, column as text, aggregations as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Table to aggregate.|  
|column|Column containing nexted table to aggragate.|  
|aggregations|Specify the columns containing the tables to aggregate, the aggregation functions to apply to the tables to generate their values, and the names of the aggregate columns to create.|  
  
## Example  
  
```  
Table.AggregateTableColumn(  
  
    Table.FromRecords(  
  
    {[t = Table.FromRecords({[a=1, b=2, c=3], [a=2,b=4,c=6]}), b = 2]}, type table [t = table [a=number, b=number, c=number], b = number]  
  
    ), "t",  
  
    {{"a", List.Sum, "sum of t.a"},  
  
     {"b", List.Min, "min of t.b"},  
  
     {"b", List.Max, "max of t.b"},  
  
     {"a", List.Count, "count of t.a"}})  
```  
  
|sumoft.a|minoft.b|maxoft.b|countoft.a|b|  
|------------|------------|------------|--------------|-----|  
|3|2|4|2|2|  
  
