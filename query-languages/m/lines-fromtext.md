---
description: "Learn more about: Lines.FromText"
title: "Lines.FromText"
ms.subservice: m-source
ms.topic: reference
---
# Lines.FromText

## Syntax

<pre>
Lines.FromText(
    <b>text</b> as text,
    optional <b>quoteStyle</b> as any,
    optional <b>includeLineSeparators</b> as nullable logical
) as list
</pre>

## About

Converts a text value to a list of text values split at line breaks.

* `text`: The text value to convert to the list of text values.
* `quoteStyle`: Specifies how line breaks are handled. The value of `quoteStyle` can be `null`. The default value is [QuoteStyle.None](quotestyle-type.md).
* `includeLineSeparators`: Specifies whether to include the line break characters in the text. The value of `includeLineSeparators` can be `null`. The default value is `false`.

If a record is specified for `quoteStyle` (and `includeLineSeparators` is `null`), the following record fields can be provided:

* `QuoteStyle`: Specifies how quoted line breaks are handled.
  * [QuoteStyle.Csv](quotestyle-type.md): Quoted line breaks are treated as part of the data, not as the end of the current row.
  * [QuoteStyle.None](quotestyle-type.md): All line breaks are treated as the end of the current row, even when they occur inside a quoted value. This value is the default if the `CsvStyle` option isn't specified.
* `CsvStyle`: Specifies how quotes are handled. Should not be used with `QuoteStyle.None`.
  * [CsvStyle.QuoteAfterDelimiter](csvstyle-type.md): Quotes in a field are only significant immediately following the `Delimiter`.
  * [CsvStyle.QuoteAlways](csvstyle-type.md): Quotes in a field are always significant, regardless of where they appear.
* `Delimiter`: A single character delimiter. Should be used only with `CsvStyle.QuoteAfterDelimiter`.
* `IncludeLineSeparators`: Specifies whether to include the line break characters in the text. The default value is `false`.
