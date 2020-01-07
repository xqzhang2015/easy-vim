
<!-- vim-markdown-toc GFM -->

* [easy-vim](#easy-vim)
* [vim](#vim)
		* [vim download](#vim-download)
		* [vim compile](#vim-compile)
		* [vim runtime](#vim-runtime)
* [plugins](#plugins)
		* [Vundle](#vundle)
		* [YouCompleMe](#youcompleme)
		* [YCM-Generator](#ycm-generator)
		* [tagbar](#tagbar)
		* [vim-markdown-toc](#vim-markdown-toc)
* [References](#references)

<!-- vim-markdown-toc -->

# easy-vim

```sh
git clone https://github.com/xqzhang2015/easy-vim.git .vim
```

# vim

### vim download

[]()

### vim compile

* enable perl, python, lua and etc

```sh
./configure --enable-perlinterp=dynamic --enable-pythoninterp=dynamic --enable-python3interp=dynamic --enable-luainterp=dynamic
```

### vim runtime

* Vim cannot find syntax.vim

```sh
make VIMRUNTIMEDIR=/usr/local/share/vim/vim82
```

# plugins

### Vundle

pathogen和vundle都是用来管理vim插件的，但是其作用的方面不同。这两个插件可同时使用。

* pathogen
  * pathogen是为了解决每一个插件安装后文件分散到多个目录不好管理而存在的。
* vundle
  * vundle是为了解决自动搜索及下载插件而存在的。
* vim-plug
  * a nice alternative to Vundle, but faster

### YouCompleMe

* install

```sh
# ~/easy-vim/bundle/YouCompleteMe
python install.py --clang-completer --go-completer --ts-completer
```

* Issue: about 400MB, too large

```sh
git clone --recursive https://github.com/Valloric/YouCompleteMe.git
```
* Issue 

[Option 2: Provide the flags manually](https://github.com/ycm-core/YouCompleteMe#option-2-provide-the-flags-manually)<br/>

```sh
NoExtraConfDetected: No .ycm_extra_conf.py file detected, so no compile flags are available. Thus no semantic support for C/C++/ObjC/ObjC++. Go READ THE DOCS *NOW*, DON'T fil...
```

```
https://github.com/ycm-core/YouCompleteMe#goto-commands
```

### YCM-Generator

[YCM-Generator](https://github.com/rdnetto/YCM-Generator.git)

* generate a `.ycm_extra_conf.py` file for use with YouCompleteMe

```sh
# under .../YCM-Generator/
python ./config_gen.py ~/docker/common/src -x c++ -C "--enable-selector --enable-debug ..."
cp ~/docker/common/src/.ycm_extra_conf.py ~/.vim/
```

```sh
# in vimrc
let g:ycm_global_ycm_extra_conf='~/.vim/.ycm_extra_conf.py'
```

### tagbar

* [Tagbar: a class outline viewer for Vim](https://github.com/majutsushi/tagbar)<br/>
* [ctags-compatible tag generator for Go](https://github.com/jstemmer/gotags)<br/>
  * ctags doesn't support golang
  * install: `go get -u github.com/jstemmer/gotags`

### vim-markdown-toc

* [vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc)

* usage: Generate table of contents in GFM link style
  * This command is suitable for Markdown files in GitHub repositories, like README.md
  * existing table of contents will auto update on save by default

```sh
:GenTocGFM
```

# References

[Vim Awesome](https://vimawesome.com/)<br/>

[]()<br/>

[]()<br/>

[]()<br/>

