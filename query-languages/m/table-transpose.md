---
title: "Table.Transpose | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6ce7cfac-6720-45bd-a59e-9443932cd8ed
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Transpose

  
## About  
Returns a table with columns converted to rows and rows converted to columns from the input table.  
  
```  
Table.Transpose(table as table, optional columns as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional columns|Columns to transform.|  
  
## <a name="__goback"></a>Example  
  
```  
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
  
