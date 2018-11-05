---
title: "Table.TransformColumnNames | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.TransformColumnNames

  
## About  
Transforms column names by using the given `nameGenerator` function. Valid options:  `MaxLength` specifies the maximum length of new column names. If the given function results with a longer column name, the long name will be trimmed.  `Comparer` is used to control the comparison while generating new column names. Comparers can be used to provide case insensitive or culture and locale aware comparisons. The following built in comparers are available in the formula language: <ul> <li>`Comparer.Ordinal`: Used to perform an exact ordinal comparison</li> <li>`Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison</li> <li> `Comparer.FromCulture`: Used to perform a culture aware comparison</li> </ul>   
  
  
## Syntax

<pre>
Table.TransformColumnNames(table as table, nameGenerator as function, optional options as nullable record) as table  
</pre>
  
## Example 1  
Remove the #(tab) character from column names  
  
```powerquery-m
Table.TransformColumnNames(Table.FromRecords({[#"Col#(tab)umn" = 1]}), Text.Clean)  
```  
  
|Column|  
|----------|  
|1|  
  
## Example 2  
Transform column names to generate case-insensitive names of length 6.  
  
```powerquery-m
Table.TransformColumnNames(Table.FromRecords({[ColumnNum = 1, cOlumnnum = 2, coLumnNUM = 3]}), Text.Clean, [MaxLength = 6, Comparer = Comparer.OrdinalIgnoreCase])
``` 
  
|Column|cOlum1|coLum2|  
|----------|  
|1|2|3|  
  
  
