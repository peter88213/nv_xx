novelibre [${Home page}](https://github.com/peter88213/novelibre) > [Index](../) > [${Online help}](./) > ${Export} menu

---

# ${Export} menu

**File export**

## ${Manuscript for editing}

**Export an ODT document that can be imported again after editing**

With **${Export} > ${Manuscript for editing}**, you can create a text
document that is split into sections (to be seen in the Navigator). File
name suffix is `_manuscript_tmp`.

-   Only "${Normal}" chapters and sections are exported. Chapters and
    sections marked "${Unused}" are not exported.

-   Section titles are invisible, but appear in the *Navigator*.

-   Chapters and sections can neither be rearranged nor deleted.

-   With *Writer*, you can split sections by inserting headings:

    -   *Heading 1* → New part title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 2* → New chapter title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 3* → New section title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 4* → New appended section title. Optionally, you can
        add a description, separated by `|`.

    > **Important**
    > 
    > Documents with split sections are automatically discarded after the
    > *novelibre* project is updated.

-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.

-   Bold and italics cannot be combined.

-   The character styles *Emphasis* and *Strong Emphasis* are more
    suitable than hard formatting and are supported.

-   Change tracking: All changes are accepted on import. Change tracking
    data is lost.

## ${Manuscript for third-party word processing}

**Export an ODT document that can be imported again after editing**

With **${Export} > ${Manuscript for third-party word processing}**, you can
create a text document with visible section markers. File name suffix is
`_proof_tmp`.

> **Note**
> 
> This document retains its section information even if it is converted to
> other formats and back again. This may work with popular commercial word
> processors and even with web-based word processors such as Google Docs.

-   Only "${Normal}" chapters and sections are exported. Chapters and
    sections marked "${Unused}" are not exported.

-   The document contains chapter and section headings. However, changes
    will not be reimported.

-   The document contains section `[scx]` markers. **Do not touch lines
    containing the markers** if you want to be able to write the
    document back to *novelibre* format.

-   Chapters and sections can neither be rearranged nor deleted.

-   When editing the document, you can split sections by inserting
    headings or a section divider:

    -   *Heading 1* → New part title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 2* → New chapter title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 3* → New section title. Optionally, you can add a
        description, separated by `|`.
    -   *Heading 4* → New appended section title. Optionally, you can
        add a description, separated by `|`.

    > **Tip**
    > 
    > If you use a word processor whose heading styles cannot be properly
    > converted back to *.ODT* format for reimport, use *Markdown* heading
    > markers instead:
    > 
    > -   `#` begins a first-level heading.
    > -   `##` begins a second-level heading.
    > -   `###` begins a third-level heading.
    > -   `####` begins a fourth-level heading.
    > 
    > However, don't combine such markup with heading styles. Put a space
    > between the marker and the title. Additional blank lines are not
    > necessary.

    > **Important**
    > 
    > Documents with split sections are automatically discarded after the
    > *novelibre* project is updated.

-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.

-   Bold and italics cannot be combined.

-   The character styles *Emphasis* and *Strong Emphasis* are more
    suitable than hard formatting and are supported.

-   Change tracking: All changes are accepted on import. Change tracking
    data is lost.

## ${Final manuscript document (export only)}

**Export an ODT document**

With **${Export} > ${Final manuscript document (export only)}**, you can
create a text document for further use, e.g. a final document when you
are finished with *novelibre*.

> Hint
> 
> In contrast to the manuscript for editing, this document is not divided
> internally into sections, which could facilitate further processing and
> reformatting.

-   The document is placed in the same folder as the project.
-   Document's **filename**: `<project name>.odt`.
-   Only "${Normal}" chapters and sections are exported. Chapters and
    sections marked "${Unused}" are not exported.
-   Part titles appear as first level heading.
-   Chapter titles appear as second level heading.
-   Sections are separated by `* * *`. The first line is not indented.
-   Starting from the second paragraph, paragraphs begin with
    indentation of the first line.
-   Sections marked "attach to previous section" appear like
    continuous paragraphs.
-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.
-   The first paragraph of each chapter is assigned the paragraph style
    *Chapter beginning* which is by default like the body text without
    indentiation. By modifying this paragraph style you can give a
    special look to the beginnings ot the chapters, e.g. with initials.

> Tip
> 
> If you prefer simple blank lines instead of the three-asterisks in your
> final document, you can achieve this using "Find and replace". This is
> particularly convenient with a macro that comes with the
> [novelibre-tools](https://github.com/peter88213/novelibre-tools/)
> extension.

## ${Brief synopsis (export only)}

**Export an ODT document**

With **${Export} > ${Brief synopsis (export only)}**, you can create a text
document containing a brief synopsis with part, chapter, and sections
titles only. File name suffix is `_brf_synopsis`.

-   Only "${Normal}" chapters and sections are exported. Chapters and
    sections marked "${Unused}" are not exported.
-   Part titles appear as first level heading.
-   Chapter titles appear as second level heading.
-   Section titles appear as plain paragraphs.

## ${Cross references (export only)}

**Export an ODT document**

With **${Export} > ${Cross references (export only)}**, you can create a text
document containing navigable cross references. File name suffix is
`_xref`.

The cross references are:

-   Sections per character,
-   sections per location,
-   sections per item,
-   sections per tag,
-   characters per tag,
-   locations per tag,
-   items per tag.

## ${XML data files}

**Export XML files that can be imported into other projects**

With **${Export} > ${XML data files}**, you can create a set of XML files
containing the project's characters, locations, items, and plot lines
with all their properties. These files can be used to transfer the
elements to another projects.

> **Hint**
> 
> To import XML data files from another project, use the **${Import}**
> command in the **${Characters}**, **${Locations}**, **${Items}**, 
> or **${Plot}** menu.

## ${Options}

**Project independent program settings**

With **${Export} > ${Options}**, You can open a dialog for settings
concerning the document export.

### ${Ask before opening exported documents}

This checkbox controls the behavior on document export.

-   If ticked, you will be asked whether you want to have *novelibre*
    launch *Writer* or *Calc* with the newly created document opened.
-   If unticked, *novelibre* will launch *Writer* or *Calc* with the
    newly created document opened right away.

### ${Lock the project after document export for editing}

This checkbox controls the behavior on opening documents for editing.

-   If ticked, *novelibre* will lock the project when launching *Writer*
    or *Calc*.
-   If unticked, *novelibre* won't lock the project when launching
    *Writer* or *Calc*.

### ${Select document template}

You can have *novelibre* apply your own styles so that the exported text
documents better suit your taste and habits.

If you click on this button, a file select dialog will open. You can
select either an *.ott* document template or an *.odt* document.
*novelibre* will adopt the selected document's styles and use them for
ODT document export.

### ${Restore default styles}

If you click on this button, *novelibre* will discard the styles loaded
with **Select document template** and revert to its built-in default
styles.

---

[English manual](https://peter88213.github.io/nvhelp-en/)

