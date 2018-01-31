---
title: "Table.ReplaceValue | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dafb3e1c-0865-4f8a-9dac-6394dded9cbf
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ReplaceValue

  
## About  
Replaces oldValue with newValue in specific columns of a table, using the provided replacer function, such as text.Replace or Value.Replace.  
  
```  
Table.ReplaceValue(table as table, oldValue as any, newValue as any,replacer as function, columnsToSearch as {Text}) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|oldValue|The old value to modify.|  
|newValue|The new value to replace with.|  
|replacer|The replacer function to use, such as Text.Replace or Value.Replace.|  
|columnsToSearch|The list of columns to search through.|  
  
## Examples  
  
```  
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
  
