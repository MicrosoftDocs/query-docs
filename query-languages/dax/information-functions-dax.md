---
description: "Learn more about: Information functions"
title: "Information functions (DAX)"
ms.topic: concept-article
---
# Information functions

DAX information functions look at the cell or row that is provided as an argument and tells you whether the value matches the expected type. For example, the ISERROR function returns `TRUE` if the value that you reference contains an error.

## In this category

|Function  |Description  |
|---------|---------|
|[COLUMNSTATISTICS](columnstatistics-function-dax.md)     | Returns a table of statistics regarding every column in every table in the model.         |
|[CONTAINS](contains-function-dax.md)     | Returns true if values for all referred columns exist, or are contained, in those columns; otherwise, the function returns false.         |
|[CONTAINSROW](containsrow-function-dax.md)     | Returns `TRUE` if a row of values exists or contained in a table, otherwise returns `FALSE`.          |
|[CONTAINSSTRING](containsstring-function-dax.md)    |  Returns `TRUE` or `FALSE` indicating whether one string contains another string.         |
|[CONTAINSSTRINGEXACT](containsstringexact-function-dax.md)     |  Returns `TRUE` or `FALSE` indicating whether one string contains another string.       |
|[CUSTOMDATA](customdata-function-dax.md)     | Returns the content of the CustomData property in the connection string.         |
|[HASONEFILTER](hasonefilter-function-dax.md)      |  Returns TRUE when the number of directly filtered values on `columnName` is one; otherwise returns `FALSE`.        |
|[HASONEVALUE](hasonevalue-function-dax.md)     |  Returns `TRUE` when the context for `columnName` has been filtered down to one distinct value only. Otherwise is `FALSE`.        |
|[ISAFTER](isafter-function-dax.md)     | A boolean function that emulates the behavior of a Start At clause and returns true for a row that meets all of the condition parameters.        |
|[ISBLANK](isblank-function-dax.md)     | Checks whether a value is blank, and returns `TRUE` or `FALSE`.         |
|[ISBOOLEAN](isboolean-function-dax.md) | Checks whether a value is a logical value, (`TRUE` or `FALSE`), and returns `TRUE` or `FALSE`. Alias of [ISLOGICAL](islogical-function-dax.md). |
|[ISCROSSFILTERED](iscrossfiltered-function-dax.md)      |  Returns `TRUE` when `columnName` or another column in the same or related table is being filtered.         |
|[ISCURRENCY](iscurrency-function-dax.md)|Checks whether a value is a decimal number, and returns `TRUE` or `FALSE`. Alias of [ISDECIMAL](isdecimal-function-dax.md).|
|[ISDATETIME](isdatetime-function-dax.md)|Checks whether a value is a date / time, and returns `TRUE` or `FALSE`.|
|[ISDECIMAL](isdecimal-function-dax.md)|Checks whether a value is a decimal number, and returns `TRUE` or `FALSE`. Alias of [ISCURRENCY](iscurrency-function-dax.md).|
|[ISDOUBLE](isdouble-function-dax.md)|Checks whether a value is a floating-point number, and returns `TRUE` or `FALSE`.|
|[ISEMPTY](isempty-function-dax.md)     |  Checks if a table is empty.       |
|[ISERROR](iserror-function-dax.md)      |  Checks whether a value is an error, and returns `TRUE` or `FALSE`.        |
|[ISEVEN](iseven-function-dax.md)      |  Returns `TRUE` if number is even, or `FALSE` if number is odd.       |
|[ISFILTERED](isfiltered-function-dax.md)     |  Returns `TRUE` when `columnName` is being filtered directly.       |
|[ISINSCOPE](isinscope-function-dax.md)      | Returns true when the specified column is the level in a hierarchy of levels.        |
|[ISINT64](isint64-function-dax.md)|Checks whether a value is a whole number, and returns `TRUE` or `FALSE`. Alias of [ISINTEGER](isinteger-function-dax.md).|
|[ISINTEGER](isinteger-function-dax.md)|Checks whether a value is a whole number, and returns `TRUE` or `FALSE`. Alias of [ISINT64](isint64-function-dax.md).|
|[ISLOGICAL](islogical-function-dax.md)     | Checks whether a value is a logical value, (`TRUE` or `FALSE`), and returns `TRUE` or `FALSE`. Alias of [ISBOOLEAN](isboolean-function-dax.md).|
|[ISNONTEXT](isnontext-function-dax.md)     | Checks if a value is not text (blank cells are not text), and returns `TRUE` or `FALSE`.          |
|[ISNUMBER](isnumber-function-dax.md)      | Checks whether a value is a number, and returns `TRUE` or `FALSE`. Alias of [ISNUMERIC](isnumeric-function-dax.md).|
|[ISNUMERIC](isnumeric-function-dax.md)      | Checks whether a value is a number, and returns `TRUE` or `FALSE`. Alias of [ISNUMBER](isnumber-function-dax.md).|
|[ISODD](isodd-function-dax.md)      | Returns `TRUE` if number is odd, or `FALSE` if number is even.        |
|[ISONORAFTER](isonorafter-function-dax.md)     | A boolean function that emulates the behavior of a Start At clause and returns true for a row that meets all of the condition parameters.        |
|[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md)|   Used by expressions for calculation items to determine the measure that is in context is one of those specified in a list of measures.   |
|[ISSTRING](isstring-function-dax.md)     | Checks if a value is text, and returns `TRUE` or `FALSE`. Alias of [ISTEXT](istext-function-dax.md).
|[ISSUBTOTAL](issubtotal-function-dax.md)       |  Creates another column in a SUMMARIZE expression that returns True if the row contains subtotal values for the column given as argument, otherwise returns False.        |
|[ISTEXT](istext-function-dax.md)     | Checks if a value is text, and returns `TRUE` or `FALSE`. Alias of [ISSTRING](isstring-function-dax.md).|
|[NONVISUAL](nonvisual-function-dax.md)     |  Marks a value filter in a SUMMARIZECOLUMNS expression as non-visual.       |
|[SELECTEDMEASURE](selectedmeasure-function-dax.md) |   Used by expressions for calculation items to reference the measure that is in context.   |
|[SELECTEDMEASUREFORMATSTRING](selectedmeasureformatstring-function-dax.md) |   Used by expressions for calculation items to retrieve the format string of the measure that is in context.   |
|[SELECTEDMEASURENAME](selectedmeasurename-function-dax.md) |   Used by expressions for calculation items to determine the measure that is in context by name.   |
|[USERCULTURE](userculture-function-dax.md)   |Returns the locale for the current user.    |
|[USERNAME](username-function-dax.md)    |  Returns the domain name and username from the credentials given to the system at connection time.        |
|[USEROBJECTID](userobjectid-function-dax.md)    |  Returns the current user's Object ID or SID.       |
|[USERPRINCIPALNAME](userprincipalname-function-dax.md)    |  Returns the user principal name.       |
