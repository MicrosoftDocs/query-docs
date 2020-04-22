---
title: "Csv.Document | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Csv.Document

## Syntax

<pre> 
Csv.Document(<b>source</b> as any, optional <b>columns</b> as any, optional <b>delimiter</b> as any, optional <b>extraValues</b> as nullable number, optional <b>encoding</b> as nullable number) as table
</pre>

## About

Returns the contents of the CSV document as a table. <ul> <li> `columns` can be null, the number of columns, a list of column names, a table type, or an options record. (See below for more details on the options record.)</li> <li> `delimiter` can be a single character, or a list of characters. Default: `","`.</li> <li> Please refer to `ExtraValues.Type` for the supported values of `extraValues`.</li> <li> `encoding` specifies the text encoding type.</li> </ul> 

If a record is specified for `columns` (and `delimiter`, `extraValues`, and `encoding` are null), the following record fields may be provided: <ul> <li> `Delimiter`: The column delimiter. Default: `","`.</li> <li> `Columns`: Can be null, the number of columns, a list of column names, or a table type. If the number of columns is lower than the number found in the input, the additional columns will be ignored. If the number of columns is higher than the number found in the input, the additional columns will be null. When not specified, the number of columns will be determined by what is found in the input.</li> <li> `Encoding`: The text encoding of the file. Default: 65001 (UTF-8).</li> <li> `CsvStyle`: Specifies how quotes are handled. `CsvStyle.QuoteAfterDelimiter` (default): Quotes in a field are only significant immediately following the delimiter. `CsvStyle.QuoteAlways`: Quotes in a field are always significant, regardless of where they appear.</li> <li> `QuoteStyle`: Specifies how quoted line breaks are handled. `QuoteStyle.None` (default): All line breaks are treated as the end of the current row, even when they occur inside a quoted value. `QuoteStyle.Csv`: Quoted line breaks are treated as part of the data, not as the end of the current row.</li> </ul> 

## Example 1
Process CSV text with column headers.

```powerquery-m
let 
    csv = Text.Combine({"OrderID,Item", "1,Fishing rod", "2,1 lb. worms"}, "#(cr)#(lf)") 
in 
    Table.PromoteHeaders(Csv.Document(csv))
```

|OrderID  |Item |
|---------|---------|
|1     |    Fishing rod     |
|2     |     1 lb. worms    |
