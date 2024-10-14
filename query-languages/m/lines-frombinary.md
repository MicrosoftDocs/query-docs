---
description: "Learn more about: Lines.FromBinary"
title: "Lines.FromBinary"
---
# Lines.FromBinary

## Syntax

<pre>
Lines.FromBinary(<b>binary</b> as binary, optional <b>quoteStyle</b> as any, optional <b>includeLineSeparators</b> as nullable logical, optional <b>encoding</b> as nullable number) as list
</pre>

## About

Converts a binary value to a list of text values split at lines breaks. If a quote style is specified, then line breaks may appear within quotes. If includeLineSeparators is true, then the line break characters are included in the text.
