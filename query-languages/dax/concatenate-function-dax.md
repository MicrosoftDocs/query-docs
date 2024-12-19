---
description: "Learn more about: CONCATENATE"
title: "CONCATENATE function (DAX)"
---
# CONCATENATE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Joins two text strings into one text string.

## Syntax

```dax
CONCATENATE(<text1>, <text2>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text1`|The first text string to be joined into a single text string. The string can include text or numbers. You can also use column references.|
|`text2`|The second text string to be joined into a single text string. The string can include text or numbers. You can also use column references.|

## Return value

A concatenated string.

## Remarks

- The CONCATENATE function joins two text strings into one text string. The joined items can be text, numbers, Boolean values represented as text, or a combination of those items. You can also use a column reference if the column contains appropriate values.

- The CONCATENATE function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to concatenate multiple columns, you can create a series of calculations or use the concatenation operator (`&`) to join all of them in a simpler expression.

- If you want to use text strings directly, rather than using a column reference, you must enclose each string in double quotation marks.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example: Concatenation of Literals

The sample formula creates a new string value by combining two string values that you provide as arguments.

```dax
= CONCATENATE("Hello ", "World") 
```

## Example: Concatenation of strings in columns

The sample formula returns the customer's full name as listed in a phone book. Note how a nested function is used as the second argument. This is one way to concatenate multiple strings when you have more than two values that you want to use as arguments.

```dax
= CONCATENATE(Customer[LastName], CONCATENATE(", ", Customer[FirstName]))
```

## Example: Conditional concatenation of strings in columns

The sample formula creates a new calculated column in the Customer table with the full customer name as a combination of first name, middle initial, and last name. If there is no middle name, the last name comes directly after the first name. If there is a middle name, only the first letter of the middle name is used and the initial letter is followed by a period.

```dax
= CONCATENATE( [FirstName]&" ", CONCATENATE( IF( LEN([MiddleName])>1, LEFT([MiddleName],1)&". ", ""), [LastName]))
```

This formula uses nested CONCATENATE and IF functions, together with the ampersand (`&`) operator, to conditionally concatenate three string values and add spaces as separators.

## Example: Concatenation of columns with different data types

The following example demonstrates how to concatenate values in columns that have different data types. If the value that you are concatenating is numeric, the value will be implicitly converted to text. If both values are numeric, both values will be cast to text and concatenated as if they were strings.

|Product description|Product abbreviation (column 1 of composite key)|Product number (column 2 of composite key)|New generated key column|
|-----------------------|----------------------------------------------------|----------------------------------------------|----------------------------|
|Mountain bike|MTN|40|MTN40|
|Mountain bike|MTN|42|MTN42|

```dax
= CONCATENATE('Products'[Product abbreviation],'Products'[Product number])
```

The CONCATENATE function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to add more arguments, you can use the ampersand (&amp;) operator. For example, the following formula produces the results, MTN-40 and MTN-42.

```dax
= [Product abbreviation] & "-" & [Product number]
```

## Related content

[CONCATENATEX](concatenatex-function-dax.md)
