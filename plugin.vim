" Vim Plugin for Rubber Duck Programming

function! RunPythonScript()
    " Get the selected lines
    let l:selected_lines = join(getline(visualmode()), "\n")

    " Get the active buffer's filename
    let l:filename = expand("%:p")

    " Prompt the user for a query
    let l:query = input("Enter your query: ")

    " Get the path to the Python script from the g:python_script_path variable
    let l:python_script_path = expand("<sfile>:p") . "/" . g:python_script_path

    " Run the Python script and save the output in a variable
    let l:output = system("python " . l:python_script_path . " " . l:selected_lines . " " . l:filename . " " . l:query)

    " Split the output into lines
    let l:lines = split(l:output, "\n")

    " Create a new floating window with the response from the Python script
    floating new
    floating resize 30
    floating position center

    " Loop through the lines and append them to the floating window
    for l:line in l:lines
        floating top
        floating wincmd P
        floating normal i
        call append(line("."), l:line)
    endfor
endfunction

" Set the default value for the g:python_script_path variable
let g:python_script_path = "python-script.py"

" Map the RunPythonScript function to the <F9> key
nnoremap <F9> :call RunPythonScript()<CR>
