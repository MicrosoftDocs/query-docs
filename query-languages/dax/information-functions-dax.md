---
description: "Learn more about: Information functions"
title: "Information functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 10/31/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false
---
# Information functions

DAX information functions look at the cell or row that is provided as an argument and tells you whether the value matches the expected type. For example, the ISERROR function returns TRUE if the value that you reference contains an error.  
  
## In this category  

|Function  |Description  |
|---------|---------|
|[COLUMNSTATISTICS](columnstatistics-function-dax.md)     | Returns a table of statistics regarding every column in every table in the model.         |
|[CONTAINS](contains-function-dax.md)     | Returns true if values for all referred columns exist, or are contained, in those columns; otherwise, the function returns false.         |
|[CONTAINSROW](containsrow-function-dax.md)     | Returns TRUE if a row of values exists or contained in a table, otherwise returns FALSE.          |
|[CONTAINSSTRING](containsstring-function-dax.md)    |  Returns TRUE or FALSE indicating whether one string contains another string.         |
|[CONTAINSSTRINGEXACT](containsstringexact-function-dax.md)     |  Returns TRUE or FALSE indicating whether one string contains another string.       |
|[CUSTOMDATA](customdata-function-dax.md)     | Returns the content of the CustomData property in the connection string.         |
|[HASONEFILTER](hasonefilter-function-dax.md)      |  Returns TRUE when the number of directly filtered values on *columnName* is one; otherwise returns FALSE.        |
|[HASONEVALUE](hasonevalue-function-dax.md)     |  Returns TRUE when the context for *columnName* has been filtered down to one distinct value only. Otherwise is FALSE.        |
|[ISAFTER](isafter-function-dax.md)     | A boolean function that emulates the behavior of a Start At clause and returns true for a row that meets all of the condition parameters.        |
|[ISBLANK](isblank-function-dax.md)     | Checks whether a value is blank, and returns TRUE or FALSE.         |
|[ISCROSSFILTERED](iscrossfiltered-function-dax.md)      |  Returns TRUE when *columnName* or another column in the same or related table is being filtered.         |
|[ISEMPTY](isempty-function-dax.md)     |  Checks if a table is empty.       |
|[ISERROR](iserror-function-dax.md)      |  Checks whether a value is an error, and returns TRUE or FALSE.        |
|[ISEVEN](iseven-function-dax.md)      |  Returns TRUE if number is even, or FALSE if number is odd.       |
|[ISFILTERED](isfiltered-function-dax.md)     |  Returns TRUE when *columnName* is being filtered directly.       |
|[ISINSCOPE](isinscope-function-dax.md)      | Returns true when the specified column is the level in a hierarchy of levels.        |
|[ISLOGICAL](islogical-function-dax.md)     | Checks whether a value is a logical value, (TRUE or FALSE), and returns TRUE or FALSE.          |
|[ISNONTEXT](isnontext-function-dax.md)     | Checks if a value is not text (blank cells are not text), and returns TRUE or FALSE.          |
|[ISNUMBER](isnumber-function-dax.md)      | Checks whether a value is a number, and returns TRUE or FALSE.        |
|[ISODD](isodd-function-dax.md)      | Returns TRUE if number is odd, or FALSE if number is even.        |
|[ISONORAFTER](isonorafter-function-dax.md)     | A boolean function that emulates the behavior of a Start At clause and returns true for a row that meets all of the condition parameters.        |
|[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md)|   Used by expressions for calculation items to determine the measure that is in context is one of those specified in a list of measures.   |
|[ISSUBTOTAL](issubtotal-function-dax.md)       |  Creates another column in a SUMMARIZE expression that returns True if the row contains subtotal values for the column given as argument, otherwise returns False.        |
|[ISTEXT](istext-function-dax.md)     | Checks if a value is text, and returns TRUE or FALSE.          |
|[NONVISUAL](nonvisual-function-dax.md)     |  Marks a value filter in a SUMMARIZECOLUMNS expression as non-visual.       |
|[SELECTEDMEASURE](selectedmeasure-function-dax.md) |   Used by expressions for calculation items to reference the measure that is in context.   |
|[SELECTEDMEASUREFORMATSTRING](selectedmeasureformatstring-function-dax.md) |   Used by expressions for calculation items to retrieve the format string of the measure that is in context.   |
|[SELECTEDMEASURENAME](selectedmeasurename-function-dax.md) |   Used by expressions for calculation items to determine the measure that is in context by name.   |
|[USERCULTURE](userculture-function-dax.md)   |Returns the locale for the current user.    |
|[USERNAME](username-function-dax.md)    |  Returns the domain name and username from the credentials given to the system at connection time.        |
|[USEROBJECTID](userobjectid-function-dax.md)    |  Returns the current user's Object ID or SID.       |
|[USERPRINCIPALNAME](userprincipalname-function-dax.md)    |  Returns the user principal name.       |
