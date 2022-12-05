# Vim Plugin for Rubber Duck Programming

This is a vim plugin that allows you to simulate rubber duck programming by using the chatGPT API to generate code suggestions and natural language explanations based on the selected lines of code and a user-specified query.

Rubber duck programming is a debugging technique in which explaining one's code to an inanimate object, such as a rubber duck, helps to identify and fix errors or improve the code. This vim plugin uses the chatGPT API to simulate this process by providing code suggestions and explanations in response to the user's query.

## Installation

To install the plugin, copy the `vim-python-script-runner.vim` file to your `~/.vim/plugin` directory, along with the Python script, and edit the path to the python script in the vim plugin. You'll also need to have `requests` installed for the Python script.

## Usage

1. Open a file in vim and enter Visual mode (by pressing `v`)
2. Select the lines of code you want to improve or debug
3. Press the key mapped to the `RunPythonScript` function (e.g. `<F9>`)
4. Enter your query when prompted (e.g. "How do I rewrite this more idiomatically?")
5. The chatGPT API will generate code suggestions and natural language explanations based on your selected lines and query

## Configuration

The `vim-python-script-runner.vim` file contains the following configuration variables that you can modify:

- `g:python_script_path`: The path to the Python script to run. The default value is `'python-script.py'`.
- `RunPythonScript` function: The function that runs the Python script. You can map it to a key by adding a line like `nnoremap <F9> :call RunPythonScript()<CR>` (to map it to `<F9>`).

## Python Script

The `python-script.py` file is a sample Python script that shows how to use the chatGPT API to generate code suggestions and natural language explanations based on the selected lines, active buffer's filename, and user-specified query. It receives these arguments from the vim plugin, and makes a post request to the chatGPT API with the appropriate data.

You can modify this script to customize the chatGPT API request and the handling of the response.

## Why Rubber Duck Programming

Rubber duck programming is a useful technique for improving code and debugging errors. By explaining one's code to an inanimate object, one is forced to articulate their thought process and consider their code from a different perspective, which can help identify and fix errors or improve the code.

Additionally, having a senior developer or mentor act as a "rubber duck" can be beneficial for junior developers, as it provides an opportunity to learn from experienced developers and gain exposure to their thought processes and problem-solving strategies.

## Credits

This vim plugin and Python script were co-ideated with [Frankie](https://twitter.com/FrankieIsLost) and [Assistant](chat.openai.com/chat), a large language model trained by OpenAI.
