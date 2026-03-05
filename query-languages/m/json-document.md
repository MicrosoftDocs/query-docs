---
description: "Learn more about: Json.Document"
title: "Json.Document"
ms.subservice: m-source
ms.topic: reference
---
# Json.Document

## Syntax

<pre>
Json.Document(<b>jsonText</b> as any, optional <b>encoding</b> as nullable number) as any
</pre>

## About

Returns the content of the JSON document.

* `jsonText`: The content of the JSON document. The value of this parameter can be text or a binary value returned by a function like [File.Content](file-contents.md).
* `encoding`: A [TextEncoding.Type](textencoding-type.md) that specifies the encoding used in the JSON document. If `encoding` is omitted, UTF8 is used.

## Example 1

Returns the content of the specified JSON text as a record.

**Usage**

```powerquery-m
let
    Source = "{
        ""project"": ""Contosoware"",
        ""description"": ""A comprehensive initiative aimed at enhancing digital presence."",
        ""components"": [
            ""Website Development"",
            ""CRM Implementation"",
            ""Mobile Application""
        ]
    }",
    jsonDocument = Json.Document(Source)
in
    jsonDocument
```

**Output**

```powerquery-m
[
    project = "Contosoware",
    description = "A comprehensive initiative aimed at enhancing digital presence."
    components =
    {
        "Website Development",
        "CRM Implementation",
        "Mobile Application"
    }
]
```

## Example 2

Returns the content of a local JSON file.

**Usage**

```powerquery-m
let
    Source = (Json.Document(
        File.Contents("C:\test-examples\JSON\Contosoware.json")
    )
in
    Source
```

**Output**

A record, list, or primitive value representing the JSON data contained in the file

## Example 3

Returns the content of an online UTF16 encoded JSON file.

**Usage**

```powerquery-m
let
    Source = Json.Document(
        Web.Contents("htts://contoso.com/products/Contosoware.json"),
        TextEncoding.Utf16)
    )
```

**Output**

A record, list, or primitive value representing the JSON UTF16 data contained in the file
