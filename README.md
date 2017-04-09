# on-my-vim
pathogen和vundle都是用来管理vim插件的，但是其作用的方面不同。这两个插件可同时使用。
* pathogen是为了解决每一个插件安装后文件分散到多个目录不好管理而存在的。
* vundle是为了解决自动搜索及下载插件而存在的。
可以在~/.vim/autoload/目录下用如下命令下载 

curl -Sso pathogen.vim https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim 
然后在配置文件的首行添加如下命令 
execute pathogen#infect() 
有了pathogen后，再下载的插件就直接把它们放到bundle目录下即可，而不需要管理相应的autoload、colors、plugin等目录。 
不过pathogen没有自动下载功能，所以再加一个vundle。 
在bundle目录下执行如下命令 
git clone https://github.com/gmarik/vundle.git 
然后在配置文件中添加如下内容

# vimconfig
This is a vim config files managed by pathogen: .vimrc is auto configured.

[NOTICE: 2017-04-09 14:15:28]
The vim version from command "➜  ~  vim --version" show be >= 7.4,because of "UltiSnips requires Vim >= 7.4". And you should execute the command "ln -s `pwd` ~/.vim".


vimconfig
=========

This is a vim config files managed by pathogen.After download the project, you should take a minute to know how `pathogen` [click me](https://github.com/tpope/vim-pathogen) works.

Features:
*	Some plugins which are used very often.
*	An easy way of extension, you can add anything as an submodule.
*	Easy to install and update: you need only one command.
*	Easy to compile and debug program: you need not exit your vim any more.

##1. what plugins are included  in this project?

###1.1 go
This is syntax hight for go language. You need not do nothing to invoke it.

###1.2 nerdtree
With this plugin, you can brow your file in one project more easily: it will be displayed in file tree.

**config**

	let g:nerdtree_tabs_open_on_console_startup=0
	let g:pydiction_location = '~/.vim/bundle/pydiction/complete-dict'
	map <leader>n <plug>NERDTreeTabsToggle <CR>

**invoke**
	To invoke it , just put `\n` in vim NORMAL mode.

###1.3 vim-commentary
**config**

	autocmd FileType python,shell set commentstring=#\ %s   " 设置Python注释字符
	autocmd FileType mako set cms=##\ %s
	nmap	,c  gcc
	nmap	,u	gcu

**invoke**

Select what you want to comment in visual mode. Then use `gcc` or `gcu`.
###1.4 vim-fileHeader
(to be added)
###1.5 vim-multicursor
(to be added)
###1.6 vim-pathogen
With this plugin, you can management much easier.

**config**

	filetype plugin indent on
	runtime bundle/vim-pathogen/autoload/pathogen.vim
	call pathogen#infect()
**invoe**

Do nothing.
###1.7 vimwiki
ignore
###1.8 neobundle.vim
(to be added)
###1.9 ultisnips
(to be added)
###1.10 vim-easymotion
(to be added)
###1.11 vim-markdown

This is just for syntax hightlight for markdown.
###1.12 vim-nerdtree-tabs
(to be added)
###1.13 vim-PinyinSearch
This is for search PinYin.
**config**

	vim-PinyinSearch
	let g:PinyinSearch_Dict = '/home/huangyk/.vim/bundle/vim-PinyinSearch/PinyinSearch.dict'
	map		?	:call PinyinSearch()<cr>
**invoke**

Just input `?` in NORMAL model.
###1.14 airline
This is usefull when you want to display some info about the pwd, model, filename, encode, and so on.

**config**

	"airline
	if !exists('g:airline_symbols')
		let g:airline_symbols = {}
	endif
	let g:airline_left_sep = '>'
	let g:airline_right_sep = '<'
	let g:airline_section_b = '%{getcwd()}'
	let g:airline#extensions#tabline#enabled = 1
	let g:airline#extensions#tabline#left_sep = ' '
	let g:airline#extensions#tabline#left_alt_sep = '|'
	" set the status line
	set laststatus=2
**invoe**

Do nothing.
###1.15 CtrlP
When there are many files in your project, chances are that you want to open the files which were opened recently.This plugin helps you to do this.

**config**

	"ctrlp
	let g:ctrlp_map = '<c-p>'
	let g:ctrlp_cmd = 'CtrlP'

**invode**

Input `<c-p>` in NORMAL model.

###1.16 taglist

In some IDE like Visual Studio or Eclipse, we can see the name of typedef,Class, Function and so on.This plugin can help you do this.
**config**

	"taglist 设置
	let Tlist_Show_One_File=1
	let Tlist_Exit_OnlyWindow=1
	let Tlist_Ctags_Cmd="/usr/bin/ctags"
	map tl	:Tlist<cr>
**invode**

Input `tl` in NORMAL model.

###1.17 winManager
This plugin will help you manage the windows in one terminal.
**config**

	"winManager config
	let g:winManagerWindowLayout='FileExplorer|TagList'
	map wm :WMToggle<cr>
	let g:AutoOpenWinManager = 1
**invoke**

Input `wm` in VIM NORMAL model.

##2. Easy compile&&debug

When you use `visual studio`, you can use `F7` to compile and `F5` to debug. Now you can also do this with our vimrc.

**Usage**

You can find this by "map key" in vimrc.
## 3 Installation

	git clone https://github.com/xqzhang2015/oh-my-vim.git
	./install

## 4. extention

**How to install new plugin**

* Download a plugin from github in to directory of `bundle`

	git clone $URL $PATH

* Add  this plugin as an submodule to your project

You can use git command to do this:

    git submodule add $URL $PATH

* Add the modification to the project, commit , and push it to your repository.

	git add $PATH
	git commit -m $MSG
	git push origin master
