hi clear
if exists("syntax_on")
    syntax reset
endif

let g:colors_name = 'chango'

let s:Black         = '#333333'
let s:RedShadow     = '#C64242'
let s:GreenShadow   = '#2E8942'
let s:LemonShadow   = '#CBAF2C'
let s:BlueShadow    = '#025594'
"let s:PurpleShadow  = '#854191'
let s:OrangeShadow  = '#CE8229'
let s:OceanShadow   = '#3C939D'
let s:MediumGrey    = '#DCDCDC'
let s:DarkGrey      = '#6C788B'
let s:Coral         = '#EF565C'
let s:Green         = '#5CB747'
let s:Lemon         = '#FFDB60'
let s:Blue          = '#1292D0'
"let s:Purple        = '#BB88DD'
let s:Orange        = '#F5A51C'
let s:Ocean         = '#4EB9C5'
let s:White         = '#FAFAFA'

exe 'hi ErrorMsg term=standout ctermbg=DarkRed guibg=' . s:RedShadow . ' ctermfg=White guifg=' . s:White
exe 'hi IncSearch term=reverse cterm=reverse gui=reverse'
exe 'hi ModeMsg term=bold cterm=bold gui=bold'
exe 'hi NonText term=bold ctermfg=Blue guifg=' . s:Blue
exe 'hi StatusLine term=reverse,bold cterm=reverse,bold gui=reverse,bold'
exe 'hi StatusLineNC term=reverse cterm=reverse gui=reverse'
exe 'hi VertSplit term=reverse cterm=reverse gui=reverse'
exe 'hi VisualNOS term=underline,bold cterm=underline,bold gui=underline,bold'
exe 'hi DiffText term=reverse cterm=bold gui=bold ctermbg=Red guibg=' . s:Coral
exe 'hi PmenuThumb cterm=reverse gui=reverse'
exe 'hi PmenuSbar ctermbg=Grey guibg=' . s:MediumGrey
exe 'hi TabLineSel term=bold cterm=bold gui=bold'
exe 'hi TabLineFill term=reverse cterm=reverse gui=reverse'
exe 'hi Cursor guibg=fg guifg=bg'
exe 'hi lCursor guibg=fg guifg=bg'

if &bg == 'light'
    exe 'hi Directory term=bold ctermfg=DarkBlue guifg=' . s:BlueShadow
    exe 'hi LineNr term=underline ctermfg=Brown guifg=' . s:LemonShadow
    exe 'hi MoreMsg term=bold ctermfg=DarkGreen guifg=' . s:GreenShadow
    exe 'hi Question term=standout ctermfg=DarkGreen guifg=' . s:GreenShadow
    exe 'hi Search term=reverse ctermbg=Yellow guibg=' . s:Lemon . ' ctermfg=NONE guifg=NONE'
    exe 'hi SpellBad term=reverse ctermbg=Red guibg=' . s:Coral
    exe 'hi SpellCap term=reverse ctermbg=Blue guibg=' . s:Blue
    exe 'hi SpellRare term=reverse ctermbg=Magenta guibg=' . s:Orange
    exe 'hi SpellLocal term=underline ctermbg=Cyan guibg=' . s:Ocean
    exe 'hi Pmenu ctermbg=Magenta guibg=' . s:Orange
    exe 'hi PmenuSel ctermbg=Grey guibg=' . s:MediumGrey
    exe 'hi SpecialKey term=bold ctermfg=DarkBlue guifg=' . s:BlueShadow
    exe 'hi Title term=bold ctermfg=DarkMagenta guifg=' . s:OrangeShadow
    exe 'hi WarningMsg term=standout ctermfg=DarkRed guifg=' . s:RedShadow
    exe 'hi WildMenu term=standout ctermbg=Yellow guibg=' . s:Lemon . ' ctermfg=Black guifg=' . s:Black
    exe 'hi Folded term=standout ctermbg=Grey guibg=' . s:MediumGrey . ' ctermfg=DarkBlue guifg=' . s:BlueShadow
    exe 'hi FoldColumn term=standout ctermbg=Grey guibg=' . s:MediumGrey . ' ctermfg=DarkBlue guifg=' . s:BlueShadow
    exe 'hi SignColumn term=standout ctermbg=Grey guibg=' . s:MediumGrey . ' ctermfg=DarkBlue guifg=' . s:BlueShadow
    exe 'hi Visual term=reverse'
    exe 'hi DiffAdd term=bold ctermbg=Blue guibg=' . s:Blue
    exe 'hi DiffChange term=bold ctermbg=Magenta guibg=' . s:Orange
    exe 'hi DiffDelete term=bold ctermfg=Blue guifg=' . s:Blue . ' ctermbg=Cyan guibg=' . s:Ocean
    exe 'hi TabLine term=underline cterm=underline gui=underline ctermfg=Black guifg=' . s:Black . ' ctermbg=Grey guibg=' . s:MediumGrey
    exe 'hi CursorColumn term=reverse ctermbg=Grey guibg=' . s:MediumGrey
    exe 'hi CursorLine term=underline cterm=underline gui=underline'
    exe 'hi MatchParen term=reverse ctermbg=Cyan guibg=' . s:Ocean
    exe 'hi Normal gui=NONE'
