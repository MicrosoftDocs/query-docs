---
title: "Table.ReplaceValue | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceValue

  
## About  
Replaces oldValue with newValue in specific columns of a table, using the provided replacer function, such as text.Replace or Value.Replace.  
  
## Syntax

<pre>
Table.ReplaceValue(table as table, oldValue as any, newValue as any,replacer as function, columnsToSearch as {Text}) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|oldValue|The old value to modify.|  
|newValue|The new value to replace with.|  
|replacer|The replacer function to use, such as Text.Replace or Value.Replace.|  
|columnsToSearch|The list of columns to search through.|  
  
## Examples  
  
```powerquery-m
Table.ReplaceValue(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),  
  
    "Bob",  
  
    "New Customer Name",  
  
    Text.Replace, {"Name"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|New Customer Name|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
