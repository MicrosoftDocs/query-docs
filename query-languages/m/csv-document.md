---
description: "Learn more about: Csv.Document"
title: "Csv.Document"
ms.date: 6/15/2023
---
# Csv.Document

## Syntax

<pre> 
Csv.Document(<b>source</b> as any, optional <b>columns</b> as any, optional <b>delimiter</b> as any, optional <b>extraValues</b> as nullable number, optional <b>encoding</b> as nullable number) as table
</pre>

## About

Returns the contents of the CSV document as a table.

* `columns` can be null, the number of columns, a list of column names, a table type, or an options record.
* `delimiter` can be a single character, a list of characters, or the value `""`, which indicates rows should be split by consecutive whitespace characters. Default: `","`.
* Refer to [ExtraValues.Type](extravalues-type.md) for the supported values of `extraValues`.
* `encoding` specifies the text encoding type.

If a record is specified for `columns` (and `delimiter`, `extraValues`, and `encoding` are null), the following record fields may be provided:

* `Delimiter`: The column delimiter. Default: `","`.
* `Columns`: Can be null, the number of columns, a list of column names, or a table type. If the number of columns is lower than the number found in the input, the additional columns will be ignored. If the number of columns is higher than the number found in the input, the additional columns will be null. When not specified, the number of columns will be determined by what is found in the input.
* `Encoding`: The text encoding of the file. Default: 65001 (UTF-8).
* `CsvStyle`: Specifies how quotes are handled.
  * [CsvStyle.QuoteAfterDelimiter](csvstyle-type.md) (default): Quotes in a field are only significant immediately following the delimiter.
  * [CsvStyle.QuoteAlways](csvstyle-type.md): Quotes in a field are always significant, regardless of where they appear.
* `QuoteStyle`: Specifies how quoted line breaks are handled.
  * [QuoteStyle.Csv](quotestyle-type.md) (default): Quoted line breaks are treated as part of the data, not as the end of the current row.
  * [QuoteStyle.None](quotestyle-type.md): All line breaks are treated as the end of the current row, even when they occur inside a quoted value.

## Example 1

Process CSV text with column headers.

**Usage**

```powerquery-m
let
    csv = Text.Combine({"OrderID,Item", "1,Fishing rod", "2,1 lb. worms"}, "#(cr)#(lf)")
in
    Table.PromoteHeaders(Csv.Document(csv))
```

**Output**

```powerquery-m
Table.FromRecords({
    [OrderID = "1", Item = "Fishing rod"],
    [OrderID = "2", Item = "1 lb. worms"]
```
