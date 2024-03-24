# Norg Tutorial

\*This page is generated from [`./norg_tutorial.norg`](./norg_tutorial.norg)

I'd suggest reading [`./norg_tutorial.md`](https://github.com/pysan3/Norg-Tutorial/blob/main/norg_tutorial.md) first to do the installation and then clone the repo locally to read [How to Write Notes](norg_tutorial.norg#how-to-write-notes) in your neovim with the neorg plugin :)

## Useful Videos

- [From No Org to Neorg - Playlist](https://www.youtube.com/watch?v=NnmRVY22Lq8&list=PLx2ksyallYzVI8CN1JMXhEf62j2AijeDa)
  - [From No Org to Neorg - The Basics \| \#1](https://youtu.be/NnmRVY22Lq8)
  - [From No Org to Neorg - Workflow, Links \| \#2](https://youtu.be/Bi9JiW5nSig)
  - ...

I highly recommend you watch these videos by `Vhyrro`, the main contributor of [Neorg](https://github.com/nvim-neorg/neorg/) plugin. He says he'll start a devlog series soon as well.

# How to Get Started

The current implementations of `norg` format is mostly done with the [Neorg](https://github.com/nvim-neorg/neorg/) plugin.

## Installation Guide

Read this section. [Installation / Quickstart](https://github.com/nvim-neorg/neorg/#-installationquickstart)

- I'd recommend following the `Treesitter` section as well to install `tree-sitter-norg` spec.
  - `run = ":Neorg sync-parsers",`
- **Mac Users**: ensure that the CC environment variable points to a compiler that has C++14 support.
  - Details written in github README.
  - [Issue and How to solve](https://github.com/nvim-neorg/tree-sitter-norg/issues/7#issuecomment-1291508121)

## Kickstart Config

Here is my basic config. I'll explain about `modules` in [Modules](#modules).

``` lua
-- lazy.nvim spec
local M = {
  "nvim-neorg/neorg",
  ft = "norg",
  dependencies = {
    "nvim-treesitter/nvim-treesitter",
    "nvim-treesitter/nvim-treesitter-textobjects",
    "nvim-cmp",
    "nvim-lua/plenary.nvim",
  },
  build = ":Neorg sync-parsers",
  cmd = "Neorg",
}
local modules = {
  ["core.defaults"] = {},
  ["core.completion"] = { config = { engine = "nvim-cmp", name = "[Norg]" } },
  ["core.integrations.nvim-cmp"] = {},
  ["core.concealer"] = { config = { icon_preset = "diamond" } },
  ["core.keybinds"] = {
    -- https://github.com/nvim-neorg/neorg/blob/main/lua/neorg/modules/core/keybinds/keybinds.lua
    config = {
      default_keybinds = true,
      neorg_leader = "<Leader><Leader>",
    },
  },
  ["core.dirman"] = {
    config = {
      workspaces = {
        Notes = "~/Nextcloud/Notes",
        Work = "~/Nextcloud/Work",
      }
    }
  },
}
M.opts = {
  load = modules,
}
return M
```

If you still have problems setting up `neorg`, `@d-r-a-b` explains more thoroughly in [Understanding Neorg dependencies](https://gist.github.com/d-r-a-b/3af7083a018be15e6c1d1d2c5317e9c7). I'd really recommend this as well.

### `core.dirman`

This module manages what are called *workspaces*.

You can define multiple workspaces at `config["core.dirman"].config.workspaces`, and open with command `:Neorg workspace <name-of-workspace>`. This command opens `/path/to/workspace/index.norg` which is like the entry point file.

Norg files inside a workspace can be linked with `{:$<name-of-workspace>/path/to/file:}`. So for example, inside workspace `Notes = "~/Nextcloud/Notes"`, `~/Nextcloud/Notes/journal/2023-04-16.norg` would be `{:$Notes/journal/2023-04-16:}`. Or, it can be abbreviated to `$/` when referring from files in the same workspace. More info in [Links](#links) section.

# How to Write Your Notes

## Basics of Modules

There is a config option `config.load = {}` to define modules you want to use.

<sub>I decomposed that into a local var `modules` in above code for simplicity tho.</sub>

More information about modules in [Modules](#modules) section. I'd recommend just simply adding the ones already stated in [Kickstart Config](#kickstart-config).

## How to Write Notes

Below text is a sample note which explains about the norg syntax.

Run `:Neorg toggle-concealer` to see the raw text.

# Heading 1

- Spec: [Structural Detached Modifiers](1.0-specification.norg#structural-detached-modifiers)
  - This links to a local copy of <https://github.com/nvim-neorg/norg-specs/blob/main/1.0-specification.norg>.
  - Read [Before you start](https://github.com/pysan3/Norg-Tutorial#before-you-start) and download these files.

Normal text here. Single new line will be ignored.

Double new lines mean a new paragraph.

## Heading 2

Indentation of normal text is advised to align with the start of the heading name. See? The indentation of this text is different from the ones in [Heading 1](#heading-1).

Oh, BTW that's how you create in-document links. Literal heading name wrapped in `{}`. Press `<Enter>` on the link to jump to the definition. (case, space **in**-sensitive, punctuation **sensitive**). More about links in [links](#links)

With `---`, you can decrease the heading level. This text is inside [Heading 1](#heading-1) again.

- Bullet List
  - Spec: [Unordered Lists](1.0-specification.norg#unordered-lists)
  - Second level bullet is with `--` and not an indented `-`.
    - Third level
  - Second level
- In insert mode, press `<M-CR>` to create a new bullet.
  - Press `<C-t>`, `<C-d>` to increase, decrease the level.
  - More info can be found [Wiki - Indent](https://github.com/nvim-neorg/neorg/wiki/Indent) or [Raw code](https://github.com/nvim-neorg/neorg/blob/main/lua/neorg/modules/core/keybinds/keybinds.lua).

1.  Numbered List
    1.  Spec: [Ordered Lists](1.0-specification.norg#ordered-lists)
    2.  It's `~`, not `1.` (Tho the conceal makes it look like that)

- Can be mixed with bullets as well (not in markdown tho).

1.  Second

> Quotes
>
> > Spec: [Quotes](1.0-specification.norg#quotes)
> >
> > Quote level 2

- You can use [TODO lists](1.0-specification.norg#todo-status-extension) in combination with these lists.
  - I highly suggest reading this section as well.

# Links

- Spec: [Link Location](1.0-specification.norg#link-location)

There are so so many types of useful links in `norg`. You can also press `<Enter>` on all links to open the appropriate application. (e.g. urls are opened in the browser.)

Again, `Vhyrro` does a great job explaining about links in his video, [From No Org to Neorg \#2: 17:44~](https://youtu.be/Bi9JiW5nSig?t=17m44s) so go ahead and watch that video.

## Links Examples

- URL: `{https://xxx.example.com}`
  - URL with name: [Neorg GitHub](https://github.com/nvim-neorg/neorg/)
- Norg files
  - Relative to current file: `{:foo/bar:}` -\> `foo/bar.norg`
  - Absolute path: `{:/tmp/foo/bar:}` -\> `/tmp/foo/bar.norg`. (Also works with `~/` = `$HOME/`)
  - Relative to current workspace: `{:$/foo/bar:}` -\> `~/Norg/Notes/foo/bar.norg`
  - Relative to different workspace: `{:$work/foo/bar:}` -\> `~/Norg/work/foo/bar.norg`
- Usual files: `{/ /path/to/file}`
- Headings: [Heading 1](#heading-1)
  - Any level heading: [Heading 2](#heading-2)

**AND YOU CAN COMBINE THEM**

- `Heading 1` of `foo/bar.norg`: [Heading 1](foo/bar.norg#heading-1)
- Line numbers: [foo/bar](foo/bar.norg)

# Attached Modifiers

- \*bold\*: **bold**
- /italic/: *italic*
- \_underline\_: <u>underline</u>
- \-strike-through-: ~~strike-through~~
- !spoiler!: <span class="spoiler">spoiler</span>
- ^superscript^: <sup>superscript</sup> (cannot be nested into `subscript`)
- ,subscript,: <sub>subscript</sub> (cannot be nested into `superscript`)
- \`inline code\`: `inline code` (disables any nested markup - verbatim)
- %[null modifier](#null-modifier)%:
- \$inline math\$: $f(x) = y$ (verbatim)
- &variable&: <span class="variable">variable</span> (verbatim)

# Modules

Keys passed to `config.load` are name of modules. Their documents can be found in [Neorg - Wiki](https://github.com/nvim-neorg/neorg/wiki) -\> Pages.

I already mentioned the necessary ones in [Kickstart Config](#kickstart-config), but here are ones I personally use on top of them.

``` lua
local modules = {
  ... -- ones mentioned in {** Kickstart Config}
  ["core.esupports.metagen"] = { config = { type = "auto", update_date = true } },
  ["core.qol.toc"] = {},
  ["core.qol.todo_items"] = {},
  ["core.looking-glass"] = {},
  ["core.presenter"] = { config = { zen_mode = "zen-mode" } },
  ["core.export"] = {},
  ["core.export.markdown"] = { config = { extensions = "all" } },
  ["core.summary"] = {},
  ["core.tangle"] = { config = { report_on_empty = false } },
  ["core.ui.calendar"] = {},
  ["core.journal"] = {
    config = {
      strategy = "flat",
      workspace = "Notes",
    },
  },
}
```

## Notes for Important Modules

### `core.journal`

- <https://github.com/nvim-neorg/neorg/wiki/Journal>

This adds commands `:Neorg journal {today,tomorrow,yesterday}`, which opens norg file with the appropriate date as name. Also, take a look at [`core.ui.calendar`](https://github.com/nvim-neorg/neorg/wiki/Calendar) to add `:Neorg journal custom` command to choose a date with a calendar UI.

Great for diary :)

### `core.keybinds`

- <https://github.com/nvim-neorg/neorg/wiki/User-Keybinds>

To register `norg` file specific keybinds, read this section: [Neorg - Wiki - User-Keybinds - Setting Up a Keybind Hook](https://github.com/nvim-neorg/neorg/wiki/User-Keybinds#setting-up-a-keybind-hook).

The default keybinds are listed [here](https://github.com/nvim-neorg/neorg/blob/main/lua/neorg/modules/core/keybinds/keybinds.lua).

### `core.export`

- <https://github.com/nvim-neorg/neorg/wiki/Exporting-Files>

You will want [`core.export.markdown`](https://github.com/nvim-neorg/neorg/wiki/Markdown-Export) as well to export your files to markdown format.

Read [Export / Import](#export--import) section for instructions for other filetypes in detail.

### `core.summary`

- <https://github.com/nvim-neorg/neorg/wiki/Summary>

Use `:Neorg generate-workspace-summary` to generate a summary of the entire workspace with links to each respective entry.

It seems that it has some bugs that are being worked on.

- ✅ ~~<https://github.com/nvim-neorg/neorg/issues/1108>~~
- <https://github.com/nvim-neorg/neorg/issues/1071>

### `core.tangle`

- <https://github.com/nvim-neorg/neorg/wiki/Tangling>

Use `:Neorg tangle current-file` to export the code blocks in the current file into another file.

Basics are listed below, but you've got more options to control the output. See the [official wiki](https://github.com/nvim-neorg/neorg/wiki/Tangling#usage-tutorial) for more information.

#### Tangle each code block.

``` norg
#tangle init.lua
@code lua
-- This will be tangled to init.lua
print("Hello from init.lua!")
@end
```

#### Tangle entire document.

Specify output file inside `@document.meta`.

- Want to export to multiple files? =\> [More complex options.](https://github.com/nvim-neorg/neorg/wiki/Tangling#global-tangling-for-multiple-files)

``` norg
@document.meta
tangle: ./init.lua
@end

@code lua
-- This will be tangled to init.lua
print("Hello from init.lua!")
@end

#tangle.none
@code lua
-- Ignore this code block
print("Not tangled.")
@end
```

#### Automatically tangle current file on save using `autocmd`.

``` lua
vim.api.nvim_create_autocmd("BufWritePost", {
  pattern = "*.norg",
  command = "Neorg tangle current-file",
})
```

### `core.looking-glass`

- <https://github.com/nvim-neorg/neorg/wiki/Looking-Glass>

Use `:Neorg keybind all core.looking-glass.magnify-code-block` to edit code blocks in an external buffer, which allows LSPs and other language-specific tools to kick in.

![looking-glass](https://user-images.githubusercontent.com/76052559/216782314-5d82907f-ea6c-44f9-9bd8-1675f1849358.gif)

## Export / Import

You can convert your `norg` notes from / to different formats. You've got mainly three options to export and one to import. For exporting, I find [Export: `norg-pandoc`](#export-norgpandoc) the most stable at the moment (2023-11-05) but [Export: `norganic + pandoc + Norg.jl`](#export-norganic--pandoc--norgjl) works pretty well as well.

### Builtin Export Module

`:Neorg export to-file foo.md` -\> Exports to `foo.md` in markdown format.

This only supports markdown and the conversion is not very reliable. However, you can use this as a neovim command, so it's the easiest among others.

This is a function to export to `suffix` with the same dir and name of current file.

``` lua
local export_file = function(suffix, open_preview)
  local dst = vim.fn.fnamemodify(vim.fn.expand("%"), ":~:.:r") .. suffix -- same name but with suffix
  vim.cmd(string.format([[Neorg export to-file %s]], string.gsub(dst, " ", [[\ ]])))
  vim.schedule(function()
    vim.cmd.edit(dst)
    if suffix == ".md" and open_preview then
      vim.cmd([[MarkdownPreview]]) -- https://github.com/iamcco/markdown-preview.nvim
    end
  end)
end
-- export_file(".md", true)
```

### Export: `norganic + pandoc + Norg.jl`

[`Norg.jl`](https://github.com/Klafyvel/Norg.jl/) is a project to parse norg format file written in julia. [`norganic`](https://github.com/klafyvel/norganic) is a frontend of `Norg.jl` to use the tool from command line.

For installation document, please read norganic's [README](https://github.com/klafyvel/norganic).

- Example usage:
  - Convert norg file to html file.

``` bash
$ norganic html --input /path/to/file.norg --output /path/to/file.html
```

- Convert norg file to arbitrary file using `pandoc`.
  - norganic can output specific json format that pandoc understands and can convert to any format of file.
  - Note that things might not work here and there.

``` bash
$ norganic json --input /path/to/file.norg | pandoc -f json -t <file type you want> /path/to/output.xxx
```

### Export: `norg-pandoc`

[`norg-pandoc`](https://github.com/boltlessengineer/norg-pandoc) is a plugin for pandoc to parse norg format written in lua. A parser in directly added to pandoc, but you have to git clone and run pandoc inside `norg-pandoc`'s directory (or add this dir to lua's runtime path I guess?), so it is kinda cumbersome to run.

``` bash
$ git clone https://github.com/boltlessengineer/norg-pandoc.git
$ cd norg-pandoc
$ pandoc -f init.lua -t gfm /path/to/file.norg -o /path/to/output.md
# gfm (GitHub flavored markdown)
```

[./norg_tutorial.md](./norg_tutorial.md) is generated using this tool with a combination of [my custom script](https://github.com/pysan3/dotfiles/blob/main/static/remove_empty_lines_in_lists.py) to remove unnecessary newlines when exporting to markdown at the moment.

``` bash
$ pandoc -f init.lua -t gfm /path/to/norg_tutorial.norg | python remove_empty_lines_in_lists.py > /path/to/norg_tutorial.md
```

### Import: `pandoc + minorg`

[`minorg`](https://github.com/pysan3/minorg) is a tool to convert pandoc json format to norg file. Theoretically, it should be able to convert from all file formats that pandoc supports (and it's extensions).

Please install the tool via [minorg - Releases](https://github.com/pysan3/minorg/releases)

- Example usage:
  - Convert from markdown.

``` bash
$ pandoc -f markdown -t json /path/to/input/file.md | minorg generate -o /path/to/output.norg
```

- Convert Obsidian files.
  - Obsidian markdown flavor is a bit out of the standards and pandoc fails to parse it correctly.
  - I've implemented some workarounds specifically for obsidian style markdowns.

``` bash
$ pandoc -f markdown -f json /path/to/obsidian/file.md | minorg generate -o /path/to/output.norg --isObsidian --workRootDir=/path/to/workspace
```

- For more usage examples (for example convert whole dir recursively), please read the [README](https://github.com/pysan3/minorg).
- BTW, I'm the author of this cli tool, so if you have any problem, don't hesitate to send me an issue or feature request.

### Future: tree-sitter v3 parser

The tree-sitter parser for norg format version 3 is being worked at the moment. I've not been able to follow the development closely but I heard that it might work if you compile locally at the moment (2023-11-06).

After this parser is complete, we should be able to write a working importer / exporter with the output of the parser to plug into pandoc to have a reliable result.

## Image Support

Image support in norg file is partially done, partially not.

The syntax is like below and the second format is currently discussed for inline images.

``` norg
%preferred image syntax, image.nvim supports this out of the box%
.image /path/to/image.png

%inline image syntax being discussed. No real implementation or parser supports this yet%
{url}[alt text](image)
{/ /path/to/img.png}[alt text](image)
```

Parser or especially the [Builtin Export Module](#builtin-export-module) does not fully support this. Read [Embed Images](#embed-images) if you want a workaround to have a working markdown export now.

### Visualization

[`image.nvim`](https://github.com/3rd/image.nvim) is an awesome plugin that can inject the images inside the neovim buffer if you use *kitty-graphics-protocol* compatible terminal.

[Working example GIF](https://github.com/nvim-neorg/neorg/issues/971#issuecomment-1620775558).

## Table Syntax

The table syntax is one of the most powerfull, but really tricky thing in norg's specification. I will try my best to explain. Even if it's hard to comprehend, skim through til the [Table Format Examples](#table-format-examples) section and you might get the hang of it.

There are two syntax to define a table, one easy but limited and one that is very extensible.

### Markdown Wrapper

This format is very easy. It is basically the same as markdown table format wrapped in `@table - @end`.

One pro is that it should work with some markdown exporter at the momemt.

``` norg
@table
| Head a | Head b | Head c |
| -      | -      | -      |
| Cell 1 | Cell 2 | Cell 3 |
| Cell 4 | Cell 5 | Cell 6 |
@end
```

### Rich Table Format

This table format has infinite size table and you can specify the cell positions with movement (relative) commands.

Here are the three ways to write a cell. It consists of `: <movement> : cell content`.

``` norg
%basic format%
: .
  cell content

%shorthand syntax when content fits in single line%
: . : cell content

%multi line content syntax. you also need the closing :: below%
:: .
  - cell
  - content
::
```

Now let's talk about the movements. These should go into the `.` part in the above example. In this example, `A1` means first row, first column, `C2` means **second row (2)**, **third column (C)**. Look at `MS Excel` for more visual explanation.

- `.`: Top left (A1) of the table.
- `>` / `<`: Go one left / right.
  - You can prefix number to move multiple times. `3>` moves three right.
- `^` / `v`: Go one up / down. Also combine with numbers.
- `_`: Move to leftmost column on the next row. (If on `D1` and `_` will go to `A2`)
- `/`: Like `_` but vertically. Move one right and to the top. Imagine an upper-right arrow (↗️).

One special case is that when you go `<` on `A?` (left most column), it will wrap around and go to the cell one row above and all the way to the right (that has content). (`A2` -\> `<` -\> `X1`)

Another option other than relative movement is to specify absolute cell position.

- `: A1 : cell content`: Position `A1`.
- `: B1 : second cell`: Obviously cell next to `A1`.
- `: A1-A4 : multi row cell`: You can specify a multi row / column cell with this format.

#### Alignments

You can align the cell content with `+align right` above the cell row. Note that these are still **very work in progress** and neither the exporter nor the parser understand it, and *might even change in the future*. Other variances are...

- `+align left`: align a single cell
- `#align center`: align all cells to the center after this line
- `#align.columns A right`: align all cells in `A` column

### Table Format Examples

Let's wrap our heads around with some examples. The following tables represent the same thing.

``` norg
@table
(This is not a valid table, just added the wrapper to avoid parser errors)
| Head a    |    Head b |   Head c  |
| --------- | --------- | --------- |
| multi     | multi col cell        |
| row       | --------- | --------- |
| cell      |    Cell 5 |    Cell 6 |
| --------- | --------- | --------- |
@end

#align left
: . : Head a
+align right
: > : Head b
+align center
: > : Head c
: A2-A3 : multi row cell
: B2-C2 : multi col cell
#align right
: _> : Cell 5
: > : Cell 6
```

The following mimics table in [Markdown Wrapper](#markdown-wrapper). Although you can totally express this table with only `. > _`, I purposely used different notations as well. BTW, there are no ways to express `<th>` cells at the moment. The format is being discussed at [Discord](#discord) right now (2023-11-06).

``` norg
: . : Head a
: B1 : Head b
: C1
  Head c
: _ : Cell 1
: 5>4<
  Cell 2
:: >
  Cell 3
::
: >>>_ : Cell 4
: /2v : Cell 5
: _2>^ : Cell 6
```

## Macros

Macros in norg format starts with one of (`#`, `@`, `.`, `|`) and can invoke a function written in [Janet Langauge](https://janet-lang.org/). You've already seen this with `#align`, `@table`, `.image`, `|example` and so on. The spec hasn't matured yet but we are working on it steadily. We will see things like `+color:red` and many more interesting ones that connects to database soon ~~I mean pretty in long term...~~.

### Attached Modifier Extensions (WIP)

Macros or labels attached on attached modifiers.

Best example is the below where `(lang:norg)` extends the inline code block (backticks).

``` norg
- `* Heading`(lang:norg)
```

### Detached Modifier Extensions (WIP)

Kind of like a tag attached to headings, bullet points and some other stuffs.

Best example is the todo items where `- (x) item` means that this bullet point has attribute *TODO item* and *IS DONE*. These modifiers can be chained together with a pipe (`|`). Below example means a heading that is *TODO item* and *PENDING* and *PRIORITY A (A is highest)*.

``` norg
* (-|# A) Heading 1
```

## Your Own Module

If you want to create your own module for neorg, this video is very useful. [YouTube - Neorg Custom Modules](https://www.youtube.com/watch?v=j4lTvIGRhmw&list=PLxpY86LRR3B0rtOBjXAsq1XnsOt4m4owu)

Here's one external module I implemented: [neorg-templates](https://github.com/pysan3/neorg-templates), which adds support for template files with the power of `LuaSnip`.

Feel free to explorer the code.

# Explore More Norg

## [Awesome Neorg](https://github.com/NTBBloodbath/awesome-neorg)

> A collection of awesome Neorg notes, software and resources.

- You might find more useful neorg external modules to integrate to your workflow.

## [Other Official Projects](https://github.com/orgs/nvim-neorg/repositories)

There are many other projects going on around the `norg` format.

## GitHub Tags

Of course you can search through GitHub with tags.

- `norg`: <https://github.com/topics/norg>
  - More likely to find external modules.
- `neorg` <https://github.com/topics/neorg>
  - More likely to find personal dotfiles and other configs.

## Discord

More, alpha stage concepts are discussed in the Discord channel.

Feel free to join: <https://discord.gg/T6EgTAX7ht>

# Tips

## Embed Images

**This section is old.** Read [Image Support](#image-support) for new information. ~~As far as I know, there are **NO** specifications about how to embed / link to an image.~~

Update: 2023-10-19.

- Spec for image added: <https://github.com/nvim-neorg/norg-specs/issues/14>.

``` norg
.image /path/to/image.png
```

- There are also some attempts to add image preview support thanks to [image.nvim](https://github.com/3rd/image.nvim).
  - <https://github.com/nvim-neorg/neorg/issues/971>
- Markdown export and treesitter parsing is not yet *fully* implemented, so I'd suggest using the old workaround described below for now.

### OLD: Discussions

- [Is there any way to insert a image just like kitty icat does \#768](https://github.com/nvim-neorg/neorg/discussions/768)
- [render.nvim \#791](https://github.com/nvim-neorg/neorg/discussions/791)

### OLD: Workaround

As a workaround, funny enough, you can prepend a link with `!` like `!{path}[name]` to link to an image, which will be correctly converted to image tag when exported to markdown files. (Of course this only works with markdown and I hope this will not become the correct way.)

``` norg
  !{https://user-images.githubusercontent.com/76052559/150838408-1a021d7b-1891-4cab-b16e-6b755e741e87.png}[Norg format]
```

Example: ![Norg format](https://user-images.githubusercontent.com/76052559/150838408-1a021d7b-1891-4cab-b16e-6b755e741e87.png)

## Sync with Git, Nextcloud, etc

**BACKUP YOUR NOTES**

### Nextcloud, Edit on Your Phone

If you use selfhosted Nextcloud, you can edit your `norg` notes from your phone.

#### After Logging In

1.  Install [Notes app](https://apps.nextcloud.com/apps/notes)
2.  Go to <https://nextcloud.your.domain/apps/notes>
3.  Go down to `Notes settings`
4.  Change `File extension for new notes`
    1.  `User defined` -\> `.norg`

#### On Your Phone

1.  Access page with safari. <sub>I'm sorry but I use iPhone...</sub>
    1.  Shoud work on other phones as well tho.
2.  Go to <https://nextcloud.your.domain/apps/notes>
3.  Press `share` to `Add page to home`.
4.  You have a new app that jumps directly to notes

#### Notes

- Might not work if you have [Text](https://github.com/nextcloud/text) app installed
