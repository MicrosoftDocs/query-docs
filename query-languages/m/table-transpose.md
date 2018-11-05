---
title: "Table.Transpose | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Transpose

  
## About  
Returns a table with columns converted to rows and rows converted to columns from the input table.  
  
## Syntax

<pre>
Table.Transpose(table as table, optional columns as any) as table  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional columns|Columns to transform.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Table.PromoteHeaders(  
  
    Table.Transpose(  
  
        Table.DemoteHeaders(  
  
            Table.FromRecords({  
  
                [Name = "Full Name", Value = "Fred"],  
  
                [Name = "Age", Value = 42],  
  
                [Name = "Country", Value = "UK"]  
  
            })  
  
        )  
  
    )  
  
)  
```  
  
|Name|FullName|Age|Country|  
|--------|------------|-------|-----------|  
|Value|Fred|42|UK|  
  
