set encoding=utf-8
" show line number
set nu

" set backspace
set backspace=indent,eol,start

" where the splits should occur
set splitbelow "sp
set splitright "vs

"split navigations
"nnoremap <C-J> <C-W><C-J> "move to the split below
"nnoremap <C-K> <C-W><C-K> "move to the split above
"nnoremap <C-L> <C-W><C-L> "move to the split right
"nnoremap <C-H> <C-W><C-H> "move to the split left

" Enable folding
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za

" ///////////////////////////////////////////////
set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
" set rtp+=~/easy-vim/bundle/Vundle.vim
set rtp+=~/.vim/bundle/Vundle.vim
"call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
call vundle#begin('~/.vim/bundle')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

"Plugin 'tmhedberg/SimpylFold'
" show the docstrings for folded code
"let g:SimpylFold_docstring_preview=1

" Syntax Checking/Highlighting
Plugin 'vim-syntastic/syntastic'
" C++ 11 syntax checking
let g:syntastic_cpp_compiler_options = '-std=c++11 -stdlib=libc++'
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" PEP(Python Enhancement Proposals) 8 checking 
Plugin 'nvie/vim-flake8'
let python_highlight_all=1

" NERD Tree 
Plugin 'vim-scripts/The-NERD-tree'
let NERDChristmasTree=0
let NERDTreeWinSize=30
map <C-n> :NERDTreeToggle<CR>
let NERDTreeWinPos="left"
" Automatically open a NERDTree if no files where specified
autocmd vimenter * if !argc() | NERDTree | endif
" Close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif

" Tagbar
Plugin 'vim-scripts/Tagbar'
let g:tagbar_width=35
let g:tagbar_autofocus=1
nmap <F6> :TagbarToggle<CR>
map <C-t> :TagbarToggle<CR>
" Close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:TagbarType") && b:TagbarType == "primary") | q | endif

Plugin 'Valloric/YouCompleteMe'
let g:ycm_global_ycm_extra_conf='~/.vim/.ycm_extra_conf.py'
let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_disable_for_files_larger_than_kb=1517475
let g:ycm_confirm_extra_conf=1
map <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

Plugin 'rdnetto/YCM-Generator'

Plugin 'tpope/vim-git'
Plugin 'vim-scripts/commentary.vim'
Plugin 'vim-scripts/Markdown'
Plugin 'vim-scripts/fugitive.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-scripts/vimwiki'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'vim-scripts/AutoClose'


" All of your Plugins must be added before the following line
call vundle#end()            " required

" To ignore plugin indent changes, instead use:
"filetype plugin on
filetype plugin indent on    " required

syntax on

set list " show Tab
set listchars=tab:\|\ , " use | to replace Tab

" airline

" indent set
set autoindent
" set expandtab "intention: whitespace instead of tab
set tabstop=4
set shiftwidth=4
set softtabstop=4

set list " show Tab
set listchars=tab:\|\ , " use | to replace Tab


" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"

" tagbar configuration for gotags
let g:tagbar_type_go = {
	\ 'ctagstype' : 'go',
	\ 'kinds'     : [
		\ 'p:package',
		\ 'i:imports:1',
		\ 'c:constants',
		\ 'v:variables',
		\ 't:types',
		\ 'n:interfaces',
		\ 'w:fields',
		\ 'e:embedded',
		\ 'm:methods',
		\ 'r:constructor',
		\ 'f:functions'
	\ ],
	\ 'sro' : '.',
	\ 'kind2scope' : {
		\ 't' : 'ctype',
		\ 'n' : 'ntype'
	\ },
	\ 'scope2kind' : {
		\ 'ctype' : 't',
		\ 'ntype' : 'n'
	\ },
	\ 'ctagsbin'  : 'gotags',
	\ 'ctagsargs' : '-sort -silent'
	\ }