else
    exe 'hi Directory term=bold ctermfg=Cyan guifg=' . s:Ocean
    exe 'hi LineNr term=underline ctermfg=Yellow guifg=' . s:Lemon
    exe 'hi MoreMsg term=bold ctermfg=Green guifg=' . s:Green
    exe 'hi Question term=standout ctermfg=Green guifg=' . s:Green
    exe 'hi Search term=reverse ctermbg=Yellow guibg=' . s:Lemon . ' ctermfg=Black guifg=' . s:Black
    exe 'hi SpecialKey term=bold ctermfg=Blue guifg=' . s:Blue
    exe 'hi SpellBad term=reverse ctermbg=Red guibg=' . s:Coral
    exe 'hi SpellCap term=reverse ctermbg=Blue guibg=' . s:Blue
    exe 'hi SpellRare term=reverse ctermbg=Magenta guibg=' . s:Orange
    exe 'hi SpellLocal term=underline ctermbg=Cyan guibg=' . s:Ocean
    exe 'hi Pmenu ctermbg=Magenta guibg=' . s:Orange
    exe 'hi PmenuSel ctermbg=DarkGrey guibg=' . s:DarkGrey
    exe 'hi Title term=bold ctermfg=Magenta guifg=' . s:Orange
    exe 'hi WarningMsg term=standout ctermfg=Red guifg=' . s:Coral
    exe 'hi WildMenu term=standout ctermbg=Yellow guibg=' . s:Lemon . ' ctermfg=Black guifg=' . s:Black
    exe 'hi Folded term=standout ctermbg=DarkGrey guibg=' . s:DarkGrey . ' ctermfg=Cyan guifg=' . s:Ocean
    exe 'hi FoldColumn term=standout ctermbg=DarkGrey guibg=' . s:DarkGrey . ' ctermfg=Cyan guifg=' . s:Ocean
    exe 'hi SignColumn term=standout ctermbg=DarkGrey guibg=' . s:DarkGrey . ' ctermfg=Cyan guifg=' . s:Ocean
    exe 'hi Visual term=reverse'
    exe 'hi DiffAdd term=bold ctermbg=DarkBlue guibg=' . s:BlueShadow
    exe 'hi DiffChange term=bold ctermbg=DarkMagenta guibg=' . s:OrangeShadow
    exe 'hi DiffDelete term=bold ctermfg=Blue guifg=' . s:Blue . ' ctermbg=DarkCyan guibg=' . s:OceanShadow
    exe 'hi TabLine term=underline cterm=underline gui=underline ctermfg=White guifg=' . s:White . ' ctermbg=DarkGrey guibg=' . s:DarkGrey
    exe 'hi CursorColumn term=reverse ctermbg=DarkGrey guibg=' . s:DarkGrey
    exe 'hi CursorLine term=underline cterm=underline gui=underline'
    exe 'hi MatchParen term=reverse ctermbg=DarkCyan guibg=' . s:OceanShadow
    exe 'hi Normal gui=NONE'
endif
