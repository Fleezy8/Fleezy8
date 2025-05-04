source $VIMRUNTIME/defaults.vim

" set basics
syntax on
colorscheme sorbet
set autoindent
set backspace=indent,eol,start
set softtabstop=4
set tabstop=4
"set number
set numberwidth=6
set noswapfile

" cursor line
set cursorline
set cursorlineopt=number
set relativenumber

" shortcuts
map bn :bn!<Enter>
map bp :bp!<Enter>
map ,e :20Lexplore<Enter>
map bs :buffers<Enter>:buffer
map bu :buffers<Enter>:bdelete
