# lang="ja" span extension for Markdown-Python

A small Python-Markdown extension for embedding Japanese content in multilingual markdown files into stylizable span tags using {{ }} brackets as span tags with a `lang="ja"` attribute. This is useful when you're writing multilingual pages utilizing Japanese and would like more styling control.

# Installation

Copy the `japanese.py` script into your python-markdown extension directory.

If you're using [Pelican](http://docs.getpelican.com/en/latest/) as static site generator, open your project's `pelicanconf.py` and add `'japanese'` to the `MD_EXTENSIONS` list:

``` python
    MD_EXTENSIONS = ['japanese']
```

## Usage

Using a simple regular expression <code>(\{\{)(.+?)(\}\})</code>, the extension treats double {} brackets as span tags with a `lang="ja"` attribute. 

``` markdown
    {{読書クラブ}}
```

thus outputs:

``` html
    <span lang="ja">読書クラブ</span>
```

Finally, ensure that your site's CSS recognises and display the pull quote correctly. There are several ways of achieving this. A sample CSS code utilizing Google Font's Noto japanese font could be:

``` css
    @import url(https://fonts.googleapis.com/earlyaccess/notosansjapanese.css);

    [lang="ja"] {
      font-family: "Noto Sans Japanese", "メイリオ","Meiryo","ヒラギノ角ゴ Pro W3",
      "Hiragino Kaku Gothic Pro","ＭＳ Ｐゴシック","MS PGothic",Sans-Serif;
      font-weight: 100;
      font-size: 90%;
    }
```

## License

lang_ja_span_markdown is licensed under the [MIT license](http://opensource.org/licenses/MIT), as provided in the LICENSE file.
