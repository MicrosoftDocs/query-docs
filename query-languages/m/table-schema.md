---
title: "Table.Schema | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3830c166-ced7-4831-8d4e-819e8883b5d3
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Schema
<code>Table.Schema(<b>table</b> as table) as table</code>

## About

<p>Returns a table describing the columns of <code>table</code>.</p> <p>Each row in the table describes the properties of a column of <code>table</code>:</p> <p><table> <tr> <td><b>Column Name</b></td> <td><b>Description</b></td> </tr> <tr> <td><code>Name</code></td> <td>The name of the column.</td> </tr> <tr> <td><code>Position</code></td> <td>The 0-based position of the column in <code>table</code>.</td> </tr> <tr> <td><code>TypeName</code></td> <td>The name of the type of the column.</td> </tr> <tr> <td><code>Kind</code></td> <td>The kind of the type of the column.</td> </tr> <tr> <td><code>IsNullable</code></td> <td>Whether the column can contain <code>null</code> values.</td> </tr> <tr> <td><code>NumericPrecisionBase</code></td> <td>The numeric base (e.g. base-2, base-10) of the <code>NumericPrecision</code> and <code>NumericScale</code> fields.</td> </tr> <tr> <td><code>NumericPrecision</code></td> <td>The precision of a numeric column in the base specified by <code>NumericPrecisionBase</code>. This is the maximum number of digits that can be represented by a value of this type (including fractional digits).</td> </tr> <tr> <td><code>NumericScale</code></td> <td>The scale of a numeric column in the base specified by <code>NumericPrecisionBase</code>. This is the number of digits in the fractional part of a value of this type. A value of <code>0</code> indicates a fixed scale with no fractional digits. A value of <code>null</code> indicates the scale is not known (either because it is floating or not defined).</td> </tr> <tr> <td><code>DateTimePrecision</code></td> <td>The maximum number of fractional digits supported in the seconds portion of a date or time value.</td> </tr> <tr> <td><code>MaxLength</code></td> <td>The maximum number of characters permitted in a <code>text</code> column, or the maximum number of bytes permitted in a <code>binary</code> column.</td> </tr> <tr> <td><code>IsVariableLength</code></td> <td>Indicates whether this column can vary in length (up to <code>MaxLength</code>) or if it is of fixed size.</td> </tr> > <tr> <td><code>NativeTypeName</code></td> <td>The name of the type of the column in the native type system of the source (e.g. <code>nvarchar</code> for SQL Server).</td> </tr> <tr> <td><code>NativeDefaultExpression</code></td> <td>The default expression for a value of this column in the native expression language of the source (e.g. <code>42</code> or <code>newid()</code> for SQL Server).</td> </tr> <tr> <td><code>Description</code></td> <td>The description of the column.</td> </tr> </table></p>

  
