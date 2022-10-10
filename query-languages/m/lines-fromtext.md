---
description: "Learn more about: Lines.FromText"
title: "Lines.FromText"
ms.date: 10/7/2022
---
# Lines.FromText

## Syntax

<pre>
Lines.FromText(<b>text</b> as text, optional <b>quoteStyle</b> as nullable number, optional <b>includeLineSeparators</b> as nullable logical) as list
</pre>

## About

Converts a text value to a list of text values split at lines breaks. If `includeLineSeparators` is true, then the line break characters are included in the text.

* `QuoteStyle.None`: (default) No quoting behavior is needed.
* `QuoteStyle.Csv`: Quoting is as per Csv. A double quote character is used to demarcate such regions, and a pair of double quote characters is used to indicate a single double quote character within such a region.
