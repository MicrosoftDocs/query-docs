---
description: "Learn more about: Excel.Workbook"
title: "Excel.Workbook"
---
# Excel.Workbook

## Syntax

<pre>
Excel.Workbook(<b>workbook</b> as binary, optional <b>useHeaders</b> as any, optional <b>delayTypes</b> as nullable logical) as table
</pre>

## About

Returns the contents of the Excel workbook.

* `useHeaders` can be null, a logical (true/false) value indicating whether the first row of each returned table should be treated as a header, or an options record. Default: false. This option converts numbers and dates to text using the current culture, and thus behaves differently when run in environments with different operating system cultures set. We recommend using [Table.PromoteHeaders](table-promoteheaders.md) instead.
* `delayTypes` can be null or a logical (true/false) value indicating whether the columns of each returned table should be left untyped. Default: false.

If a record is specified for `useHeaders` (and `delayTypes` is null), the following record fields may be provided:

* `UseHeaders`: Can be null or a logical (true/false) value indicating whether the first row of each returned table should be treated as a header. Default: false. The `useHeaders` option converts numbers and dates to text using the current culture, and thus behaves differently when run in environments with different operating system cultures set. We recommend using [Table.PromoteHeaders](table-promoteheaders.md) instead.
* `DelayTypes`: Can be null or a logical (true/false) value indicating whether the columns of each returned table should be left untyped. Default: false.
* `InferSheetDimensions`: Can be null or a logical (true/false) value indicating whether the area of a worksheet that contains data should be inferred by reading the worksheet itself, rather than by reading the dimensions metadata from the file. This can be useful in cases where the dimensions metadata is incorrect. Note that this option is only supported for Open XML Excel files, not for legacy Excel files. Default: false.

## Example 1

Return the contents of Sheet1 from an Excel workbook.

**Usage**

```powerquery-m
Excel.Workbook(File.Contents("C:\Book1.xlsx"), null, true){[Item="Sheet1"]}[Data]
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = "ID", Column2 = "Name", Column3 = "Phone"],
    [Column1 = 1, Column2 = "Bob", Column3 = "123-4567"],
    [Column1 = 3, Column2 = "Pam", Column3 = "543-7890"],
    [Column1 = 2, Column2 = "Jim", Column3 = "987-6543"]
})
```
