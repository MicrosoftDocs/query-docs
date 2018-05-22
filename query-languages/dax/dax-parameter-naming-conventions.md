---
title: "DAX Parameter-Naming Conventions | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DAX Parameter-Naming Conventions
Parameter names are standardized in DAX reference to facilitate the usage and understanding of the functions.  
  
## Parameter Names  
  
|Paramter|Description|  
|-|-|  
|expression|Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).|  
|value|Any DAX expression that returns a single scalar value where the expression is to be evaluated exactly once before all other operations.|  
|table|Any DAX expression that returns a table of data.|  
|tableName|The name of an existing table using standard DAX syntax. It cannot be an expression.|  
|columnName|The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression.|  
|name|A string constant that will be used to provide the name of a new object.|  
|order|An enumeration used to determine the sort order.|  
|ties|An enumeration used to determine the handling of tie values.|  
|type|An enumeration used to determine the data type for PathItem and PathItemReverse.|  
  
### Prefixing parameter names or using the prefix only  
  
|Paramter|Description|  
|-|-|  
|prefixing|Parameter names may be further qualified with a prefix that is descriptive of how the argument is used and to avoid ambiguous reading of the parameters. For example:<br /><br />Result_ColumnName -  Refers to an existing column used to get the result values in the LOOKUPVALUE() function.<br /><br />Search_ColumnName - Refers to an existing column used to search for a value in the LOOKUPVALUE() function.|  
|omitting|Parameter names will be omitted if the prefix is clear enough to describe the parameter.<br /><br />For example, instead of having the following syntax DATE (Year_Value, Month_Value, Day_Value) it is clearer for the user to read DATE (Year, Month, Day); repeating three times the suffix value does not add anything to a better comprehension of the function and it clutters the reading unnecessarily.<br /><br />However, if the prefixed parameter is Year_columnName then the parameter name and the prefix will stay to make sure the user understands that the parameter requires a reference to an existing column of Years.|  
  
