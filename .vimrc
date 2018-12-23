execute pathogen#infect()
execute pathogen#helptags()
syntax on

autocmd vimenter * NERDTree | wincmd p 
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"set columns=112
set tabstop=4
set shiftwidth=4   
set softtabstop=4
set autoindent
set smartindent
set smarttab
set autowrite
set autochdir
filetype indent on
filetype on
filetype plugin on
filetype plugin indent on

let g:pymode_python = 'python3'
let g:pymode_options_colorcolumn = 1
let g:pymode_rope = 1
"let g:pymode_rope_completion = 1 
"let g:pymode_rope_complete_on_dot = 1
