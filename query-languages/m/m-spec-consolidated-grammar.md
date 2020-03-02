---
title: M Language Consolidated Grammar | Microsoft Docs
description: Use the "create from blank" option to create a custom connector for Power Automate and Power Apps
author: dougklopfenstein

ms.service: powerquery

ms.topic: article
ms.date: 02/28/2020
ms.author: v-douklo
---

## Consolidated Grammar

## Lexical grammar

<em>lexical-unit:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>lexical-elements<sub>opt</sub></em><br/>
<em>lexical-elements: lexical-element</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>lexical-element  lexical-elements</em><br/>
<em>lexical-element:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>whitespace</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>token comment</em>

### White space

<em>whitespace:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character with Unicode class Zs<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Horizontal tab character (`U+0009`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vertical tab character (`U+000B`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form feed character (`U+000C`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`) followed by line feed character (`U+000A`)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>new-line-character</em><br/>
<em>new-line-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line feed character (`U+000A`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next line character (`U+0085`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line separator character (`U+2028`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paragraph separator character (`U+2029`)

### Comment

<em>comment:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>single-line-comment delimited-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>comment</em><br/> 
<em>single-line-comment:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`//`  <em>single-line-comment-characters<sub>opt</sub> single-line-comment-</em><br/>
<em>characters: single-line-comment-character single-line-comment-</em><br/>
<em>characters  single-line-comment-character</em><br/> 
<em>single-line-comment-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except a <em>new-line-character</em><br/>
<em>delimited-comment:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/*` <em>delimited-comment-text<sub>opt</sub>  asterisks</em>  `/` <em>delimited-comment-text:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>delimited-comment-section delimited-comment-text</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>delimited-comment-section</em><br/>
<em>delimited-comment-section:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>asterisks<sub>opt</sub>  not-slash-or-asterisk</em><br/> 
<em>asterisks:</em> `*`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>asterisks</em>  `*`<br/> 
<em>not-slash-or-asterisk:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except `*` or `/`

### Tokens

<em>token: identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>operator-or-punctuator</em>

### Character escape sequences

<em>character-escape-sequence:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#`(  <em>escape-sequence-list</em>  )<br/>
<em>escape-sequence-list:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>single-escape-sequence escape-sequence-list  ,</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>single-escape-sequence</em><br/>
<em>single-escape-sequence:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>long-unicode-escape-sequence short-unicode-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>escape-sequence control-character-escape-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>sequence escape-escape</em><br/>
<em>long-unicode-escape-sequence: hex-digit  hex-digit  hex-digit  hex-digit  hex-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digit  hex-digit  hex-digit</em><br/>
<em>short-unicode-escape-sequence: hex-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digit  hex-digit  hex-digit</em><br/>
<em>control-character-escape-sequence:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>control-character</em><br/>
<em>control-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cr` `lf` `tab`<br/>
<em>escape-escape:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#`

### Literals

<em>literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>number-literal  text-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal null-literal</em><br/>
<em>number-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-number-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hexadecimal-number-literal</em><br/>
<em>decimal-digits: decimal-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-digit  decimal-digits</em><br/>
<em>decimal-digit:</em>  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9`<br/>
<em>hexadecimal-number-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0x`  <em>hex-digits</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0X`  <em>hex-digits hex-</em><br/>
<em>digits: hex-digit hex-</em><br/>
<em>digit  hex-digits</em><br/>
<em>hex-digit:</em>  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  a  b  c  d e  f`<br/>
<em>decimal-number-literal:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-digits  .  decimal-digits  exponent-part<sub>opt</sub></em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>.  decimal-digits  exponent-part<sub>opt</sub> decimal-digits</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>exponent-part    decimal-digits</em><br/>
<em>exponent-part:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`e`  <em>sign<sub>opt</sub>  decimal-digits</em> `E`<br/>
<em>sign<sub>opt</sub>  decimal-digits sign:</em>  one of<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+  -` <em>text-literal:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"`  <em>text-literal-characters<sub>opt</sub></em>  `"`<br/>
<em>text-literal-characters: text-literal-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>text-literal-character  text-literal-characters</em><br/>
<em>text-literal-character: single-text-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character character-escape-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>sequence  double-quote-escape-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>sequence</em><br/>
<em>single-text-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`)<br/>
<em>double-quote-escape-sequence:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`""` (`U+0022`, `U+0022`)<br/>
<em>null-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`null`

### Identifiers

<em>identifier:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>regular-identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>quoted-identifier</em><br/>
<em>regular-identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>available-identifier available-identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>dot-character  regular-identifier</em><br/>
<em>available-identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <em>keyword-or-identifier</em> that is not a <em>keyword</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword-or-identifier: letter-character underscore-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character identifier-start-character  identifier-part-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>characters</em><br/>
<em>identifier-start-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>letter-character underscore-character</em><br/>
<em>identifier-part-characters: identifier-part-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>identifier-part-character  identifier-part-characters</em><br/>
<em>identifier-part-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>letter-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-digit-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>underscore-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>connecting-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>combining-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>formatting-character</em><br/> <em>generalized-identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-part generalized-identifier</em> separated only by blanks (`U+0020`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-part</em><br/>
<em>generalized-identifier-part:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-segment decimal-digit-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-segment</em><br/>
<em>generalized-identifier-segment:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword-or-identifier keyword-or-identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>dot-character  keyword-or-identifier</em><br/>
<em>dot-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  (`U+002E`) underscore-</em><br/>
<em>character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`_`  (`U+005F`) letter-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nl <em>combining-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Mn or Mc  <em>decimal-digit-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Nd  <em>connecting-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Pc <em>formatting-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Cf <em>quoted-identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#"`  <em>text-literal-charactersopt</em>  `"`

### Keywords and predefined identifiers

Predefined identifiers and keywords cannot be redefined. A quoted identifier can be used to handle identifiers that would otherwise collide with predefined identifiers or keywords.

<em>keyword:</em>  one of</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`and as each else error false if in is let meta not otherwise or section`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`shared then true try type #binary #date #datetime #datetimezone #duration`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#infinity #nan #sections #shared #table #time`

### Operators and punctuators 

<em>operator-or-punctuator:</em>  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`, ; = < <= > >= <> + - * / & ( ) [ ] { } @ ? => .. ...`

## Syntactic grammar

### Documents

<em>document:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>section-document expression-document</em>

### Section Documents

<em>section-document: section</em><br/>
<em>section: literal-attributes<sub>opt</sub></em>  `section`  <em>section-name<sub>opt</sub>  ;  section-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>members<sub>opt</sub></em><br/>
<em>section-name: identifier</em><br/>
<em>section-members: section-member</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>section-member  section-members</em><br/>
<em>section-member:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal-attributes<sub>opt</sub>  shared<sub>opt</sub>  section-member-name  =  expression  ;</em><br/>
<em>section-member-name: identifier</em>

### Expression Documents

#### Expressions

<em>expression-document: expression</em><br/>
<em>expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>logical-or-expression</em></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;each-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>function-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>let-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>if-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>error-raising-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>error-handling-expression</em>

#### Logical expressions

<em>logical-or-expression: logical-and-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>logical-and-expression</em>  `or`  <em>logical-or-expression</em><br/>
<em>logical-and-expression: is-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>logical-and-expression</em>  `and`  <em>is-expression</em>

#### Is expression

<em>is-expression: as-expression is-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`is`  <em>nullable-primitive-type</em><br/>
<em>nullable-primitive-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nullable`<sub>opt</sub>  <em>primitive-type</em>

#### As expression

<em>as-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>equality-expression as-expression</em>  `as`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>nullable-primitive-type</em>

#### Equality expression

<em>equality-expression: relational-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>relational-expression</em>  `=`  <em>equality-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>relational-expression</em>  `<>`  <em>equality-expression</em>

#### Relational expression

<em>relational-expression: additive-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>additive-expression</em>  `<`  <em>relational-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>additive-expression</em>  `>`  <em>relational-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>additive-expression</em>  `<=`  <em>relational-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>additive-expression</em>  `>=`  <em>relational-expression</em>

#### Arithmetic expressions

<em>additive-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>multiplicative-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>multiplicative-expression</em>  `+`  <em>additive-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>multiplicative-expression</em>  `-`  <em>additive-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>multiplicative-expression</em>  `&`  <em>additive-expression</em><br/>
<em>multiplicative-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>metadata-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>metadata-expression</em>  `*`  <em>multiplicative-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>metadata-expression</em>  `/`  <em>multiplicative-expression</em>

#### Metadata expression

<em>metadata-expression: unary-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>unary-expression</em>  `meta`  <em>unary-expression</em>

#### Unary expression

<em>unary-expression: type-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em> `+`  <em>unary-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em> `-`  <em>unary-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em> `not`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>unary-expression</em>

#### Primary expression

<em>primary-expression:  literal-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression  list-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>record-expression identifier-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression section-access-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression parenthesized-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression field-access-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression  item-access-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression invoke-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>not-implemented-expression</em>

#### Literal expression

_literal-expression: literal_

#### Identifier expression

<em>identifier-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>identifier-reference</em><br/>
<em>identifier-reference:</em><br/>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>exclusive-identifier-reference</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>inclusive-identifier-reference</em><br/> 
<em>exclusive-identifier-reference:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>identifier</em><br/>
<em>inclusive-identifier-reference:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`@`  <em>identifier</em>

#### Section-access expression

<em>section-access-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>identifier</em> `!` <em>identifier</em>

#### Parenthesized expression

<em>parenthesized-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  <em>expression</em>  `)`

#### Not-implemented expression

<em>not-implemented-expression:</em> `...`

#### Invoke expression

<em>invoke-expression: primary-expression</em>  `(`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>argument-listopt</em>  `)`<br/>
<em>argument-list: expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression  ,   argument-list</em>

#### List expression

<em>list-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{`  <em>item-list<sub>opt</sub></em>  `}`<br/>
<em>item-list: item item</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>,  item-list</em><br/>
<em>item:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression expression</em>  `..`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em>

#### Record expression

<em>record-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`  <em>field-list<sub>opt<sub></em>  `]`<br/>
<em>field-list: field field</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>,  field-list</em><br/>
<em>field:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>field-name</em>  `=`  <em>expression</em><br/>
<em>field-name:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier</em>

#### Item access expression

<em>item-access-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>item-selection</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-item-selection</em><br/>
<em>item-selection:</em></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-expression</em>  `{`  <em>item-selector</em>  `}`<br/>
<em>optional-item-selection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-expression</em>  `{`  <em>item-selector</em>  `} ?`

#### Field access expressions

<em>field-access-expression:  field-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>selection implicit-target-field-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>selection projection implicit-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>target-projection</em><br/>
<em>field-selection: primary-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>field-selector</em><br/>
<em>field-selector:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>required-field-selector</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-field-selector</em><br/>
<em>required-field-selector:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   <em>field-name</em>  `]`</em><br/>
<em>optional-field-selector:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   <em>field-name</em>  `] ?`<br/>
<em>field-name: generalized-identifier</em><br/>
<em>implicit-target-field-selection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>field-selector</em><br/>
<em>projection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-expression  required-projection</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-expression  optional-projection</em><br/>
<em>required-projection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` <em>required-selector-list</em> `]`<br/>
<em>optional-projection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` <em>required-selector-list</em> `] ?`<br/>
<em>required-selector-list: required-field-selector</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>required-field-selector ,  required-selector-list</em><br/>
<em>implicit-target-projection:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>projection</em>

#### Function expression

<em>function-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  <em>parameter-list<sub>opt</sub></em>  `)`  <em>return-type<sub>opt</sub></em>  `=>`  <em>function-body</em><br/>
<em>function-body:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>parameter-list:</em>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>fixed-parameter-list fixed-parameter-list  ,</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-parameter-list optional-parameter-list</em><br/>
<em>fixed-parameter-list: parameter</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>parameter  ,  fixed-parameter-list</em><br/>
<em>parameter: parameter-name</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>parameter-type<sub>opt</sub></em><br/>
<em>parameter-name: identifier</em><br/>
<em>parameter-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>assertion</em><br/>
<em>return-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>assertion</em><br/>
<em>assertion:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`as`  <em>type</em><br/>
<em>optional-parameter-list: optional-parameter</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-parameter  ,  optional-parameter-list</em><br/>
<em>optional-parameter:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional`  <em>parameter</em>

#### Each expression

<em>each-expression:</em> `each` <em>each-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression-body</em><br/>
<em>each-expression-body: function-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>body</em>

#### Let expression

<em>let-expression:</em> `let`  <em>variable-list</em>  `in`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>variable-list: variable</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>variable  ,  variable-list</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>variable: variable-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>name  =  expression</em><br/>
<em>variable-name: identifier</em>

#### If expression

<em>if-expression:</em> `if` <em>if-condition</em>  `then`  <em>true-expression</em>  `else`  </em>false-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>if-condition:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/> 
<em>true-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>false-expression: expression</em>

#### Type expression

<em>type-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-expression</em> `type`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-type</em><br/>
<em>type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>parenthesized-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primary-type</em><br/>
<em>primary-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>primitive-type</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>record-type</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>list-type</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>function-type table-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>type nullable-type</em><br/>
<em>primitive-type:</em> one of `any anynonnull binary date datetime datetimezone`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`duration function list logical none null number record table text`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`type`<br/> 
<em>record-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`  <em>open-record-marker</em>  `]`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   <em>field-specification-list</em>  `]`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   <em>field-specification-list  ,  open-record-marker</em>  `]` <em>field-specification-list:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>field-specification field-specification
  ,</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>field-specification-list</em><br/>
<em>field-specification:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional`<em><sub>opt</sub> identifier field-type-specification<sub>opt</sub></em><br/> 
<em>field-type-specification:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`=` <em>field-type  field-</em><br/>
<em>type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>type</em><br/>
<em>open-record-marker:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`...`<br/>
<em>list-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{`   <em>item-type</em>   `}` <em>item-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>type</em><br/> 
<em>function-type:</em> `function (`  <em>parameter-specification-listopt</em>  `)`</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>return-type</em><br/>
<em>parameter-specification-list:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>required-parameter-specification-list required-parameter-specification-list  ,</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-parameter-specification-list optional-parameter-specification-list</em><br/>
<em>required-parameter-specification-list: required-parameter-specification</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>required-parameter-specification  ,  required-parameter-specification-list</em><br/>
<em>required-parameter-specification:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>parameter-specification</em><br/>
<em>optional-parameter-specification-list: optional-parameter-specification</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>optional-parameter-specification  ,  optional-parameter-specification-list</em><br/>
<em>optional-parameter-specification:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional` <em>parameter-specification</em><br/> 
<em>parameter-specification: parameter-name</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>parameter-type</em><br/>
<em>table-type:</em> `table`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>row-type</em><br/>
<em>row-type:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   <em>field-specification-list</em>  `]`<br/>
<em>nullable-type:</em> `nullable`  <em>type</em>

#### Error raising expression

<em>error-raising-expression:</em> `error`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em>

#### Error handling expression

<em>error-handling-expression:</em> `try` protected-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression otherwise-clause<sub>opt</sub></em><br/>
<em>protected-expression:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>otherwise-clause:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`otherwise` <em>default-expression</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>default-expression: expression</em>

###  Literal Attributes

<em>literal-attributes:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>record-literal</em><br/>
<em>record-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` <em>literal-field-listopt</em> `]` <em>literal-</em><br/>
<em>field-list: literal-field literal-field</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>, literal-field-list</em><br/>
<em>literal-field: field-name</em> `=`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>any-literal</em><br/>
<em>list-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{` <em>literal-item-list<sub>opt</sub></em> `}` <em>literal-</em><br/>
<em>item-list: any-literal , literal-</em><br/>
<em>item-list</em><br/>
<em>any-literal: record-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>list-literal logical-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal number-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>text-literal null-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal</em>

