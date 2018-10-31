---
title: "Table.Schema | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Schema
`Table.Schema(<b>table</b> as table) as table`

## About

<p>Returns a table describing the columns of `table`.</p> <p>Each row in the table describes the properties of a column of `table`:</p> <p><table> <tr> <td><b>Column Name</b></td> <td><b>Description</b></td> </tr> <tr> <td>`Name`</td> <td>The name of the column.</td> </tr> <tr> <td>`Position`</td> <td>The 0-based position of the column in `table`.</td> </tr> <tr> <td>`TypeName`</td> <td>The name of the type of the column.</td> </tr> <tr> <td>`Kind`</td> <td>The kind of the type of the column.</td> </tr> <tr> <td>`IsNullable`</td> <td>Whether the column can contain `null` values.</td> </tr> <tr> <td>`NumericPrecisionBase`</td> <td>The numeric base (e.g. base-2, base-10) of the `NumericPrecision` and `NumericScale` fields.</td> </tr> <tr> <td>`NumericPrecision`</td> <td>The precision of a numeric column in the base specified by `NumericPrecisionBase`. This is the maximum number of digits that can be represented by a value of this type (including fractional digits).</td> </tr> <tr> <td>`NumericScale`</td> <td>The scale of a numeric column in the base specified by `NumericPrecisionBase`. This is the number of digits in the fractional part of a value of this type. A value of `0` indicates a fixed scale with no fractional digits. A value of `null` indicates the scale is not known (either because it is floating or not defined).</td> </tr> <tr> <td>`DateTimePrecision`</td> <td>The maximum number of fractional digits supported in the seconds portion of a date or time value.</td> </tr> <tr> <td>`MaxLength`</td> <td>The maximum number of characters permitted in a `text` column, or the maximum number of bytes permitted in a `binary` column.</td> </tr> <tr> <td>`IsVariableLength`</td> <td>Indicates whether this column can vary in length (up to `MaxLength`) or if it is of fixed size.</td> </tr> > <tr> <td>`NativeTypeName`</td> <td>The name of the type of the column in the native type system of the source (e.g. `nvarchar` for SQL Server).</td> </tr> <tr> <td>`NativeDefaultExpression`</td> <td>The default expression for a value of this column in the native expression language of the source (e.g. `42` or `newid()` for SQL Server).</td> </tr> <tr> <td>`Description`</td> <td>The description of the column.</td> </tr> </table></p>

  
