---
title: "DATATABLE Function | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
applies_to: 
  - "Power BI"
  - "SQL Server 2016 Preview"
ms.assetid: bd72f357-7f86-41ac-ac0a-d783c4af7567
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DATATABLE Function
Provides a mechanism for declaring an inline set of data values.  
  
## Syntax  
  
```  
DATATABLE (ColumnName1, DataType1, ColumnName2, DataType2..., {{Value1, Value2...}, {ValueN, ValueN+1...}...})  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|ColumnName|Any DAX expression that returns a table.|  
|DataType|An enumeration that includes: INTEGER, DOUBLE, STRING, BOOLEAN, CURRENCY, DATETIME|  
|Value|A single argument using Excel syntax for a one dimensional array constant, nested to provide an array of arrays.  This argument represents the set of data values that will be in the table<br /><br />For example,<br />{ {values in row1}, {values in row2}, {values in row3}, etc. }<br />Where {values in row1} is a comma delimited set of constant expressions, namely a combination of constants, combined with a handful of basic functions including DATE, TIME, and BLANK, as well as a plus operator between DATE and TIME and a unary minus operator so that negative values can be expressed.<br /><br />The following are all valid values: 3, -5, BLANK(), DATE(2009,4,15)+TIME(2,45,21)  Values may not refer to anything outside the immediate expression, and cannot refer to columns, tables, relationships, or anything else.<br /><br />A missing value will be treated identically to BLANK().  For example, the following are the same:   {1,2,BLANK(),4}  {1,2,,4}|  
  
## Return Value  
A table declaring an inline set of values.  
  
## Example  
  
```  
=DataTable("Name", STRING,  
               "Region", STRING  
               ,{  
                        {" User1","East"},  
                        {" User2","East"},  
                        {" User3","West"},  
                        {" User4","West"},  
                        {" User4","East"}  
                }  
           )  
```  
