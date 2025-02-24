# TPP Info Teletext

View the teletext pages [here](https://twitchplayspokemon.github.io/tpp-streamdocs/description/teletext/html/100.html).

There is also a [combined Rules page](https://twitchplayspokemon.github.io/tpp-streamdocs/description/teletext/html/rules.html).

## Editing

To update the teletext pages, use the included [editor](https://twitchplayspokemon.github.io/tpp-streamdocs/description/teletext/editor.html). Create a new page from scratch, or select an existing page to load from the dropdown. The editor can be a bit buggy with loading some pages, so if the page doesn't look right, try hitting your browser's refresh button.

Remember when building a page that the top line will be replaced with the page number and date, so do not use the top line.

To save a page, update the text file in the /description/teletext/pages folder. The naming scheme is important: `P###-title.txt`. The editor can export the page in many formats, but for our purposes, click on `raw (0x00-0x7f)` in the export list. This will copy the page in that format into your Clipboard. You can paste the contents of your Clipboard into the corresponding text file, replacing what was there.

After you have made all the relevant updates, commit the txt files to GitHub and send it as a pull request to this repository.

If your local fork has GitHub Actions enabled, the rendered teletext image files and html pages will be updated automatically. There is no need to modify these files. They will be generated anew when the pull request is accepted. 