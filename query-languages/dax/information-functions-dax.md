---
title: "Information functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Information functions
DAX information functions look at the cell or row that is provided as an argument and tells you whether the value matches the expected type. For example, the ISERROR function returns TRUE if the value that you reference contains an error.  
  
## In this section  

|Function  |Description  |
|---------|---------|
|[CONTAINS](contains-function-dax.md)     | Returns true if values for all referred columns exist, or are contained, in those columns; otherwise, the function returns false.         |
|[CUSTOMDATA](customdata-function-dax.md)     | Returns the content of the CustomData property in the connection string.         |
|[ISBLANK](isblank-function-dax.md)     | Checks whether a value is blank, and returns TRUE or FALSE.         |
|[ISERROR](iserror-function-dax.md)      |  Checks whether a value is an error, and returns TRUE or FALSE.        |
|[ISEVEN](iseven-function-dax.md)      |  Returns TRUE if number is even, or FALSE if number is odd.       |
|[ISINSCOPE](isinscope-function-dax.md)      | Returns true when the specified column is the level in a hierarchy of levels.        |
|[ISLOGICAL](islogical-function-dax.md)     | Checks whether a value is a logical value, (TRUE or FALSE), and returns TRUE or FALSE.          |
|[ISNONTEXT](isnontext-function-dax.md)     | Checks if a value is not text (blank cells are not text), and returns TRUE or FALSE.          |
|[ISNUMBER](isnumber-function-dax.md)      | Checks whether a value is a number, and returns TRUE or FALSE.        |
|[ISONORAFTER](isonorafter-function-dax.md)     | A boolean function that emulates the behavior of a Start At clause and returns true for a row that meets all of the condition parameters.        |
|[ISTEXT](istext-function-dax.md)     | Checks if a value is text, and returns TRUE or FALSE.          |
|[LOOKUPVALUE](lookupvalue-function-dax.md)    | Returns the value in *result_columnName* for the row that meets all criteria specified by *search_columnName* and *search_value*.         |
|[USERNAME](username-function-dax.md)    |  Returns the domain name and username from the credentials given to the system at connection time.        |